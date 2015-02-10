import webbrowser

class Movie():
	"""Stores relevant information about a movie, such as title, poster and trailer url """

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]	

	def __name__(self):
		return "Movie"

	def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_youtube_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_url
		self.trailer_youtube_url = movie_youtube_url
		
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
