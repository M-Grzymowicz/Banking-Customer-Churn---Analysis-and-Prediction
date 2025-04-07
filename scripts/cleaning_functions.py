
import pandas as pd

def clean_data(df):
    """Returns cleaned DataFrame.
    
    Processes:
        -removing irrelevant columns
        -transform data into less demanding formats
       
    Args: 
        df (pd.DataFrame) : uncleaned DataFrame
        
    Returns:
        df  (pd.DataFrame) : cleaned DataFrame
    
    """

    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)

    # removing unnecessary columns
    df = df.drop(['RowNumber', 'Surname', 'CustomerId'], axis=1)
    
    # convert 'object' to 'category' type
    category_columns = ['Geography']
    for column in category_columns:
        df[column] = df[column].astype('category')

    # convert 'object' to numerical columns
    df['Gender'] = df['Gender'].replace({'Male': 0, 'Female': 1})

    # convert numerical columns: data type optimization
    df['Gender'] = df['Gender'].astype('uint8')
    df['HasCrCard'] = df['HasCrCard'].astype('uint8')
    df['IsActiveMember'] = df['IsActiveMember'].astype('uint8')
    df['Age'] = df['Age'].astype('uint8')
    df['Tenure'] = df['Tenure'].astype('uint8')
    df['NumOfProducts'] = df['NumOfProducts'].astype('uint8')
    df['CreditScore'] = df['CreditScore'].astype('uint16')
        
    return df
