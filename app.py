import streamlit as st
import pickle
import requests

def fetch_Poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4d67525303f3b9d96ae3ae5c35423367'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']

def recommend(movie):

    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies_df.iloc[i[0]].title)
        #fetch Poster from API
        recommended_movies_posters.append(fetch_Poster(movies_df.iloc[i[0]].movie_id)) 
    return recommended_movies, recommended_movies_posters


movies_df = pickle.load(open('./movies.pkl', 'rb'))
similarity = pickle.load(open('./similarity.pkl', 'rb'))

movie_titles = movies_df['title'].values

st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Please select a movie', movie_titles)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with col4:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with col5:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
