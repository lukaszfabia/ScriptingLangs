class DataModel:
    def __init__(self, data):
        self.data = data # json type
        self.main: str = None
        self.description: str = None
        self.temp: float = None
        self.feels_like: float = None
        self.pressure: int = None
        self.city_name: str = None
        self.country: str = None

    def get_data(self):
        return self.data

    def preprocess_json(self):
        weather_list = self.data['weather']
        weather_data = weather_list[0]
        self.main = weather_data['main'] 
        self.description = weather_data['description']
        params_data = self.data['main']
        self.temp = float(params_data['temp'])
        self.feels_like = float(params_data['feels_like'])
        self.pressure = int(params_data['pressure'])

        self.city_name = self.data['name']

        sys_list = self.data['sys']
        self.country = sys_list['country']

