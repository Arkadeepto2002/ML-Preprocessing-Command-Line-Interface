from sklearn.preprocessing import MinMaxScaler, StandardScaler

class FeatureScaling:
    def __init__(self, data):
        self.data = data

    def normalize(self, cols):
        try:
            scaler = MinMaxScaler()
            self.data[cols] = scaler.fit_transform(self.data[cols])
            print(f"{cols} column(s) normalized")
        except KeyError:
            print("Invalid column name(s) provided")
        except Exception as e:
            print(f"Error occurred during normalization: {str(e)}")
        return self.data

    def standardize(self, cols):
        try:
            scaler = StandardScaler()
            self.data[cols] = scaler.fit_transform(self.data[cols])
            print(f"{cols} column(s) standardized")
        except KeyError:
            print("Invalid column name(s) provided")
        except Exception as e:
            print(f"Error occurred during standardization: {str(e)}")
        return self.data
        
    def print_rows(self, n):
        print(self.data.head(n))