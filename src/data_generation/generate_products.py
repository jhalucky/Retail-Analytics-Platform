import csv
from faker import Faker

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
                    fake.,
                    fake.,
                    fake.brand_suffix(),
                    fake.pricetag(),
                    fake.random_number()
                ])
               

          print(f"{nums_products} generated and written successfully.")




if __name__ == "__main__":
     generate_products(nums_products=1000, output_file="data/raw/products.csv")
