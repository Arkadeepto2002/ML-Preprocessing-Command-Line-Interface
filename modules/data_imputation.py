import pandas as pd
import numpy as np
class DataImputation:
    
    def __init__(self, data):
        self.data = data
    
    def remove_column(self, col_name):
        if col_name not in self.data.columns:
            print("Error: column not found")
            return
        
        self.data.drop(columns=[col_name], inplace=True)
        print(f"{col_name} column removed")

        return self.data
    def fill_null_with_mean(self, col_name):
        if col_name not in self.data.columns:
            print("Error: column not found")
            return
        if self.data[col_name].dtype != 'object':
            self.data[col_name].fillna(self.data[col_name].mean(), inplace=True)
            print(f"Null values in {col_name} column filled with mean")
        else:
            print("It's a non-categorical object, can't work with that")
        return self.data

    def fill_null_with_median(self, col_name):
        if col_name not in self.data.columns:
            print("Error: column not found")
            return
        
        if self.data[col_name].dtype != 'object':
            self.data[col_name].fillna(self.data[col_name].median(), inplace=True)
            print(f"Null values in {col_name} column filled with mean")
        else:
            print("It's a non-categorical object, can't work with that")
        return self.data
    def fill_null_with_mode(self, col_name):
        if col_name not in self.data.columns:
            print("Error: column not found")
            return
        
        if self.data[col_name].dtype != 'object':
            self.data[col_name].fillna(self.data[col_name].mode(), inplace=True)
            print(f"Null values in {col_name} column filled with mean")
        else:
            print("It's a non-categorical object, can't work with that")
        return self.data
    def print_rows(self, n):
        print(self.data.head(n))