class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        #all this instances are added upon intialization
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

# class method to count the number of songs created
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

# class method to add the genre of a song when it is added
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

# class method to add the artist of the song when added
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

# class method to count the genres of the song and represent as a dict
    @classmethod
    def add_to_genre_count(cls, genre):
        # if the genre exists it is incremented once again
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        # adds the genre count for the first time
        else: 
            cls.genre_count[genre] = 1
    
# class method to count artists of a song and represent the data in a dict
    @classmethod
    def add_to_artist_count(cls, artist):
        # if the genre exists it is incremented once again
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        # adds the genre count for the first time
        else:
            cls.artist_count[artist] = 1