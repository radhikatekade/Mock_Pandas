# Keep orders from the year 2019 only. Get the count of the orders based on the buyer_id. Drop the
# duplicate rows. Left join the users df with orders df, fill Null values with 0, return the df with
# desired columns and column names.

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[orders['order_date'].dt.to_period("Y") == '2019']
    orders['count'] = orders.groupby('buyer_id')['buyer_id'].transform('count')
    orders = orders[['buyer_id', 'count']].drop_duplicates(subset=['buyer_id'])
    df = users.merge(orders, left_on='user_id', right_on='buyer_id', how='left').fillna(0)
    return (df[['user_id', 'join_date', 'count']]
            .rename(columns={'user_id': 'buyer_id', 'count': 'orders_in_2019'}))