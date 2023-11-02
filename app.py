import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    

def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse = True, key = lambda x:x[1])
    recommended_movies_names = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_names.append(movies.iloc[i[0]].title)
    return recommended_movies_names, recommended_movies_poster

st.header("Movies Recommender System")

movies = pickle.load(open('files/movies_list.pickle','rb'))
similarity = pickle.load(open('files/similarity.pickle','rb'))

movies_list = movies['title'].values

selected_movie = st.selectbox(
    'Type or select a movie to get the recommendations',
    movies_list
)

if st.button('Show Recommendations'):
    recommended_movies_name,recommended_movies_poster = recommend(selected_movie)