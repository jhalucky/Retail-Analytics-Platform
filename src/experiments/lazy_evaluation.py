from src.config.spark_session import get_spark_session
from src.extract.read_csv import read_csv

def lazy_evaluation_demo(df):

    spark = get_spark_session()

    

    # transformation

    filtered_df = df.filter(
        df.state == "Delaware"
    )

    print("\nFilter Transformation created.")

    # Action 1

    print("----SHOW----\n")
    filtered_df.show(5)

    # Action 2

    print("----Count----")
    print(f"Rows from Delaware: {filtered_df.count()}")

    # Action 3

    print("\nFIRST ROW")
    print(filtered_df.first())


    # Action 4

    print("\n----Collect----")
    rows = filtered_df.collect()
    print(f"Collected {len(rows)} rows.")

    print(rows[:5])

    spark.stop()


if __name__ == "__main__":
    lazy_evaluation_demo()




