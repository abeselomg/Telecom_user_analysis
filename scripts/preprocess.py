import pandas as pd

class Preproccessing:
    
    def __init__(self, df:pd.DataFrame):
        self.df = df
        

    def get_null_percentage_of_dataframe(self)->pd.DataFrame:
        return self.df.isnull().sum().sort_values(ascending=False)/self.df.shape[0]*100
    
    def convert_to_GB(self,col:list)->pd.DataFrame:
        for i in col:
            self.df[i] = self.df[i] / 1 * 10e8
            self.df.rename(columns={i:i.replace("Bytes", "GB")}, inplace=True)
        return self.df
    
    def convert_to_Minutes(self)->pd.DataFrame:
        self.df["Dur. (ms)"] / 60000
        return self.df

if __name__ == "__main__":
    Preproccessing()
