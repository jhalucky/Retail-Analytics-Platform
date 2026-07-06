from src.config.spark_session import get_spark_session
from src.extract.read_csv import read_csv
from src.extract.explore_df import print_schema

spark = get_spark_session()
customer_df = read_csv(spark, "data/raw/customers.csv")
# print_schema(customer_df)
# print(f"spark version : {spark.version}")
print(customer_df.columns)

spark.stop()