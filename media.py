class Movie:
    """
    Data structure representing a film or movie containing the title,
    the poster URL and the YouTube link to the movie trailer
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
