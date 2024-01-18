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
    # 基本預處理和設置MAB模型
    # 按廣告組分組以獲得匯總指標
    grouped_df = df.groupby('ad group').agg({'ad Cost': 'sum', 'Buy': 'sum'})
    product_cost = get_positive_float("Enter product cost: ")
    product_price = get_positive_float("Enter product price: ")

    data_visualization.generate_and_save_plots(df,product_cost,product_price)
    # 重新计算ROI
    grouped_df['ROI'] = ((grouped_df['Buy'] * product_price) - (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])) / (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])
    grouped_df = grouped_df.reset_index()
    grouped_df.rename(columns={'ad group': 'Ad Group'}, inplace=True)
    # 定義廣告組的數量（MAB中的臂）
    n_arms = grouped_df.shape[0]
    arms = grouped_df.index.tolist()

    # 初始化ε-greedy算法的參數
    epsilon = get_positive_float_epsilon("Enter epsilon (a number between 0 and 1): ")  # 探索率
    n_rounds = get_positive_int("Enter number of rounds: ")  # 模擬回合數
    total_budget = get_positive_int("Enter number of budget: ")  # 所有組的總廣告成本

    # 初始化數組以存儲每個臂被玩的次數及其獎勵
    counts = np.zeros(n_arms)
    rewards = np.zeros(n_arms)

    # 根據ε-greedy算法選擇臂的函數
    def choose_arm(epsilon, counts):
        if random.random() > epsilon:
            # 利用：選擇平均獎勵最高的臂
            average_rewards = rewards / (counts + 1)  # 加1以避免除以零
            return np.argmax(average_rewards)
        else:
            # 探索：選擇一個隨機臂
            return np.random.randint(0, n_arms)

    # 模擬MAB模型
    for i in range(n_rounds):
        chosen_arm = choose_arm(epsilon, counts)
        # 模擬獎勵 - 在這裡我們使用歷史ROI作為獎勵的代理
        reward = grouped_df.iloc[chosen_arm]['ROI']
        # 更新次數和獎勵
        counts[chosen_arm] += 1
        rewards[chosen_arm] += reward

    # 根據模型計算最終分配
    final_allocation = (counts / counts.sum()) * total_budget

    # Append allocation results to the dataframe
    grouped_df['Counts'] = counts
    grouped_df['Budget Allocation'] = final_allocation
    # Change column's name
    grouped_df.rename(columns={'ad Cost': 'Historical Ad Cost'}, inplace=True)
    grouped_df.rename(columns={'Buy': 'Historical Buy'}, inplace=True)
    grouped_df.rename(columns={'ROI': 'Historical Average ROI'}, inplace=True)
    grouped_df.rename(columns={'ROI': 'Historical Average ROI'}, inplace=True)
    



    print(grouped_df)

def epsilon_greedy_mab_Buy(df):
    # 基本預處理和設置MAB模型
    # 按廣告組分組以獲得匯總指標
    grouped_df = df.groupby('ad group').agg({'ad Cost': 'sum', 'Buy': 'sum'})
    product_cost = get_positive_float("Enter product cost: ")
    product_price = get_positive_float("Enter product price: ")
    data_visualization.generate_and_save_plots(df,product_cost,product_price)
    grouped_df = grouped_df.reset_index()
    grouped_df.rename(columns={'ad group': 'Ad Group'}, inplace=True)
    # 重新计算ROI
    grouped_df['ROI'] = ((grouped_df['Buy'] * product_price) - (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])) / (product_cost * grouped_df['Buy'] + grouped_df['ad Cost'])

    # 定義廣告組的數量（MAB中的臂）
    n_arms = grouped_df.shape[0]
    arms = grouped_df.index.tolist()

    # 初始化ε-greedy算法的參數
    epsilon = get_positive_float_epsilon("Enter epsilon (a number between 0 and 1): ")  # 探索率
    n_rounds = get_positive_int("Enter number of rounds: ")  # 模擬回合數
    total_budget = get_positive_int("Enter number of budget: ")  # 所有組的總廣告成本

    # 初始化數組以存儲每個臂被玩的次數及其獎勵
    counts = np.zeros(n_arms)
    rewards = np.zeros(n_arms)

    # 根據ε-greedy算法選擇臂的函數
    def choose_arm(epsilon, counts):
        if random.random() > epsilon:
            # 利用：選擇平均獎勵最高的臂
            average_rewards = rewards / (counts + 1)  # 加1以避免除以零
            return np.argmax(average_rewards)
        else:
            # 探索：選擇一個隨機臂
            return np.random.randint(0, n_arms)
        

        # 模擬MAB模型
    for i in range(n_rounds):
        chosen_arm = choose_arm(epsilon, counts)
        # 模擬獎勵 - 在這裡我們使用歷史Buy作為獎勵的代理
        reward = grouped_df.iloc[chosen_arm]['Buy']
        # 更新次數和獎勵
        counts[chosen_arm] += 1
        rewards[chosen_arm] += reward  # 注意這裡是累加Buy
        # 累加选择的臂和奖励


    # 根據模型計算最終分配
    final_allocation = (counts / counts.sum()) * total_budget

    # Append allocation results to the dataframe
    grouped_df['Counts'] = counts
    grouped_df['Budget Allocation'] = final_allocation
    # Change column's name
    grouped_df.rename(columns={'ad Cost': 'Historical Ad Cost'}, inplace=True)
    grouped_df.rename(columns={'Buy': 'Historical Buy'}, inplace=True)
    grouped_df.rename(columns={'ROI': 'Historical Average ROI'}, inplace=True)
    grouped_df.rename(columns={'ROI': 'Historical Average ROI'}, inplace=True)
    


    

    print(grouped_df)