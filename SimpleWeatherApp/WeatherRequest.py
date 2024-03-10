import requests
from dotenv import load_dotenv
import os
from DataModel import DataModel
from LocationManager import get_location


def get_api_key():
    load_dotenv()
    return os.getenv('API')


class WeatherRequest:
    def __init__(self, coords: tuple[str, str]):
        self.lat = coords[0]
        self.log = coords[1]
        self.response = None

    def get_weather(self) -> str:
        """Get the weather of a given location

        Returns:
            str: Data about weather in JSON format
        """
        return f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.log}&appid={get_api_key()}&units=metric'
    
    def wrap_in_data_model(self) -> DataModel | None:
        self.response = requests.get(self.get_weather())
        if self.response.status_code != 200:
            return None
        data = DataModel(self.response.json())
        data.preprocess_json()
        return data

if __name__ == '__main__':
    loc = get_location('Wrocław')
    pogoda = WeatherRequest(loc)
    print(pogoda.wrap_in_data_model().temp)
