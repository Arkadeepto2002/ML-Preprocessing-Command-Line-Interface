
import pandas as pd
class EncodingCategoricalData:
    
    def __init__(self, data):
        self.data = data
    
    def get_categorical_columns(self):
        categorical_cols = [col for col in self.data.columns if self.data[col].dtype == 'object']
        if not categorical_cols:
            print("No categorical columns found")
        else:
            print(f"Categorical columns: {', '.join(categorical_cols)}")
    
    def one_hot_encode(self, col_name):
        if col_name not in self.data.columns:
            print("Error: column not found")
            return
        
        if self.data[col_name].dtype != 'object':
            print("Error: column is not categorical")
            return
        
        encoded_data = pd.get_dummies(self.data[col_name], prefix=col_name)
        self.data = pd.concat([self.data, encoded_data], axis=1)
        self.data.drop(columns=[col_name], inplace=True)
        print(f"{col_name} column one-hot encoded")
        return self.data

    def print_rows(self, n):
        print(self.data.head(n))