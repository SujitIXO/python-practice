import requests

def randombook_api_handle():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    res = requests.get(url)
    data = res.json()

    if data["success"] and "data" in data:
        random_book = data["data"]
        author = random_book["volumeInfo"]["authors"][0]
        title = random_book["volumeInfo"]["title"]
        desc = random_book["volumeInfo"]["description"]
        country = random_book["saleInfo"]["country"]

        return author, title, desc, country
    
    else:
        raise Exception("Failed to fetch the data")

def main():
    try:
        author, title, desc, country = randombook_api_handle()
        print(f"Author: {author} \nTitle: {title} \nDescription: {desc} \nCountry:{country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()