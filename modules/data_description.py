import pandas as pd
class DataDescription:
    
    def __init__(self,data):
        self.data = data
    
    def describe_numeric_columns(self):
        numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_cols:
            print("Column:", col)
            print("Data Type:", self.data[col].dtype)
            print("Null Values:", self.data[col].isnull().sum())
            print("Mean:", self.data[col].mean())
            print("Std Dev:", self.data[col].std())
            print("25%:", self.data[col].quantile(0.25))
            print("50%:", self.data[col].quantile(0.50))
            print("75%:", self.data[col].quantile(0.75))
            print("Max:", self.data[col].max())
            print("Min:", self.data[col].min())
            print("===" * 20)
        non_numeric_cols = self.data.select_dtypes(exclude =['float64', 'int64']).columns
        for col in non_numeric_cols:
            print("Column:", col)
            print("Data Type:", self.data[col].dtype)
            print("Null Values:", self.data[col].isnull().sum())
            print("===" * 20)
    def describe_string_column(self, col_name):
        if col_name not in self.data.columns:
            print("Error: column not found")
            return
        
        col = self.data[col_name]
        
        print("Column:", col_name)
        print("Data Type:", col.dtype)
        print("Null Values:", col.isnull().sum())
        print("Total Values:", len(col))
        if col.dtype == 'object':
            print("Distinct Values:", col.nunique())
        print("===" * 20)
    
    def print_rows(self, n):
        print(self.data.head(n))
    