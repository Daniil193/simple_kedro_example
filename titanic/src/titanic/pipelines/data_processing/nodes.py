import pandas as pd

def cat_to_num(arr):
    """
    Convert categorical value to numeric
    
    :param arr: array of string values
    :type arr: numpy array
    :return: dict of {srt: int} values
    :rtype: dict
    """
    return {i:c for c, i in enumerate(arr)}
    


def preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Label encoding for two columns "Sex" and "Embarked"
    
    :param df: dataframe with ["Sex", "Embarked"] columns
    :type df: pandas DataFrame
    :return: dataframe with prepared columns
    :rtype: pandas DataFrame
    """
    df = df.dropna(subset=["Embarked"])
    
    d_sex = cat_to_num(df["Sex"].unique())
    d_embarked = cat_to_num(df["Embarked"].unique()) 
    
    df["Sex"] = df["Sex"].map(d_sex)
    df["Embarked"]= df["Embarked"].map(d_embarked)
    
    return df