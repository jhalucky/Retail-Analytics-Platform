import random

# ==========================
# Product Names
# ==========================

PRODUCT_NAMES = [
    "Laptop",
    "Wireless Mouse",
    "Mechanical Keyboard",
    "Gaming Keyboard",
    "Office Chair",
    "Monitor 24 Inch",
    "Monitor 27 Inch",
    "USB-C Hub",
    "Smartphone",
    "Tablet",
    "Bluetooth Speaker",
    "Smart Watch",
    "Power Bank",
    "External SSD",
    "Pendrive",
    "Webcam",
    "Printer",
    "Scanner",
    "Headphones",
    "Earbuds",
    "Microphone",
    "Backpack",
    "School Bag",
    "Notebook",
    "Pen",
    "Pencil",
    "Desk Lamp",
    "Study Table",
    "Water Bottle",
    "Coffee Mug",
    "Ceiling Fan",
    "Mixer Grinder",
    "Electric Kettle",
    "Air Fryer",
    "Vacuum Cleaner",
    "Running Shoes",
    "Sneakers",
    "T-Shirt",
    "Jeans",
    "Jacket",
    "Wallet",
    "Sunglasses",
    "Helmet",
    "Cricket Bat",
    "Football",
    "Basketball",
    "Yoga Mat",
    "Dumbbells",
    "Protein Shaker",
    "Tripod"
]

# ==========================
# Categories
# ==========================

CATEGORIES = [
    "Electronics",
    "Furniture",
    "Fashion",
    "Stationery",
    "Home",
    "Kitchen",
    "Sports",
    "Fitness",
    "Accessories"
]

# ==========================
# Brands
# ==========================

BRANDS = [
    "Dell",
    "HP",
    "Lenovo",
    "Asus",
    "Acer",
    "Apple",
    "Samsung",
    "Sony",
    "LG",
    "Boat",
    "Logitech",
    "Redragon",
    "Nike",
    "Adidas",
    "Puma",
    "Wildcraft",
    "Milton",
    "Classmate",
    "Cello",
    "Green Soul",
    "Philips",
    "Mi",
    "OnePlus",
    "Realme",
    "Noise"
]

# ==========================
# Order Status
# ==========================

ORDER_STATUS = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled",
    "Returned"
]

# ==========================
# Payment Methods
# ==========================

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery",
    "Wallet"
]

# ==========================
# Payment Status
# ==========================

PAYMENT_STATUS = [
    "Success",
    "Pending",
    "Failed",
    "Refunded"
]

# ==========================
# Product Helper Functions
# ==========================

def random_product_name():
    return random.choice(PRODUCT_NAMES)


def random_category():
    return random.choice(CATEGORIES)


def random_brand():
    return random.choice(BRANDS)


def random_order_status():
    return random.choice(ORDER_STATUS)

def random_payment_method():
    return random.choice(PAYMENT_METHODS)

def random_payment_status():
    return random.choice(PAYMENT_STATUS)