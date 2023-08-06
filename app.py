
import streamlit as st
import streamlit.components.v1 as components

import pickle

with open('genre_model.h5', 'rb') as genre_file:
    genre_model = pickle.load(genre_file)

with open('popularity_model.h5', 'rb') as model_file:
    model = pickle.load(model_file)
    
labels = [
    {'Genre': 'EDM', 'Label': 0},
    {'Genre': 'R&B', 'Label': 1},
    {'Genre': 'Acoustic Folk', 'Label': 2},
    {'Genre': 'Country', 'Label': 3},
    {'Genre': 'Hip Hop', 'Label': 4},
    {'Genre': 'Latin', 'Label': 5},
    {'Genre': 'Metal', 'Label': 6},
    {'Genre': 'Pop', 'Label': 7},
    {'Genre': 'Rock', 'Label': 8},
]
    
def predict_genre(danceability, energy, speechiness, acousticness, liveness, valence):
    """
    this method is for predicting genre
    takes all the Audio characteristics that we used for modelling and returns the prediction 
    """
    prediction = genre_model.predict([[danceability, energy, speechiness, acousticness, liveness, valence]])
    return prediction[0]

def predict_popularity(danceability, energy, speechiness, acousticness, liveness, valence):
    """
    this method is for predicting popularity
    takes all the Audio characteristics that we used for modelling and returns the prediction 
    """
    prediction = model.predict([[danceability, energy, speechiness, acousticness, liveness, valence]])
    return prediction[0]

def main():
    st.title("Data Analysis Project")
    
#     st.image("https://cdn2.downdetector.com/static/uploads/logo/Spotify_Logo_RGB_Green.png", width=700, use_column_width=False)
    st.image("https://cdn.dribbble.com/users/441326/screenshots/3165191/spotify-gif---oliver-keane.gif", 
             width=700, use_column_width=False)
     
    html_temp2 = """
        <div style="background-color:limegreen; padding:10px;border-radius:10px;">
        <h1 style="color:white;text-align:center;">Predict the Song's Popularity on Spotify</h1>
        </div>
        """
    # can use st.write()
    components.html(html_temp2)
    # components.html() will render the render the html component
        
    danceability = st.number_input("danceability", min_value=0.00, max_value=1.00, step=0.05)
    energy = st.number_input("energy", min_value=0.00, max_value=1.00, step=0.05)
    speechiness = st.number_input("speechiness", min_value=0.00, max_value=1.00, step=0.05)
    acousticness = st.number_input("acousticness", min_value=0.00, max_value=1.00, step=0.05)
    liveness = st.number_input("liveness", min_value=0.00, max_value=1.00, step=0.05)
    valence = st.number_input("valence", min_value=0.00, max_value=1.00, step=0.05)
    
    genre=""
    result=""
    if st.button("Predict"):
#         st.table(labels)
        genre = predict_genre(danceability, energy, speechiness, acousticness, liveness, valence)
        result = predict_popularity(danceability, energy, speechiness, acousticness, liveness, valence)
        
        for item in labels:
            if item['Label'] == genre:
                genre = item['Genre']
                break
            else:
                print('Label not found')

        st.success("The song's genre is {}".format(genre))
        st.success('The Popularity of the song is {}'.format(result))

if __name__=='__main__':
    main()
