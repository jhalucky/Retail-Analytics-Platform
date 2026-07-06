import csv
import random
from faker import Faker

fake = Faker()


def generate_order_items(num_order_items, output_file):

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)
        writer.writerow([
            "order_item_id",
            "order_id",
            "product_id",
            "quantity",
            "unit_price"
        ])


        for order_item_id in range(1,num_order_items+1):

            writer.writerow([
                order_item_id,
                random.randint(1,1000),
                random.randint(1,1000),
                random.randint(50,500),
                random.randint(1000,100000)
            ])
    
    print(f"{num_order_items} generated and written successfully.")






if __name__ == "__main__":
    generate_order_items(num_order_items=1000, output_file="data/raw/order_items.csv")

    