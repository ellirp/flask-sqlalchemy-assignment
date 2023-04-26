class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        session = self.Session()
        movies = session.query(movies).all()
        session.close()
        return movies

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        session = self.Session()
        movie = session.query(movie).filter_by(movie_id=movie_id).first()
        session.close()
        return movie

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        session = self.Session()
        movie = movie(title=title, director=director, rating=rating)
        session.add(movie)
        session.commit()
        session.close()
        return movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        session = self.Session()
        movies = session.query(movies).filter(movies.title.ilike(f'%{title}%')).all()
        session.close()
        return movies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
