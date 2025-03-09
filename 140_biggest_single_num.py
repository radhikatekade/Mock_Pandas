# Create count of values, drop duplicate rows, sort them in descending order, keep only rows with count == 1
# If len(df) == 0, return the empty df, else return the first row of the df.
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers['count'] = my_numbers.groupby('num')['num'].transform('count')
    df = my_numbers.drop_duplicates(subset=['num'])
    df = df.sort_values(by=['num'], ascending=False)
    df = df[df['count'] == 1]
    if len(df) == 0:
        return pd.DataFrame([None], columns= ['num'])
    return df[['num']].head(1)