from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class UserBase(SQLModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    favorite_movies: List["Movie"] = Relationship(back_populates="owner")
    rated_movies: List["RatedMovies"] = Relationship(back_populates="owner")

class MovieBase(SQLModel):
    title: str
    overview: Optional[str] = None
    release_date: str
    vote_average: float

class Movie(MovieBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    production_companies: Optional["ProductionCompany"] = Relationship(back_populates="movie_list")
    genre_id: List[int] = Field(default=None, foreign_key="genres.id")
    genre: List["Genre"] = Relationship(back_populates="movie_list")
    owner_id: Optional[int] = Field(default=None, foreign_key="users.id")
    owner: Optional[User] = Relationship(back_populates="movies")

class ProductionCompanyBase(SQLModel):
    name: str

class ProductionCompany(ProductionCompanyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movie_list: List["Movie"] = Relationship(back_populates="production_company")

class GenreBase(SQLModel):
    name: str

class Genre(GenreBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movie_list: List["Movie"] = Relationship(back_populates="genre")

class MovieGenreLink(SQLModel, table=True):
    movie_id: Optional[int] = Field(default=None, foreign_key="movies.id", primary_key=True)
    genre_id: Optional[int] = Field(default=None, foreign_key="genres.id", primary_key=True)

class MovieProductionCompanyLink(SQLModel, table=True):
    movie_id: Optional[int] = Field(default=None, foreign_key="movies.id", primary_key=True)
    production_company_id: Optional[int] = Field(default=None, foreign_key="production_companies.id", primary_key=True)
    
class RatedMovies(Movie, table=True):
    user_rating: float

class MovieList(SQLModel):
    movies: List[Movie]
