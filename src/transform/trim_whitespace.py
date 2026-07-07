from pyspark.sql.functions import trim, col

def trim_whitespace(df):

    for c in ["first_name", "last_name", "email"]:
        df =  df.withColumn(c, trim(col(c)))


    print("\nWhitespaces trimmed.")
    return df

