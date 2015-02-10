import fresh_tomatoes
import media

"""Creates movies instances to be displayed in the browser"""

toy_story = media.Movie("Toy Story", "Boy and Toys", "http://cdnvideo.dolimg.com/cdn_assets/5670999ffe25e4bd664bc9486adef5171a494e7f.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "Aliens and shit", "http://vignette1.wikia.nocookie.net/jamescameronsavatar/images/9/96/Avatar_Soundtrack.jpg/revision/latest?cb=20100516092820", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

interstellar = media.Movie("Interstellar", "Best Sci-fi movie ever!!!", "http://cdn.screenrant.com/wp-content/uploads/interstellar-poster.jpg", "https://www.youtube.com/watch?v=zSWdZVtXT7E")

fellowshipOfTheRing = media.Movie("LOTR: 1", "Froooodo", "http://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg","https://www.youtube.com/watch?v=Pki6jbSbXIY")

amelie = media.Movie("Amelie Poulain", "The story of Amelie", "http://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg", "https://www.youtube.com/watch?v=0LPxU7659D4")

yellowSubmarine = media.Movie("Yellow Submarine", "The Beatles movie", "http://upload.wikimedia.org/wikipedia/en/b/bb/Yellow_submarine_songtrack.jpg", "https://www.youtube.com/watch?v=DBfy05hbBws")

movies = [toy_story, avatar, interstellar, fellowshipOfTheRing, amelie, yellowSubmarine]

fresh_tomatoes.open_movies_page(movies)
