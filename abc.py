import requests

def get_barcode_from_name(product_name):
    url = "https://api.upcitemdb.com/prod/trial/search"
    params = {"s": product_name}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data['code'] == 'OK' and data['total'] > 0:
        item = data['items'][0]
        return item['title'], item['upc']
    else:
        return None, None

# Example
product = input("enter product")
title, barcode = get_barcode_from_name(product)

if barcode:
    print(f"Product: {title}\nBarcode: {barcode}")
else:
    print("Barcode not found.")
