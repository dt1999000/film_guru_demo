from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from .database import get_session, init_db
from .models import User, UserCreate, Movie, MovieCreate
app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/users/", response_model=User)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/movies/", response_model=Movie)
def create_movie(movie: MovieCreate, session: Session = Depends(get_session)):
    db_movie = Movie.from_orm(movie)
    session.add(db_movie)
    session.commit()
    session.refresh(db_movie)
    return db_movie

@app.get("/movies/", response_model=List[Movie])
def read_movies(session: Session = Depends(get_session)):
    movies = session.exec(select(Movie)).all()
    return movies
