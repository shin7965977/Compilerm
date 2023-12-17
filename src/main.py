### CSV upload
import pandas as pd
import csv

def upload_and_read_csv():
    # Obtain the CSV file path from the user.
    file_path = input("Input data path: ")

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
    df = upload_and_read_csv()




# find out the size of the test set
import random
index = df.shape[0] // 5  # 20%
random.seed(697)  # initializes the random number generator
indices = list(range(0, df.shape[0]))
random.shuffle(indices)

training_indices = indices[:-index]
test_indices = indices[-index:]
