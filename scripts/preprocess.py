import pandas as pd


class Preproccessing:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def show_datatypes(self) -> pd.DataFrame:
        return self.df.dtypes

    def get_null_percentage_of_dataframe(self) -> pd.DataFrame:
        return (
            self.df.isnull().sum().sort_values(ascending=False) / self.df.shape[0] * 100
        )

    def convert_to_GB(self, col: list) -> pd.DataFrame:
        for i in col:
            self.df[i] = self.df[i] / 1000000000
            self.df.rename(columns={i: i.replace("Bytes", "GB")}, inplace=True)
        return self.df

    def convert_to_Minutes(self) -> pd.DataFrame:
        dur = "Dur. (ms)"
        self.df[dur] = self.df[dur] / 60000
        self.df.rename(columns={dur: "Dur. (Min)"}, inplace=True)
        return self.df

    def get_aggrigate_sum(self, col: list) -> pd.DataFrame:
        newconcat = pd.DataFrame(columns=col)
        for item in col:
            agg = (
                self.df.groupby(["MSISDN/Number"])[item]
                .agg([(item, "sum")])
                .reset_index()
            )
            newconcat[item] = agg[item]
        return newconcat

    def get_aggrigate_count(self, element: str):
        agg = (
            self.df.groupby(["MSISDN/Number"])[element]
            .agg([(element, "count")])
            .reset_index()
        )
        return agg
