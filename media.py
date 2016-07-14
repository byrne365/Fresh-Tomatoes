import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    #Movie ratings

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    #list of attributes

    def __init__ (self, movie_title, movie_VALID_RATINGS, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.VALID_RATINGS = movie_VALID_RATINGS
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Function to run the movie trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    
