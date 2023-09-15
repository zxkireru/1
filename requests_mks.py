import requests

def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        timestamp = data['timestamp']
        
        print(f"МКС находится на широте {latitude} и долготе {longitude}.")
        print(f"Последнее обновление данных: {timestamp}.")
    else:
        print("Не удалось получить данные о положении МКС.")

get_iss_location()