### CSV upload
import pandas as pd
import epsilon_greedy_mab
import Thompson
import UCB
import Hypothesis_test
import numpy as np
from scipy.stats import beta
from scipy import stats
import data_visualization


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
    
        df = data_visualization.upload_and_read_csv()
        

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
        df = data_visualization.upload_and_read_csv("Please enter the data path before machine learning: ")  # Assuming this is the first data set
        df2 = data_visualization.upload_and_read_csv("Please enter the data path after machine learning: ")  # Assuming this is the second data set for comparison

        if hypothesis_choice == "1":
            # Perform hypothesis testing for ROI
            Hypothesis_test.hypothesis_test_ROI(df, df2)
        elif hypothesis_choice == "2":
            # Perform hypothesis testing for Buy
            Hypothesis_test.hypothesis_test_Buy(df, df2)