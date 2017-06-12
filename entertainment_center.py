import movie_reviews
import media


goodfellas = media.Movie("Goodfellas",
                        "The true story of Henry Hill, a half-Irish, half-Sicilian Brooklyn kid who is adopted by neighborhood gangsters at an early age and climbs the ranks of a Mafia family.",
                        "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                        "https://youtu.be/qo5jJpHtI1Y")

# print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/d1_JBMrrYw8")

# print(avatar.storyline)

# avatar.show_trailer()

full_metal_jacket = media.Movie("Full Metal Jacket",
                                "In Vietnam, the wind doesn't blow, it sucks.",
                                "https://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",
                                "https://youtu.be/x9f6JaaX7Wg")

# print(full_metal_jacket.storyline)

# full_metal_jacket.show_trailer()

martian = media.Movie("The Martian",
                      "A manned mission to Mars leaves a man stranded. Science is what gets him home!",
                      "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                      "https://youtu.be/LrZCnb9gI_c")

# martian.show_trailer()

boiler_room = media.Movie("Boiler Room",
                          "An ambitious college student learns that easy money is the myth of success",
                          "https://upload.wikimedia.org/wikipedia/en/5/5c/Boiler_room_ver3.jpg",
                          "https://youtu.be/kgCLG4gCAvI")

warlord = media.Movie("Lord of War",
                      "A wily arms dealer dodges bullets and betrayal as he schemes his way to the top of his profession, only to come face to face with his conscience.",
                      "https://upload.wikimedia.org/wikipedia/en/9/92/Lordofwar.jpg",
                      "https://youtu.be/ke79K4bO4P8")

movies = [goodfellas, avatar, full_metal_jacket, martian, boiler_room, warlord]
# movie_reviews.open_movies_page(movies)

