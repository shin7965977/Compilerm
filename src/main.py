### CSV upload
import pandas as pd
import csv
import epsilon_greedy_mab
import Thompson
import UCB
import Hypothesis_test
import numpy as np
from scipy.stats import beta
from scipy import stats
import math
import data_visualization


def upload_and_read_csv(prompt="Input data path: "):
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
        return None
    except Exception as e:
        print(f"An error occurred when loading data: {e}")
        return None

if __name__ == "__main__":
    choice = input("Please select the function to execute, Function 1: MAB Machine Learning, Function 2: Hypothesis Testing (Enter 1 or 2): ")
    
    while choice not in ["1", "2"]:
        print("Invalid input, please enter 1 or 2.")
        choice = input("Please select the function to execute, Function 1: MAB Machine Learning, Function 2: Hypothesis Testing (Enter 1 or 2): ")

    if choice == "1":
        goal_choice = input("Please choose the target for optimization, 1.ROI 2.Buy (Enter 1 or 2): ")
        while goal_choice not in ["1", "2"]:
            print("Invalid input, please enter 1 or 2.")
            goal_choice = input("Please choose the target for optimization, 1.ROI 2.Buy (Enter 1 or 2): ")

        algo_choice = input("Please choose the machine learning algorithm to use, 1.ε-greedy 2.Thompson Sampling 3.Upper Confidence Bound (UCB) (Enter 1, 2, 3): ")
        while algo_choice not in ["1", "2", "3"]:
            print("Invalid input, please enter 1, 2, or 3.")
            algo_choice = input("Please choose the machine learning algorithm to use, 1.ε-greedy 2.Thompson Sampling 3.Upper Confidence Bound (UCB) (Enter 1, 2, 3): ")
    
        df = upload_and_read_csv()
        
        data_visualization.generate_and_save_plots(df)

        if goal_choice == "1":
            if algo_choice == "1":
                epsilon_greedy_mab.epsilon_greedy_mab_ROI(df)
            elif algo_choice == "2":
                Thompson.Thompson_sampling_algorithm_ROI(df)
            elif algo_choice == "3":
                UCB.UCB_algorithm_ROI(df)

        elif goal_choice == "2":
            if algo_choice == "1":
                epsilon_greedy_mab.epsilon_greedy_mab_Buy(df)
            elif algo_choice == "2":
                Thompson.Thompson_sampling_algorithm_Buy(df)
            elif algo_choice == "3":
                UCB.UCB_algorithm_Buy(df)
    
    elif choice == "2":
        # Hypothesis testing functionality
        hypothesis_choice = input("Please choose the target for hypothesis testing: 1.ROI 2.Buy (Enter 1 or 2): ")
        while hypothesis_choice not in ["1", "2"]:
            print("Invalid input, please enter 1 or 2.")
            hypothesis_choice = input("Please choose the target for hypothesis testing: 1.ROI 2.Buy (Enter 1 or 2): ")

        # Assuming the upload_and_read_csv function returns a DataFrame
        df = upload_and_read_csv("Please enter the data path before machine learning: ")  # Assuming this is the first data set
        df2 = upload_and_read_csv("Please enter the data path after machine learning: ")  # Assuming this is the second data set for comparison

        if hypothesis_choice == "1":
            # Perform hypothesis testing for ROI
            Hypothesis_test.hypothesis_test_ROI(df, df2)
        elif hypothesis_choice == "2":
            # Perform hypothesis testing for Buy
            Hypothesis_test.hypothesis_test_Buy(df, df2)




