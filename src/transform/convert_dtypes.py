from pyspark.sql.functions import col

def convert_dtypes(df, schema):
        

    for column, dtype in schema.items():

            df = df.withColumn(
                  column, 
                  col(column).cast(dtype)
            )

    return df