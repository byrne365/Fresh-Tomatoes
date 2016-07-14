import fresh_tomatoes
import media

#First movie in list.

#Tiltle of movie and the class it is refering to in the media.py file

batman_begins  = media.Movie("Batman Begins",
                             
                             #Valid rating

                             "PG-13",

                             #Storyline src

                             "When his parents were killed, billionaire playboy Bruce Wayne adopts the image of a bat to strike fear into the criminals.",
                             
                             #Poster image src
                             
                             "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg", 
                             
                             #The URl for the youtube tailer

                             "https://www.youtube.com/tv#/watch?v=neY2xVmOfUM")

#Second movie in list.

the_butterfly_effect = media.Movie("The Butterfly Effect",
                                   "PG-13",
                                   "Evan Treborn, who blacks out frequently, finds that when he reads from his adolescent journals, he travels back in time, and able to redo parts of his past.",
                                   "https://upload.wikimedia.org/wikipedia/en/4/43/Butterflyeffect_poster.jpg",
                                   "https://www.youtube.com/watch?v=B8_dgqfPXFg")
#Third movie in list.

xmen_days_of_future_past = media.Movie("Xmen:Days of future Past",
                                       "PG-13",
                                       "In the future, robots known as Sentinels are exterminating mutants and their human allies. Wolverine's consciousness is sent back fifty years to 1973, to prevent the future.",
                                       "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg",
                                       "https://www.youtube.com/tv#/watch/video/control?v=pK2zYHWDZKo&resume")

#Fourth movie in list.

jungle_book = media.Movie("The Jungle Book",
                          "PG",
                          "Mowgli is a man cub raised by the Indian wolf Raksha and her pack, in a jungle of Seoni, Bagheera trains Mowgli to learn the ways of the wolves.",
                          "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",
                          "https://www.youtube.com/tv#/watch?v=HcgJRQWxKnw")

#Fifth movie in list.

the_martian = media.Movie("The Martian",
                          "PG-13",
                          "Astronaut Mark Watney is struck by debris and lost in a storm on Mars. With Watney believed dead, the remaining crew return to their orbiting vessel Hermes without him.",
                         "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                         "https://www.youtube.com/tv#/watch?v=ej3ioOneTy8")

#Sixth movie in list.

zootopia = media.Movie("Zootopia",
                       "G",
                       "In a world populated by anthropomorphic mammals, a rabbit from rural Bunnyburrow named Judy Hopps fulfills her childhood dream.",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/tv#/watch?v=bY73vFGhSVk")

#movies array

movies = [batman_begins, the_butterfly_effect, xmen_days_of_future_past, jungle_book, the_martian, zootopia]


#Main html page which displays all data from media.py and entertainment.py

fresh_tomatoes.open_movies_page(movies)


