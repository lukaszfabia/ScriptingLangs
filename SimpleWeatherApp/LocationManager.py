from geopy.geocoders import Nominatim

def get_location(city: str) -> tuple[str, str]:
    geolocator = Nominatim(user_agent='location_manager')
    location = geolocator.geocode(city)
    return location.latitude, location.longitude
    
if __name__ == '__main__':
    print(get_location("New York"))