from faker import Faker

fake = Faker()

def generate_customer():

    customer_id = 1
    first_name = ""
    last_name = ""
    gender = ""
    email= ""
    phone = ""
    address = ""
    city = ""
    state = ""
    signup_date = ""



    for i in range(1,101):
        customer_id = i
        first_name = fake.first_name()
        last_name = fake.last_name()
        gender = fake.passport_gender()
        email = fake.email()
        phone = fake.phone_number()
        address = fake.address()
        city = fake.city()
        state = fake.state()
        signup_date = fake.date()

        print(f"{i}. {first_name},{last_name},{gender},{email},{phone},{address},{city},{state},{signup_date}")



generate_customer()
