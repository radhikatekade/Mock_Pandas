# Create two columns with min_date and max_date for all product IDs to compute the time period in which 
# a product was sold. Find out the product sold only in first quarter of 2019. Merge the sales and 
# product table to get product ID with product name and finally drop duplicate product IDs.

import pandas as pd
def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # sales.drop_duplicates(subset=['seller_id', 'product_id'], inplace=True) # does not work
    sales['min_date'] = sales.groupby('product_id')['sale_date'].transform('min')
    sales['max_date'] = sales.groupby('product_id')['sale_date'].transform('max')
    sales = sales[(sales['min_date'] >= '2019-01-01') & (sales['min_date'] <= '2019-03-31') \
        & (sales['max_date'] >= '2019-01-01') & (sales['max_date'] <= '2019-03-31')]
    df = sales.merge(product, left_on='product_id', right_on='product_id', how='inner')
    df.drop_duplicates(subset=['product_id'], inplace=True) # drop duplicates should happen at the end
    return df[['product_id', 'product_name']]


# Approach II - Fewer lines
# def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
#     df = sales.groupby(['product_id'], as_index = False
#              ).agg(min=('sale_date', 'min'), max=('sale_date', 'max'))

#     return df[(df['min'] >='2019-01-01') &
#               (df['max'] <='2019-03-31')].merge(product).iloc[:,[0,3]]