import argparse
import pandas as pd
from modules.data_description import DataDescription
from modules.data_imputation import DataImputation
from modules.data_encoding import EncodingCategoricalData
from modules.data_featurescaling import FeatureScaling
from modules.data_download import DatasetDownloader
class DataPreprocessingProject:
    
    def __init__(self):
        self.data = None
        self.target_variable = None
    
    def read_csv_input(self, input_file):
        try:
            self.data = pd.read_csv(input_file)
        except Exception as e:
            print("Error reading input file:", e)
            return
        
        print("Data loaded successfully from", input_file)
    
    def choose_target_variable(self, target_var):
        if target_var not in self.data.columns:
            print("Error: target variable not found in data")
            return
        
        self.target_variable = target_var
        self.data.drop(columns=[target_var], inplace=True)
        
        print("Target variable", target_var, "removed from data")
    
    def display_columns(self):
        print("Columns in the dataset:")
        print(self.data.columns)
    
    def describe_data(self):
        print("\nTask (Data Description)\n1.Display the description of a particular column\n2.Display the description of all columns\n3.Show the data set")
        
        data_desc = DataDescription(self.data)
        while(True):
            choice = (int)(input("Enter the choice(Press -1 to reject)"))
            if(choice == -1):
                return
            elif(choice == 1):
                col_name = input("Enter the column name ")
                data_desc.describe_string_column(col_name)
            elif(choice == 2):
                data_desc.describe_numeric_columns()
            elif(choice == 3):
                data_desc.print_rows(10)
        
    def handle_null_values(self):
        print("\nTask( Null value handling)\n1.Remove column\n2.Fill with mean\n3.Fill with median\n4.Fill with mode\n5.Show the data set")
       
        data_imp = DataImputation(self.data)
        while(True):
            choice = (int)(input("Enter the choice(Press -1 to reject)"))
            if(choice == -1):
                return
            elif(choice == 1):
                col_name = input("Enter the column name ")
                self.data =data_imp.remove_column(col_name)
            elif(choice == 2):
                col_name = input("Enter the column name ")
                self.data =data_imp.fill_null_with_mean(col_name)
            elif(choice == 3):
                col_name = input("Enter the column name ")
                self.data =data_imp.fill_null_with_median(col_name)
            elif(choice == 4):
                col_name = input("Enter the column name ")
                self.data =data_imp.fill_null_with_mode(col_name)       
            elif(choice == 5):

                self.data =data_imp.print_rows(10)
        pass
    
    def encode_categorical_data(self):
        print("\nTask (Encoding categorical data)\n1.Show categorical columns\n2.Perform one hot encoding of a column\n3.Show the data set")
        data_encode = EncodingCategoricalData(self.data)
        while(True):
            choice = (int)(input("Enter the choice(Press -1 to reject)"))
            if(choice == -1):
                return
            elif(choice == 2):
                col_name = input("Enter the column name ")
                self.data = data_encode.one_hot_encode(col_name)
            elif(choice == 1):
                data_encode.get_categorical_columns()
            elif(choice == 3):
                data_encode.print_rows(10)
        pass
    
    def feature_scaling(self):
        scaling = FeatureScaling(self.data)
        while(True):
            scaling_method = input("Enter scaling method (1: normalize, 2: standardize): ")
            columns = input("Enter column name(s) to scale (comma-separated): ")
            columns = [col.strip() for col in columns.split(",")]

            if scaling_method == "1":
                self.data = scaling.normalize(columns)
            elif scaling_method == "2":
                self.data = scaling.standardize(columns)
            else:
                print("Invalid scaling method selected")
            scaling.print_rows(10)
        pass
    
    def download_dataset(self):
        file_name = input("Enter appropriate name for your file ")
        downloader = DatasetDownloader(self.data, file_name)
        downloader.download_dataset()
        pass
    
    def perform_task(self, task_number):
        switcher = {
            1: self.describe_data,
            2: self.handle_null_values,
            3: self.encode_categorical_data,
            4: self.feature_scaling,
            5: self.download_dataset,
        }
        # Get the function from switcher dictionary
        func = switcher.get(task_number, lambda: "Invalid task number")
        # Execute the function
        func()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data preprocessing project')
    parser.add_argument('input_file', type=str, help='path to input CSV file')
    args = parser.parse_args()

    project = DataPreprocessingProject()
    
    project.read_csv_input(args.input_file)
    
    project.display_columns()

   
    while(True):
        print("\nThe Tasks are\n1.Data Description\n2.Handling NULL values\n3.Encoding Categorical Data\n4.Feature Scaling of the Dataset\n5.Download the modified dataset")
        task_number = int(input("Enter task number (press -1 to cancel): "))
        if task_number == -1:
            print("Task cancelled")
            break
        else:
            project.perform_task(task_number)