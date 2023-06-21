import geocoder
import datetime
import pandas as pd
import os


time1 = datetime.datetime.now().strftime('%d-%m-%Y')

def loc():
    g = geocoder.ip('me')
    return g.latlng

def record():
    try:
        time2 = datetime.datetime.now().strftime(' %H-%M-%S')
        l = loc()
        lat, long = l[0], l[1]
        place_name = ''

        # Perform reverse geocoding to get the place name
        g = geocoder.reverse((lat, long))
        if g.ok:
            place_name = g.address.split(',')[0]  # Extract the name of the place

        # Create a dictionary with the location details
        location_data = {
            'Date': time1,
            'Time': time2,
            'Latitude': lat,
            'Longitude': long,
            'Place Name': place_name
        }

        # Create or append to the spreadsheet
        df = pd.DataFrame([location_data])
        df.to_csv('location_data.csv', mode='a', header=not os.path.exists('location_data.csv'), index=False)

        return place_name

    except:
        return ''