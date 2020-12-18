from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import pandas as pd

if __name__ == "__main__":
    final = pd.read_csv('Data/out.csv')
    geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36")
    for city in final['city/state']:
        try:
            loc = geolocator.geocode(city, timeout=None)
            if loc is None:
                final.append({'longitude': None, 'latitude': None}, ignore_index=True)
            else:
                final.append({'longitude': loc.longitude, 'latitude': loc.latitude}, ignore_index=True)
        except GeocoderTimedOut as e:
            print("Error: geocode failed on input %s with message %s"%
            (city, e))

    final.to_csv("Data/final.csv", index=False)