import numpy as np
from scipy.stats import beta
import data_visualization
import pandas as pd

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


def Thompson_sampling_algorithm_ROI(df):
    # Data aggregation
    product_cost = get_positive_float("Enter product cost: ")
    product_price = get_positive_float("Enter product price: ")
    data_visualization.generate_and_save_plots(df, product_cost, product_price)
    grouped_df = df.groupby('ad group').agg({'ad Cost': 'sum', 'Buy': 'sum'}).reset_index()
    grouped_df['ROI'] = ((grouped_df['Buy'] * product_price) - (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])) / (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])

    # Initialize variables
    total_budget = get_positive_int("Enter number of budget: ")
    allocation = get_positive_int("Enter allocation amount per round: ")
    n_ad_groups = len(grouped_df)
    allocated_budget = np.zeros(n_ad_groups)
    rewards = np.zeros(n_ad_groups)
    trials = np.zeros(n_ad_groups)

    # Thompson Sampling Algorithm
    for _ in range(total_budget // allocation):
        sampled_theta = np.zeros(n_ad_groups)
        for i in range(n_ad_groups):
            sampled_theta[i] = beta(a=1+rewards[i], b=1+trials[i]-rewards[i]).rvs()
        
        chosen_ad_group = np.argmax(sampled_theta)
        allocated_budget[chosen_ad_group] += allocation
        trials[chosen_ad_group] += 1
        rewards[chosen_ad_group] += grouped_df.loc[chosen_ad_group, 'ROI']

    # Update DataFrame
    grouped_df['Counts'] = trials
    grouped_df['Budget Allocation'] = allocated_budget
    grouped_df.rename(columns={'ad Cost': 'Historical Ad Cost', 'Buy': 'Historical Buy', 'ROI': 'Historical Average ROI', 'ad group': 'Ad Group'}, inplace=True)

    print(grouped_df)


def simulate_buy_increase(ad_group_index, allocation, grouped_df, remaining_budget):
    # Estimate the increase in 'Buy' based on the allocated budget
    estimated_increase = allocation * grouped_df.loc[ad_group_index, 'Buy'] / grouped_df.loc[ad_group_index, 'ad Cost']
    # Ensure the estimated increase is non-negative and does not exceed the maximum number of trials allowed by the remaining budget
    max_possible_increase = remaining_budget / allocation
    return min(max(0, estimated_increase), max_possible_increase)


def Thompson_sampling_algorithm_Buy(df):
    # Data aggregation
    product_cost = get_positive_float("Enter product cost: ")
    product_price = get_positive_float("Enter product price: ")
    data_visualization.generate_and_save_plots(df, product_cost, product_price)
    grouped_df = df.groupby('ad group').agg({'ad Cost': 'sum', 'Buy': 'sum'}).reset_index()
    grouped_df['ROI'] = ((grouped_df['Buy'] * product_price) - (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])) / (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])

    # Initialize variables
    total_budget = get_positive_int("Enter number of budget: ")
    allocation = get_positive_int("Enter allocation amount per round: ")
    n_ad_groups = len(grouped_df)
    allocated_budget = np.zeros(n_ad_groups)
    successes = np.zeros(n_ad_groups)
    trials = np.zeros(n_ad_groups)
    remaining_budget = total_budget

    while remaining_budget > 0 and remaining_budget >= allocation:
        sampled_theta = np.zeros(n_ad_groups)
        for i in range(n_ad_groups):
            # Ensure the parameters of the Beta distribution are valid
            alpha_param = 1 + successes[i]
            beta_param = 1 + trials[i] - successes[i]
            if beta_param <= 0:
                raise ValueError(f"Beta distribution parameter 'b' must be positive, got {beta_param} for ad group {i}")
            sampled_theta[i] = beta(a=alpha_param, b=beta_param).rvs()

        chosen_ad_group = np.argmax(sampled_theta)
        allocated_budget[chosen_ad_group] += allocation
        remaining_budget -= allocation
        trials[chosen_ad_group] += 1
        
        # Call simulate_buy_increase to simulate the increase in 'Buy'
        buy_increase = simulate_buy_increase(chosen_ad_group, allocation, grouped_df, remaining_budget)
        if buy_increase + successes[chosen_ad_group] > trials[chosen_ad_group]:
            raise ValueError(f"The buy increase {buy_increase} would make successes greater than trials for ad group {chosen_ad_group}")
        successes[chosen_ad_group] += buy_increase
        
    # Update DataFrame to include final results
    grouped_df['Counts'] = trials
    grouped_df['Budget Allocation'] = allocated_budget
    grouped_df['Successes'] = successes

    print(grouped_df)


