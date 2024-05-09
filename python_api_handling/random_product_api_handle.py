import requests

def fetch_random_product_data():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/30"
    res = requests.get(url)
    data = res.json()

    if data["success"] and "data" in data:
        product_data = data["data"]
        title = product_data["title"]
        desc = product_data["description"]
        price = product_data["price"]
        return title, price, desc
    else:
        raise Exception("Failed to fetch the data")

def main():
    try:
        title, desc, price = fetch_random_product_data()
        print(f"Title: {title} \nDescription: {desc} \nPrice: {price}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
