import csv
from faker import Faker

fake = Faker()

def generate_customer(num_customers, output_file):

    """ Generate synthetic data using faker module and save it to csv file."""

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "customer_id",
            "first_name",
            "last_name",
            "gender",
            "email",
            "phone",
            "address",
            "city",
            "state",
            "signup_date"
        ])



        for customer_id in range(1, num_customers+1):
            writer.writerow([
                customer_id,
                fake.first_name(),
                fake.last_name(),
                fake.passport_gender(),
                fake.email(),
                fake.phone_number(),
                fake.address().replace("\n", ","),
                fake.city(),
                fake.state(),
                fake.date_between(start_date="-3y",end_date="today")
        ])

    print(f"{num_customers} generated and written successfully.")


if __name__ == "__main__":
   generate_customer(
       num_customers=1000,
       output_file="data/raw/customers.csv"
   )

