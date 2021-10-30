import streamlit as st
import requests
import json
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
d = st.date_input("Travel day", datetime.datetime(2021, 10, 31, 8, 45, 30))
t = st.time_input('Pickup time', datetime.datetime(2021, 10, 31, 8, 45, 30))
dt = f'{d} {t}'
q2 = st.text_input('pickup longitude')
q3 = st.text_input('pickup latitude')
q4 = st.text_input('dropoff longitude')
q5 = st.text_input('dropoff latitude')
q6 = st.text_input('passenger count')
params = {
    'pickup_datetime': dt,
    'pickup_longitude': q2,
    'pickup_latitude': q3,
    'dropoff_longitude': q4,
    'dropoff_latitude': q5,
    'passenger_count': q6
}

st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''


'''
2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...


## Finally, we can display the prediction to the user
'''
url = 'https://taxifare.lewagon.ai/predict'

r = requests.get(url, params=params)
st.write(r.json()['prediction'])

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown(
#         'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
#     )
