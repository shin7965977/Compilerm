import numpy as np
import pandas as pd
import math
import data_visualization

df = pd.read_csv(r"C:\Users\shin7\Desktop\new\data\raw data.csv")


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


def UCB_algorithm_ROI(df):
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
    allocated_budget_ucb = np.zeros(n_ad_groups)
    # Initialize variables for UCB algorithm

    rewards = np.zeros(n_ad_groups)
    trials = np.zeros(n_ad_groups)
    total_iterations = total_budget // allocation

    # UCB Algorithm
    for t in range(1, total_iterations + 1):
        ucb_values = np.zeros(n_ad_groups)
        for i in range(n_ad_groups):
            if trials[i] > 0:
                # Calculate average reward and UCB value
                average_reward = rewards[i] / trials[i]
                delta_i = math.sqrt(2 * math.log(t) / trials[i])
                ucb_values[i] = average_reward + delta_i
            else:
                # Assign a very high UCB value to encourage exploration
                ucb_values[i] = 1e400

        # Choose the ad group with the highest UCB value
        chosen_ad_group = np.argmax(ucb_values)

        # Allocate budget and update rewards and trials
        allocated_budget_ucb[chosen_ad_group] += allocation
        trials[chosen_ad_group] += 1
        rewards[chosen_ad_group] += grouped_df.loc[chosen_ad_group, 'ROI']


    # Update DataFrame
    grouped_df['Counts'] = trials
    grouped_df['Budget Allocation'] = allocated_budget_ucb
    grouped_df.rename(columns={'ad Cost': 'Historical Ad Cost', 'Buy': 'Historical Buy', 'ROI': 'Historical Average ROI', 'ad group': 'Ad Group'}, inplace=True)

    print(grouped_df)


def UCB_algorithm_Buy(df):
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
    allocated_budget_ucb = np.zeros(n_ad_groups)
    rewards = np.zeros(n_ad_groups)
    trials = np.zeros(n_ad_groups)
    total_iterations = total_budget // allocation

    # UCB Algorithm
    for t in range(1, total_iterations + 1):
        ucb_values = np.zeros(n_ad_groups)
        for i in range(n_ad_groups):
            if trials[i] > 0:
                # Calculate average reward and UCB value based on 'Buy'
                average_reward = rewards[i] / trials[i]
                delta_i = math.sqrt(2 * math.log(t) / trials[i])
                ucb_values[i] = average_reward + delta_i
            else:
                # Assign a very high UCB value to encourage exploration
                ucb_values[i] = 1e400

        # Choose the ad group with the highest UCB value
        chosen_ad_group = np.argmax(ucb_values)

        # Allocate budget and update rewards and trials based on 'Buy'
        allocated_budget_ucb[chosen_ad_group] += allocation
        trials[chosen_ad_group] += 1
        rewards[chosen_ad_group] += grouped_df.loc[chosen_ad_group, 'Buy']

    # Update DataFrame
    grouped_df['Counts'] = trials
    grouped_df['Budget Allocation'] = allocated_budget_ucb
    grouped_df.rename(columns={'ad Cost': 'Historical Ad Cost', 'Buy': 'Historical Buy', 'ROI': 'Historical Average ROI', 'ad group': 'Ad Group'}, inplace=True)

    print(grouped_df)