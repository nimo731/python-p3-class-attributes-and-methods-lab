class Song:
    # Class attributes to store data across all instances
    count = 0  # Tracks total number of songs created
    genres = []  # Stores unique genres
    artists = []  # Stores unique artists
    genre_count = {}  # Histogram of genres and their counts
    artist_count = {}  # Histogram of artists and their counts

    def __init__(self, name, artist, genre):
        """
        Initialize a new Song instance with name, artist, and genre.
        Also updates class-level tracking of songs, genres, and artists.
        
        Args:
            name (str): The name of the song
            artist (str): The artist who created the song
            genre (str): The genre of the song
        """
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level tracking
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """
        Class method to increment the total count of songs.
        Called whenever a new song is created.
        """
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """
        Class method to add unique genres to the genres list.
        Called whenever a new song is created.
        """
        # Only add the genre if it's not already in the list
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """
        Class method to add unique artists to the artists list.
        Called whenever a new song is created.
        """
        # Only add the artist if it's not already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Class method to update the genre_count histogram.
        Called whenever a new song is created.
        """
        # If the genre exists in the dictionary, increment its count
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        # If it's a new genre, initialize its count to 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """
        Class method to update the artist_count histogram.
        Called whenever a new song is created.
        """
        # If the artist exists in the dictionary, increment their count
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        # If it's a new artist, initialize their count to 1
        else:
            cls.artist_count[artist] = 1 