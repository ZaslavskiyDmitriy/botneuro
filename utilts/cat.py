import requests

def cat():
    url = 'https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['url']
    else:
        print("Failed to fetch data from API:", response.status_code)
        return None

if __name__ == '__main__':
    print(cat())