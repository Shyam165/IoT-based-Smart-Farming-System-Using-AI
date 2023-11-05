import streamlit as st
import numpy as np
import pandas as pd
import joblib

#import streamlit as st
from PIL import Image
import io
#import numpy as np
import tensorflow as tf
from utils import clean_image, get_prediction, make_results


# Add a menu or button to switch between different pages
selected_page = st.sidebar.radio("Select a Page", ["Crop Prediction", "Plant Disease Prediction"])

if selected_page == "Crop Prediction":

    model_files = {
        "Ensemble": "./models/Ensemble.pkl",
        "KNNClassifier": "./models/KNNClassifier.pkl",
        "NBClassifier": "./models/NBClassifier.pkl",
        "RandomForest": "./models/RandomForest.pkl",
        "SVMClassifier": "./models/SVMClassifier.pkl"
    }

    # Sidebar with model selection
    st.sidebar.title("Select Model")
    selected_model = st.sidebar.selectbox("Choose a model for prediction", list(model_files.keys()))

    # Load the selected model
    model_file = model_files[selected_model]
    model = joblib.load(model_file)

    # Main content
    st.title("Crop Prediction Using Machine Learning")

    st.write("This application allows you to predict the most suitable crop based on input parameters using different models.")

    # Input parameters
    st.header("Input Parameters")
    param1 = st.number_input("Nitrogen", value=0.0)
    param2 = st.number_input("Phosphorus", value=0.0)
    param3 = st.number_input("Potassium", value=0.0)
    param4 = st.number_input("Temperature", value=0.0)
    param5 = st.number_input("Humidity", value=0.0)
    param6 = st.number_input("PH", value=0.0)
    param7 = st.number_input("Rainfall(in mm)", value=0.0)

    # Create a list of input parameters for prediction
    input_data = np.array([[param1, param2, param3, param4, param5, param6, param7]])

    # Prediction
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.subheader("Prediction")
        st.write(f"The predicted crop using '{selected_model}' is: {prediction[0]}")

    # Add a disclaimer
    st.sidebar.subheader("About CPA")
    st.sidebar.write('''Welcome to the Crop Prediction App! This tool leverages machine learning models to help you predict the most suitable crop based on seven essential agricultural parameters. Whether you're a farmer planning your next planting season or an enthusiast interested in crop predictions, this app has you covered. Simply input the parameters, select a model, and get accurate crop recommendations for your specific conditions. Explore the power of data-driven agriculture with ease!.''')


elif selected_page == "Plant Disease Prediction":
    # Loading the Model and saving to cache
    @st.cache(allow_output_mutation=True)
    def load_model(path):
        
        # Xception Model
        xception_model = tf.keras.models.Sequential([
        tf.keras.applications.xception.Xception(include_top=False, weights='imagenet', input_shape=(512, 512, 3)),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(4,activation='softmax')
        ])


        # DenseNet Model
        densenet_model = tf.keras.models.Sequential([
            tf.keras.applications.densenet.DenseNet121(include_top=False, weights='imagenet',input_shape=(512, 512, 3)),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(4,activation='softmax')
        ])

        # Ensembling the Models
        inputs = tf.keras.Input(shape=(512, 512, 3))

        xception_output = xception_model(inputs)
        densenet_output = densenet_model(inputs)

        outputs = tf.keras.layers.average([densenet_output, xception_output])


        model = tf.keras.Model(inputs=inputs, outputs=outputs)

        # Loading the Weights of Model
        model.load_weights(path)
        
        return model


    # Removing Menu
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Loading the Model
    model = load_model('model.h5')

    # Title and Description
    st.title('Plant Diesease Detection')
    st.write("Just Upload your Plant's Leaf Image and get predictions if the plant is healthy or not")

    # Setting the files that can be uploaded
    uploaded_file = st.file_uploader("Choose a Image file", type=["png", "jpg"])

    # If there is a uploaded file, start making prediction
    if uploaded_file != None:
        
        # Display progress and text
        progress = st.text("Crunching Image")
        my_bar = st.progress(0)
        i = 0
        
        # Reading the uploaded image
        image = Image.open(io.BytesIO(uploaded_file.read()))
        st.image(np.array(Image.fromarray(
            np.array(image)).resize((700, 400), Image.ANTIALIAS)), width=None)
        my_bar.progress(i + 40)
        
        # Cleaning the image
        image = clean_image(image)
        
        # Making the predictions
        predictions, predictions_arr = get_prediction(model, image)
        my_bar.progress(i + 30)
        
        # Making the results
        result = make_results(predictions, predictions_arr)
        
        # Removing progress bar and text after prediction done
        my_bar.progress(i + 30)
        progress.empty()
        i = 0
        my_bar.empty()
        
        # Show the results
        st.write(f"The plant {result['status']} with {result['prediction']} prediction.")

        
        
