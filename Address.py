import os.path
from geotext import GeoText
import pandas as pd
import csv

if __name__ == "__main__":

    data = pd.read_csv('Data/payments-4.csv')
    data.drop(['status', 'app_id', 'app_name', 'target_type', 'actor_is_group',
                    'action', 'mentions_count', 'likes_count'], axis=1, inplace=True)

    notes = data['note'].dropna()
    df1 = pd.DataFrame()
    for note in notes:
        places = GeoText(note)
        if len(places.cities) > 0:
            df1 = df1.append({'note': note, 'city/state': places.cities}, ignore_index=True)

    complete = df1.merge(data, on='note', how='inner').drop_duplicates(subset='payment_id', keep="first")
    print(complete)
    complete.to_csv("Data/locations-4.csv", index=False)


