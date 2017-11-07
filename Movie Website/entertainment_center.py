import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4", "G", "1995")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY","PG-13", "2009")

pretty_woman = media.Movie("Pretty Woman",
                    "A prostitute lands the perfect client",
                    "https://upload.wikimedia.org/wikipedia/en/b/b6/Pretty_woman_movie.jpg",
                    "https://youtu.be/Wzii8IuL8lk","R", "1990")


frida = media.Movie("Frida",
                    "The life of the intriguing Mexican artist Frida Kahlo",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Fridaposter.jpg",
                    "https://youtu.be/-CTM7FcY1LE", "R", "2002")


last_of_the_mohicans = media.Movie("The Last of the Mohicans",
                    "The last of the native American Mohicans get wrapped up in frontier Westernization",
                    "https://upload.wikimedia.org/wikipedia/en/d/dd/Mohicansposter.jpg",
                    "https://youtu.be/yaQeVnN6pUc","R", "1992")

twenty_eight_days = media.Movie("28 Days",
                    "The last of the native American Mohicans get wrapped up in frontier Westernization",
                    "https://upload.wikimedia.org/wikipedia/en/f/f7/28_Days_Poster.jpg",
                    "https://youtu.be/y7RXmrlGe-k","PG-13", "2000")

hope_floats = media.Movie("Hope Floats",
                    "The last of the native American Mohicans get wrapped up in frontier Westernization",
                    "https://upload.wikimedia.org/wikipedia/en/0/0e/Hope_Floats.jpg",
                    "https://youtu.be/nNVbi6tGhrg","PG-13", "1998")

gladiator = media.Movie("Gladiator",
                    "The last of the native American Mohicans get wrapped up in frontier Westernization",
                    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                    "https://youtu.be/owK1qxDselE","R", "2000")

clueless = media.Movie("Clueless",
                    "Rich girls in LA come of age.",
                    "https://upload.wikimedia.org/wikipedia/en/2/21/Clueless.jpg",
                    "https://youtu.be/RS0KyTZ3Ie4","PG-13", "1995")

jurassic_park = media.Movie("Jurassic Park",
                    "Scientists bring dinosaurs back to life.",
                    "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                    "https://youtu.be/lc0UehYemQA","PG-13", "1993")

braveheart = media.Movie("Braveheart",
                    "Scotland's last hope of independence.",
                    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                    "https://youtu.be/1cnoM8EiGGU","R", "1995")

dances_with_wolves = media.Movie("Dances with Wolves",
                    "A Union Army lieutenant travels to the Western frontier and interacts with the Lakota indians",
                    "https://upload.wikimedia.org/wikipedia/en/8/82/Dances_with_Wolves_poster.jpg",
                    "https://youtu.be/bZJdhq0_Moo","PG-13", "1990")



#the list of movies we want to display from the instances above
movies = [toy_story, avatar, pretty_woman, frida, last_of_the_mohicans, twenty_eight_days, hope_floats, gladiator, clueless, jurassic_park, braveheart, dances_with_wolves]

#calls another file, which creates the HTML and launches the HTML page
fresh_tomatoes.open_movies_page(movies)




