import media
import fresh_tomatoes

toy_story = media.Movie("Inception",
                        "A story about the dreams control",
                        "https://upload.wikimedia.org/wikipedia/en/1/18/Inception_OST.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)
#avatar.show_trailer()
Ex_machina = media.Movie("Ex Machina",
                         "An intelligent Robot was programed to find the way out via influencing other humans",
                         "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
                         "https://www.youtube.com/watch?v=sNExF5WYMaA")
#print(Ex_machina.storyline)
#Ex_machina.show_trailer()
movies = [toy_story, avatar, Ex_machina]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
