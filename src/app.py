import streamlit as st
from services.tmdb_service import fetch_data

def main():
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

if __name__ == "__main__":
    main()