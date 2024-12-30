import streamlit as st
from services.tmdb_service import fetch_data, search_movies

API_URL = "https://127.0.0.1:8000"

def create_user(username, email, password):
    response = requests.post(f"{API_URL}/users/", json={"username": username, "email": email, "password": password})
    return response.json()

def get_user(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}")
    return response.json()

def create_movie(title, overview, release_date, vote_average, owner_id):
    response = requests.post(f"{API_URL}/movies/", json={"title": title, "overview": overview, "release_date": release_date, "vote_average": vote_average, "owner_id": owner_id})
    return response.json()

def get_movies():
    response = requests.get(f"{API_URL}/movies/")
    return response.json()
    
def get_recommendations(username):
    user = st.session_state['users'][username]
    genre = user['favorite_genre']
    recommendations = search_movies(query=genre)
    user['recommendations'] = recommendations['results']


if __name__ == "__main__":
    st.title("Movie Recommendation App")
    
    st.sidebar.header("User Preferences")
    language = st.sidebar.selectbox("Select Language", ["en-US", "fr-FR", "es-ES"])
    region = st.sidebar.selectbox("Select Region", ["US", "FR", "ES"])
    search_query = st.sidebar.text_input("Search for a movie")

    if st.sidebar.button("Get Recommendations"):
        if search_query:
            results = fetch_data("/search/movie", api_key, {"query": search_query, "language": language, "region": region})
            st.write("Search Results:")
            for movie in results.get("results", []):
                st.write(f"{movie['title']} ({movie['release_date']})")
        else:
            st.warning("Please enter a movie title to search.")