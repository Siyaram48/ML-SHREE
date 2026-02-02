import streamlit as st
import pickle
import pandas as pd


st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
div.stButton > button {
    background-color: green;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 200px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    "<h1 style='color:red;'>Movie Recommender</h1>",
    unsafe_allow_html=True
)


# Load data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

# Recommend function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)),
                        reverse=True,
                        key=lambda x: x[1])[1:6]

    names = []
    for i in movie_list:
        names.append(movies.iloc[i[0]].title)

    return names

# UI
selected_movie = st.selectbox(
    "Select Movie",
    movies['title'].values
)
 


if st.button("Recommend"):
    result = recommend(selected_movie)
    for movie in result:
        st.write(movie)
        
        
st.title("Good night")

        

        
