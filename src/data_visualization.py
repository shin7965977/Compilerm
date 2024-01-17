import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def generate_and_save_plots(df):
    # Convert the date into the correct format
    df['date'] = pd.to_datetime(df['date'])

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

# generate_and_save_plots(df)  
