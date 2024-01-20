import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv


def upload_and_read_csv(prompt="Input data path: "):
    while True:
        # Obtain the CSV file path from the user.
        file_path = input(prompt)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the file contents using csv.reader.
                csv_reader = csv.reader(file)
                # Convert csv_reader to a list of lists.
                data_list = list(csv_reader)
                # Create a DataFrame from the list of lists.
                # The first row of the CSV is typically the header, which we use for column names.
                df = pd.DataFrame(data_list[1:], columns=data_list[0])
                # Convert columns to appropriate data types.
                df = df.apply(pd.to_numeric, errors='ignore')
                pd.set_option('display.width', 1000)
                return df

        except FileNotFoundError:
            print(f"Can't find CSV: {file_path}")
        except Exception as e:
            print(f"An error occurred when loading data: {e}")

def generate_and_save_plots(df, product_cost, product_price):
    # Convert the date into the correct format
    df['date'] = pd.to_datetime(df['date'])

    # 不管 'ROI' 列是否存在，都删除并重新创建 'ROI' 列
    # 删除 'ROI' 列（如果存在）
    if 'ROI' in df.columns:
        df.drop('ROI', axis=1, inplace=True)

    # 然后重新创建 'ROI' 列，并根据给定公式计算值
    df['ROI'] = ((df['Buy'] * product_price) - 
                (product_cost * df['Buy'] + df['ad Cost'])) / \
                (product_cost * df['Buy'] + df['ad Cost'])

    # Create a chart containing a subplot with one row and three columns.
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 5))
    unique_ad_groups = df['ad group'].unique()

    # for group
    for i, ad_group in enumerate(unique_ad_groups):
        ax = axes[i]
        group_data = df[df['ad group'] == ad_group]

        # for ad
        for ad in df['ad'].unique():
            ad_data = group_data[group_data['ad'] == ad]
            ax.plot(ad_data['date'], ad_data['ROI'], label=f'Ad {ad}')

        ax.set_title(f'Ad Group {ad_group}')
        ax.set_xlabel('Date')
        ax.set_ylabel('ROI')

        # Set the date format of the X-axis to show only the month and day.
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        ax.legend()

    plt.tight_layout()
    plt.show()

    # Boxplot for ROI across different ad groups
    plt.figure(figsize=(10, 6))
    boxplot_data = [df[df['ad group'] == group]['ROI'] for group in unique_ad_groups]
    plt.boxplot(boxplot_data, labels=unique_ad_groups)
    plt.title('ROI in different ad groups')
    plt.ylabel('ROI')
    plt.xlabel('Ad Group')
    plt.show()

    # Scatter plot - Draw a scatter plot for each ad group.
    fig, axs = plt.subplots(1, 3, figsize=(20, 5), sharey=False)
    ad_groups = df['ad group'].unique()
    ads = df['ad'].unique()

    for i, group in enumerate(ad_groups):
        for ad in ads:
            group_data = df[(df['ad group'] == group) & (df['ad'] == ad)]
            axs[i].scatter(group_data['ad Cost'], group_data['Buy'], label=f'Ad {ad}')
        axs[i].set_title(f'Ad Group {group}')
        axs[i].set_xlabel('ad Cost')
        axs[i].legend()

    axs[0].set_ylabel('Buy')

    plt.tight_layout()
    plt.show()
