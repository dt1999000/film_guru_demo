from sqlmodel import Session, create_engine, SQLModel
from models import User, Movie
from schemas import User, UserBase, UserCreate, Movie, MovieBase, MovieList

genre_mapping = {
    "Action": 28,
    "Adventure": 12,
    "Animation": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Science Fiction": 878,
    "TV Movie": 10770,
    "Thriller": 53,
    "War": 10752,
    "Western": 37
}

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def populate_db(session: Session = Depends(get_session)):
    with open("TMDB_movie_dataset_v11.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            genre_id = genre_mapping[row['genres']]
            genre_name = row['genres']
            genre = session.exec(select(Genre).where(Genre.id == genre_id)).first()
            if not genre:
                genre = Genre(name=genre_name, id=genre_id)
                session.add(genre)
                session.commit()
                session.refresh(genre)

            production_company_name = row['production_company']
            