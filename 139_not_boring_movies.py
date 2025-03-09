# return the rows in df with odd IDs and description is NOT boring, return the df in descending order of
# ratings.
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return (cinema[(cinema['id']%2 != 0) & (cinema['description'] != "boring")]
            .sort_values(by=['rating'], ascending=False))