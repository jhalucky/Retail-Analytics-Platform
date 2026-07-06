import csv
import random
from faker import Faker
from constants import random_brand, random_category, random_product_name

fake = Faker()

def generate_products(num_products, output_file):

     """ Generate synthetic data using faker module and save it to csv file."""

     with open(output_file, "w", newline="", encoding="utf-8") as file:
          
          writer = csv.writer(file)

          writer.writerow([
              "product_id",
              "product_name",
              "category",
              "brand",
              "price",
              "stock_quantity"
          ])

          for product_id in range(1, num_products+1):
               
               writer.writerow([
                    product_id,
                    random_product_name(),
                    random_category(),
                    random_brand(),
                    random.randint(100, 100000),
                    random.randint(0,500)
                    
                ])
               

          print(f"{num_products} generated and written successfully.")




if __name__ == "__main__":
     generate_products(num_products=1000, output_file="data/raw/products.csv")
