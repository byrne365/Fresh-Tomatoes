# Fresh-Tomatoes

## What is the purpose of Fresh Tomatoes?
Fresh Tomatoes is a Website which displays a list of some of my favourite movies, including poster image,
movie rating and youtube trailer.
Fresh Tomtoes referances three files, `fresh_tomatoes.py`, `media.py`, and `entertainment_centre.py`.

# Installation

As this is a basic html website, Installation is simple. All that is required is to have a *web browser* installed and *python 2.7*, should you wish to modify any of the above three files.

Install files of chrome and python are listed below.

`https://www.google.com/chrome/browser/desktop/index.html`

`https://www.python.org/`

# How does Fresh Tomatoes function?

In the file named `media.py` I created a class called `Movie`, within this class there is an function called `_init_`. When the `init` function gets called, it creates an instance, `self` is the instance being created (the movie), and calls the argument and its variables. for example the `movie_title`, `VALID RATING`,etc. which can be found within the `entertainment_center.py` file. When each instance is called it sets aside space for each instance and within this space each instance has its own set of variables, known as instence variables.
```
def __init__ (self, movie_title, movie_VALID_RATINGS, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.VALID_RATINGS = movie_VALID_RATINGS
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
```

## to view fresh_tomatoes.html
Simply open the `fresh_tomatoes.html` file in any browser, you will be presented with a web page which will display six of my current favourite movies.
The information presnted consists of the poster image, the title of the movie, the rating of the movie and a short detailed synopsys of the movie.

## How to view the trailer
The trailer for each movie can be easily viewed.To do this simply `click` on the *poster image* of the movie you wish to view.
A seperate movie trailer screen will then appear. You can adjust the `volume`, and `quality` of the trailer.
Should you wish to exit, simply press the close **`X`** in the top left hand courner of the movie trailer screen.

## Can I  make changes to the movies?
This is possible, by making changes to the `entertainment_center.py` file.
This file contains all the individual information about each movie which is displayed in the `fresh_tomatoes.html` file.
Changes can be made to each instance like the _**rating**_, _**synopsys**_, _**movie trailer**_, and the _**poster image**_.
The file called `media.py` should not be changed as this is the `parent` file.








