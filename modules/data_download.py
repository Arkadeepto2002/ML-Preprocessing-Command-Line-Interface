import pandas as pd
class DatasetDownloader:
    def __init__(self, df, filename):
        self.df = df
        self.filename = filename

    def download_dataset(self):
        try:
    
            if not self.filename.endswith('.csv'):
              self.filename = self.filename + '.csv'
    
            self.df.to_csv(self.filename, index=False)
            print(f'{self.filename} downloaded successfully.')
        except Exception as e:
            print(f'Error downloading dataset: {str(e)}')
