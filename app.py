import requests
import json
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

if __name__ == "__main__":
    endpoint = "/movie/now_playing"
    response = fetch_data(endpoint, api_key)
    print('now in cinema' + json.dumps(response, indent=2))

    endpoint = "/movie/popular"
    response = fetch_data(endpoint, api_key)
    print('popular' + json.dumps(response, indent=2))

    endpoint = "/movie/top_rated"
    response = fetch_data(endpoint, api_key)
    print('top rated' + json.dumps(response, indent=2))

    endpoint = "/movie/upcoming"
    response = fetch_data(endpoint, api_key)
    print('upcoming' + json.dumps(response, indent=2))

