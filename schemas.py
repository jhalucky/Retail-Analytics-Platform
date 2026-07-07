CUSTOMER_SCHEMA = {
    "customer_id": "integer",
    "first_name" : "string",
    "last_name" : "string",
    "gender" : "string",
    "email" : "string",
    "phone" : "bigint",
    "address" : "string",
    "city" : "string",
    "state" : "string",
    "signup_date" : "date"
}

PRODUCT_SCHEMA = {
    "product_id": "integer",
    "price": "double",
    "stock_quantity": "integer"
}

ORDER_SCHEMA = {
    "order_id": "integer",
    "customer_id": "integer",
    "total_amount": "double",
    "order_date": "date"
}

ORDER_ITEM_SCHEMA = {
   "order_item_id" : "integer",
   "order_id" : "integer",
   "product_id" : "integer",
   "quantity" : "integer",
   "unit_price" : "double"

}

PAYMENT_SCHEMA = { 
    "payment_id" : "integer",
    "order_id" : "integer",
    "payment_method": "string",
    "payment_status" : "string",
    "payment_date" : "date"

}
