import requests
import os

api_key = os.getenv("TMDB_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the TMDB_API_KEY environment variable.")

api_params_templates = {
    "/movie/now_playing": ["language", "region", "page"],
    "/movie/popular": ["language", "region", "page"],
    "/movie/top_rated": ["language", "region", "page"],
    "/movie/upcoming": ["language", "region", "page"],
    "/search/movie": ["query", "language", "page", "include_adult", "region", "year"]
}

def filter_params(endpoint, provided_params):
    valid_keys = api_params_templates.get(endpoint, [])
    return {key: value for key, value in provided_params.items() if key in valid_keys}

def fetch_data(endpoint, api_key, optional_params=None):
    base_url = "https://api.themoviedb.org/3"
    params = {"api_key": api_key}
    
    # Add optional parameters if provided
    if optional_params:
        filtered_params = filter_params(endpoint, optional_params)
        params.update(filtered_params)
    
    try:
        response = requests.get(f"{base_url}{endpoint}", params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")
        
def fetch_now_playing(language='en-US', region=DE, page=1):
    endpoint = "/movie/now_playing"
    params = {
        "language": language,
        "region": region,
        "page": page
    }
    return fetch_data(endpoint, api_key, params)

def fetch_popular_movies(language='en-US', region=DE, page=1):
    endpoint = "/movie/popular"
    params = {
        "language": language,
        "region": region,
        "page": page
    }
    return fetch_data(endpoint, api_key, params)

def fetch_top_rated_movies(language='en-US', region=DE, page=1):
    endpoint = "/movie/top_rated"
    params = {
        "language": language,
        "region": region,
        "page": page
    }
    return fetch_data(endpoint, api_key, params)

def fetch_upcoming_movies(language='en-US', region=DE, page=1):
    endpoint = "/movie/upcoming"
    params = {
        "language": language,
        "region": region,
        "page": page
    }
    return fetch_data(endpoint, api_key, params)

def search_movies(query, language='en-US', page=1, include_adult=False, region=DE, year=None):
    endpoint = "/search/movie"
    params = {
        "query": query,
        "language": language,
        "page": page,
        "include_adult": include_adult,
        "region": region,
        "year": year
    }
    return fetch_data(endpoint, api_key, params)
