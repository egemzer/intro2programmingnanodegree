import webbrowser


class Movie():
     """Creates movie objects

        Attributes for __init__:
        title (str): title of the movie.
        storyline (str): brief description of the movie
        poster_image_url(str): URL to the poster image from Wikimedia
        trailer_youtube_url(str): URL to the YouTube movie trailer
        rating(str): rating of the movie, ie "PG"
        year(str): year the movie was released"""

     VALID_RATINGS = ["G","PG", "PG-13", "R"]

     def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating, year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.year = year

     # opens a web browser and auto-plays the trailer for the movie
     def show_trailer(self):      
        webbrowser.open(self.trailer_youtube_url)
