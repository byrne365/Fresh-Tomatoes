import fresh_tomatoes
import media

# First movie in list.

# Title of movie and the class it is refering to in the media.py file

batman_begins = media.Movie("Batman Begins",  # movie title
                            "PG-13",  # Rating
                            "When his parents are killed," + ' ' +  # storyline
                            "billionaire plqyboy Bruce Wayne" + ' ' +
                            "adopts the symbol of a bat to strike" + ' ' +
                            "fear into the hearts of the criminals in Gotham.",
                            "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",  # Poster image # NOQA
                            "https://www.youtube.com/tv#/watch?v=neY2xVmOfUM")  # trailer  # NOQA
# Second movie in list.

the_butterfly_effect = media.Movie("The Butterfly Effect",
                                   "PG-13",
                                   "Evan Treborn," + ' ' +
                                   "who blacks out frequently," + ' ' +
                                   "finds that when he reads" + ' ' +
                                   "from his adolescent journals.",
                                   "https://upload.wikimedia.org/wikipedia/en/4/43/Butterflyeffect_poster.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=B8_dgqfPXFg")  # NOQA
# Third movie in list.

xmen_days_of_future_past = media.Movie("Xmen:Days of future Past",
                                       "PG-13",
                                       "In the future," + ' ' +
                                       "robots known as Sentinels" + ' ' +
                                       "are exterminating mutants" + ' ' +
                                       "and their human allies." + ' ' +
                                       "Wolverine's consciousness is" + ' ' +
                                       "sent back fifty years to 1973," + ' ' +
                                       "to prevent the future.",
                                       "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg",  # NOQA
                                       "https://www.youtube.com/tv#/watch/video/control?v=pK2zYHWDZKo&resume")  # NOQA
# Fourth movie in list.

jungle_book = media.Movie("The Jungle Book",
                          "PG",
                          "Mowgli is a man cub raised by" + ' ' +
                          "the Indian wolf Raksha and her pack," + ' ' +
                          "in a jungle of Seoni, Bagheera trains" + ' ' +
                          "Mowgli to learn the ways of the wolves.",
                          "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",  # NOQA
                          "https://www.youtube.com/tv#/watch?v=HcgJRQWxKnw")  # NOQA
# Fifth movie in list.

the_martian = media.Movie("The Martian",
                          "PG-13",
                          "Astronaut Mark Watney is struck by debris" + ' ' +
                          "and lost in a storm on Mars." + ' ' +
                          "With Watney believed dead," + ' ' +
                          "the remaining crew return to their " + ' ' +
                          "orbiting vessel Hermes without him.",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
                          "https://www.youtube.com/tv#/watch?v=ej3ioOneTy8")  # NOQA
# Sixth movie in list.

zootopia = media.Movie("Zootopia",
                       "G",
                       "In a world populated by" + ' ' +
                       "anthropomorphic mammals, a rabbit" + ' ' +
                       "from rural Bunnyburrow," + ' ' +
                       "named Judy Hopps fulfills her childhood dream",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",  # NOQA
                       "https://www.youtube.com/tv#/watch?v=bY73vFGhSVk")   # NOQA


# movies array

movies = [batman_begins, the_butterfly_effect, xmen_days_of_future_past,
          jungle_book, the_martian, zootopia]


# Main html page which displays all data from media.py and entertainment.py

fresh_tomatoes.open_movies_page(movies)

