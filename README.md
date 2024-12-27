# Movie Recommendation App

This is a movie recommendation application built using Streamlit and The Movie Database (TMDB) API. The application allows users to explore and receive recommendations for movies based on their preferences.

## Project Structure

```
movie-recommendation-app
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── components
│   │   └── __init__.py       # Initializes the components package
│   ├── services
│   │   └── tmdb_service.py    # Interacts with TMDB API for movie data
│   └── utils
│       └── __init__.py       # Initializes the utils package
├── requirements.txt           # Lists project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd movie-recommendation-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set the TMDB API key as an environment variable:
   ```
   export TMDB_API_KEY=<your_api_key>  # On Windows use `set TMDB_API_KEY=<your_api_key>`
   ```

## Usage

To run the application, execute the following command:
```
streamlit run src/app.py
```

Open your web browser and navigate to `http://localhost:8501` to view the application.

## Features

- Browse popular movies
- View currently playing movies
- Search for movies by title
- Get recommendations based on user preferences

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.