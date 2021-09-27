import pandas as pd

def cat_to_num(arr):
    return {i:c for c, i in enumerate(arr)}
    


def preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.dropna(subset=["Embarked"])
    
    d_sex = cat_to_num(df["Sex"].unique())
    d_embarked = cat_to_num(df["Embarked"].unique()) 
    
    df["Sex"] = df["Sex"].map(d_sex)
    df["Embarked"]= df["Embarked"].map(d_embarked)
    
    return df