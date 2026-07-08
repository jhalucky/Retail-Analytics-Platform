from pyspark.sql.functions import avg

def average_order_value(df):

    return df.select(
        avg("sales_amount").alias("average_order_value")
    )

