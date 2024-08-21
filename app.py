import streamlit as st
import pickle


def recommend(movie):

    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies


movies_df = pickle.load(open('./movies.pkl', 'rb'))
similarity = pickle.load(open('./similarity.pkl', 'rb'))

movie_titles = movies_df['title'].values

st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Please select a movie', movie_titles)
if selected_movie_name == 'Avengers: Age of Ultron':
    posters = ['https://m.media-amazon.com/images/I/81iPfppO1+L.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5Yqr_HlaDuwiMJ9w3JW-7_abshwYey5ehqw&s', 'https://rukminim2.flixcart.com/image/850/1000/xif0q/poster/0/d/d/small-spos8825-poster-iron-man-1-a-official-sticker-sl-9829-wall-original-imaghs5pygznwxu9.jpeg?q=20&crop=false', 'https://image.tmdb.org/t/p/original/prSfAi1xGrhLQNxVSUFh61xQ4Qy.jpg', 'https://c8.alamy.com/comp/FXEAGB/avengers-assemble-2012-directed-by-joss-whedon-and-starring-robert-FXEAGB.jpg']
elif selected_movie_name == 'Jurassic World':
    posters = ['https://m.media-amazon.com/images/I/91skr-8i52L._AC_UF1000,1000_QL80_.jpg', 'https://image.tmdb.org/t/p/original/jElpCJkSaRPYwIMwZY28gOKV7BK.jpg', 'https://www.postergully.com/cdn/shop/products/PP33258.jpg?v=1578633691', 'https://www.dneg.com/wp-content/uploads/2018/02/Terminator-Genisys-US-Poster-702x1024.jpeg', 'https://i.etsystatic.com/12729518/r/il/a29c54/1989049257/il_570xN.1989049257_4llk.jpg'];

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    # for i in names:
    #     st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(names[0])
        st.image(posters[0])
    with col2:
        st.write(names[1])
        st.image(posters[1])

    with col3:
        st.write(names[2])
        st.image(posters[2])

    with col4:
        st.write(names[3])
        st.image(posters[3])

    with col5:
        st.write(names[4])
        st.image(posters[4])
