import requests
import json
import streamlit as st

st.title("Predict the price of rental apartments in Hanoi")

st.sidebar.title("Features")

furniture_type_list = ['Unknown', 'full', 'cơ bản', 'full cao cấp', 'nguyên bản']
furniture_type_2id = {x: i for i, x in zip(range(5), furniture_type_list)}
furniture_type = st.sidebar.selectbox(label='Furniture type', options=furniture_type_list, index=1)
furniture_type = furniture_type_2id[furniture_type]

apartment_type_list = ['tập thể', 'thường', 'studio', 'mini', 'cao cấp']
apartment_type_2id = {x: i for i, x in zip(range(5), apartment_type_list)}
apartment_type = st.sidebar.selectbox(label='Apartment type', options=apartment_type_list, index=1)
apartment_type = apartment_type_2id[apartment_type]

poster = st.sidebar.selectbox(label='Poster', options=['môi giới', 'cá nhân'])
poster = 0 if poster == 'môi giới' else 1

no_bedroom = st.sidebar.slider(label='No bedroom', value=2, min_value=1, max_value=4, step=1)
area = st.sidebar.slider(label='Area (m2)', value=70, min_value=15, max_value=200, step=2)

latitude = st.sidebar.text_input(label='Latitude', value=21.0089749)
longitude = st.sidebar.text_input(label='Longitude', value=105.8345134)
latitude = float(latitude)
longitude = float(longitude)

is_predict = st.sidebar.button('Click here to predict')
if is_predict:
    predict_api = 'http://localhost:8004/predict'
    data = {'furniture_type': furniture_type,
            'apartment_type': apartment_type,
            'news_type': poster,
            'bedroom_number': no_bedroom,
            'area': area,
            'latitude': latitude,
            'longitude': longitude
            }
    print(data)

    response = requests.post(url=predict_api, data=json.dumps(data))
    content = json.loads(response.content)
    results = content['price']
    print(content)

    st.text("Price: {:.2f} M VND".format(results))
    st.image('../images/image_demo.jpeg')

