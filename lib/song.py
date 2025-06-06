class Song:
    
    count = 0  
    genres = []
    artists = [] 
    genre_count = {}
    artist_count = {} 
    
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
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        """
        Class method to increment the total count of songs.
        Called whenever a new song is created.
        """
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        """
        Class method to add unique genres to the genres list.
        Called whenever a new song is created.
        """
        # Only add the genre if it's not already in the list
        if cls.genre not in cls.genres:
            cls.genres.append(cls.genre)

    @classmethod
    def add_to_artists(cls):
        """
        Class method to add unique artists to the artists list.
        Called whenever a new song is created.
        """
        # Only add the artist if it's not already in the list
        if cls.artist not in cls.artists:
            cls.artists.append(cls.artist)

    @classmethod
    def add_to_genre_count(cls):
        """
        Class method to update the genre_count histogram.
        Called whenever a new song is created.
        """
        # If the genre exists in the dictionary, increment its count
        if cls.genre in cls.genre_count:
            cls.genre_count[cls.genre] += 1
        # If it's a new genre, initialize its count to 1
        else:
            cls.genre_count[cls.genre] = 1

    @classmethod
    def add_to_artist_count(cls):
        """
        Class method to update the artist_count histogram.
        Called whenever a new song is created.
        """
        # If the artist exists in the dictionary, increment their count
        if cls.artist in cls.artist_count:
            cls.artist_count[cls.artist] += 1
        # If it's a new artist, initialize their count to 1
        else:
            cls.artist_count[cls.artist] = 1