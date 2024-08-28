import requests
import streamlit

api_key = "6b155a67ac085d817e85a626eebbbe40"
def get_data(place, forcast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    request = requests.get(url)
    content = request.json()
    filtered_data = content['list']
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]


    return filtered_data


if __name__ == "__main__":
    print(get_data(place="tokyo", forcast_days=3))