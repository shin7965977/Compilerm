from scipy.stats import beta
from scipy import stats


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def hypothesis_test_ROI(df, df2):
    product_cost = get_positive_float("Enter product cost: ")
    product_price = get_positive_float("Enter product price: ")
    
    grouped_df = df.groupby('date').agg({'ad Cost': 'sum', 'Buy': 'sum'}).reset_index()
    grouped_df['ROI'] = ((grouped_df['Buy'] * product_price) - (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])) / (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])

    grouped_df2 = df2.groupby('date').agg({'ad Cost': 'sum', 'Buy': 'sum'}).reset_index()
    grouped_df2['ROI'] = ((grouped_df2['Buy'] * product_price) - (product_cost * grouped_df2['Buy'] + grouped_df2['ad Cost'])) / (product_cost * grouped_df2['Buy'] + grouped_df2['ad Cost'])

    roi_before = grouped_df['ROI'].to_numpy()
    roi_after = grouped_df2['ROI'].to_numpy()

    grouped_df_row = grouped_df['ROI'].shape[0]
    grouped_df2_row = grouped_df2['ROI'].shape[0]

    if grouped_df_row == grouped_df2_row:
        # Perform paired sample t-test
        t_statistic, p_value = stats.ttest_rel(roi_before, roi_after)

        print("t statistic:", t_statistic)
        print("p-value:", p_value)

        # Determine significance
        alpha = 0.05  # Commonly used significance level
        if p_value < alpha:
            print("Reject the null hypothesis, there is sufficient evidence to suggest that the ROI of the new advertising is significantly higher than that of the old advertising")
        else:
            print("Cannot reject the null hypothesis, there is not enough evidence to suggest that the ROI of the new advertising is significantly higher than that of the old advertising")

    elif grouped_df_row != grouped_df2_row:
        # Perform Welch's t-test
        t_statistic, p_value = stats.ttest_ind(roi_before, roi_after, equal_var=False)

        print("t statistic:", t_statistic)
        print("p-value:", p_value)

        # Determine significance
        alpha = 0.05
        if p_value < alpha:
            print("Reject the null hypothesis, there is sufficient evidence to suggest that the ROI of the new advertising is significantly higher than that of the old advertising")
        else:
            print("Cannot reject the null hypothesis, there is not enough evidence to suggest that the ROI of the new advertising is significantly higher than that of the old advertising")


def hypothesis_test_Buy(df, df2):

    grouped_df = df.groupby('date').agg({'ad Cost': 'sum', 'Buy': 'sum'}).reset_index()
    grouped_df2 = df2.groupby('date').agg({'ad Cost': 'sum', 'Buy': 'sum'}).reset_index()

    Buy_before = grouped_df['Buy'].to_numpy()
    Buy_after = grouped_df2['Buy'].to_numpy()

    grouped_df_row = grouped_df['Buy'].shape[0]
    grouped_df2_row = grouped_df2['Buy'].shape[0]

    if grouped_df_row == grouped_df2_row:
        # Perform paired sample t-test
        t_statistic, p_value = stats.ttest_rel(Buy_before, Buy_after)

        print("t statistic:", t_statistic)
        print("p-value:", p_value)

        # Determine significance
        alpha = 0.05  # Commonly used significance level
        if p_value < alpha:
            print("Reject the null hypothesis, there is sufficient evidence to suggest that the Buy of the new advertising is significantly higher than that of the old advertising")
        else:
            print("Cannot reject the null hypothesis, there is not enough evidence to suggest that the Buy of the new advertising is significantly higher than that of the old advertising")

    elif grouped_df_row != grouped_df2_row:
        # Perform Welch's t-test
        t_statistic, p_value = stats.ttest_ind(Buy_before, Buy_after, equal_var=False)

        print("t statistic:", t_statistic)
        print("p-value:", p_value)

        # Determine significance
        alpha = 0.05
        if p_value < alpha:
            print("Reject the null hypothesis, there is sufficient evidence to suggest that the Buy of the new advertising is significantly higher than that of the old advertising")
        else:
            print("Cannot reject the null hypothesis, there is not enough evidence to suggest that the Buy of the new advertising is significantly higher than that of the old advertising")