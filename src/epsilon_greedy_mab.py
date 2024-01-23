import pandas as pd
import numpy as np
import random
import data_visualization

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

def get_positive_float_epsilon(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 < value <= 1:
                return value
            else:
                print("Please enter a number greater than 0 and less than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def epsilon_greedy_mab_ROI(df):
    # Basic preprocessing and setting up the MAB model
    # Group by ad group to get aggregate metrics
    grouped_df = df.groupby('ad group').agg({'ad Cost': 'sum', 'Buy': 'sum'})
    product_cost = get_positive_float("Enter product cost: ")
    product_price = get_positive_float("Enter product price: ")

    data_visualization.generate_and_save_plots(df,product_cost,product_price)
    # Recalculate ROI
    grouped_df['ROI'] = ((grouped_df['Buy'] * product_price) - (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])) / (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])
    grouped_df = grouped_df.reset_index()
    grouped_df.rename(columns={'ad group': 'Ad Group'}, inplace=True)
    # Define the number of ad groups (arms in the MAB)
    n_arms = grouped_df.shape[0]
    arms = grouped_df.index.tolist()

    # Initialize parameters for the ε-greedy algorithm
    epsilon = get_positive_float_epsilon("Enter epsilon (a number between 0 and 1): ")  # Exploration rate
    n_rounds = get_positive_int("Enter number of rounds: ")  # Number of simulation rounds
    total_budget = get_positive_int("Enter total budget: ")  # Total ad cost for all groups

    # Initialize arrays to store the number of times each arm is played and their rewards
    counts = np.zeros(n_arms)
    rewards = np.zeros(n_arms)

    # Function to choose an arm based on the ε-greedy algorithm
    def choose_arm(epsilon, counts):
        if random.random() > epsilon:
            # Exploit: choose the arm with the highest average reward
            average_rewards = rewards / (counts + 1)  # Add 1 to avoid division by zero
            return np.argmax(average_rewards)
        else:
            # Explore: choose a random arm
            return np.random.randint(0, n_arms)

    # Simulate the MAB model
    for i in range(n_rounds):
        chosen_arm = choose_arm(epsilon, counts)
        # Simulate reward - here we use historical ROI as a proxy for the reward
        reward = grouped_df.iloc[chosen_arm]['ROI']
        # Update counts and rewards
        counts[chosen_arm] += 1
        rewards[chosen_arm] += reward

    # Calculate the final allocation based on the model
    final_allocation = (counts / counts.sum()) * total_budget

    # Append allocation results to the dataframe
    grouped_df['Counts'] = counts
    grouped_df['Budget Allocation'] = final_allocation
    # Change column names
    grouped_df.rename(columns={'ad Cost': 'Historical Ad Cost', 'Buy': 'Historical Buy', 'ROI': 'Historical Average ROI'}, inplace=True)
    
    print(grouped_df)

def epsilon_greedy_mab_Buy(df):
    # Basic preprocessing and setting up the MAB model
    # Group by ad group to get aggregate metrics
    grouped_df = df.groupby('ad group').agg({'ad Cost': 'sum', 'Buy': 'sum'})
    product_cost = get_positive_float("Enter product cost: ")
    product_price = get_positive_float("Enter product price: ")
    data_visualization.generate_and_save_plots(df,product_cost,product_price)
    grouped_df = grouped_df.reset_index()
    grouped_df.rename(columns={'ad group': 'Ad Group'}, inplace=True)
    # Recalculate ROI
    grouped_df['ROI'] = ((grouped_df['Buy'] * product_price) - (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])) / (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])

    # Define the number of ad groups (arms in the MAB)
    n_arms = grouped_df.shape[0]
    arms = grouped_df.index.tolist()

    # Initialize parameters for the ε-greedy algorithm
    epsilon = get_positive_float_epsilon("Enter epsilon (a number between 0 and 1): ")  # Exploration rate
    n_rounds = get_positive_int("Enter number of rounds: ")  # Number of simulation rounds
    total_budget = get_positive_int("Enter total budget: ")  # Total ad cost for all groups

    # Initialize arrays to store the number of times each arm is played and their rewards
    counts = np.zeros(n_arms)
    rewards = np.zeros(n_arms)

    # Function to choose an arm based on the ε-greedy algorithm
    def choose_arm(epsilon, counts):
        if random.random() > epsilon:
            # Exploit: choose the arm with the highest average reward
            average_rewards = rewards / (counts + 1)  # Add 1 to avoid division by zero
            return np.argmax(average_rewards)
        else:
            # Explore: choose a random arm
            return np.random.randint(0, n_arms)

    # Simulate the MAB model
    for i in range(n_rounds):
        chosen_arm = choose_arm(epsilon, counts)
        # Simulate reward - here we use historical Buy as a proxy for the reward
        reward = grouped_df.iloc[chosen_arm]['Buy']
        # Update counts and rewards
        counts[chosen_arm] += 1
        rewards[chosen_arm] += reward  # Note here we are accumulating Buy
        # Accumulate the chosen arm and reward

    # Calculate the final allocation based on the model
    final_allocation = (counts / counts.sum()) * total_budget

    # Append allocation results to the dataframe
    grouped_df['Counts'] = counts
    grouped_df['Budget Allocation'] = final_allocation
    # Change column names
    grouped_df.rename(columns={'ad Cost': 'Historical Ad Cost', 'Buy': 'Historical Buy', 'ROI': 'Historical Average ROI'}, inplace=True)
    
    print(grouped_df)
