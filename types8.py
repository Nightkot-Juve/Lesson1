product = {
    "city": "Москва", 
    "temperature": 20
    }
print(product["city"])
print(product["temperature"] - 5)
print(product)
print(product.get("country"))
print(product.get("country", "Россия"))
product["date"] = "27.05.2019"
print(len(product))