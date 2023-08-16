import requests
import json

baseURL = "https://fakestoreapi.com"
if __name__ == "__main__":
    response = requests.get(f"{baseURL}/products")
    data = response.json()
    total_price = 0
    for i in data:
        # print(i['title'])
        total_price += i['price']
    print(f"total - {total_price}")

    new_product =  {
                    'title': 'test product',
                    'price': 13.5,
                    'description': 'lorem ipsum set',
                    'image': 'https://i.pravatar.cc',
                    'category': 'electronic'
                }

    resp = requests.post(f"{baseURL}/products", data=new_product)

    product_id = 5
    resp = requests.delete(f'{baseURL}/products/{product_id}')

    print(resp.text)
