class Playlist():
    def __init__(self):
        self.tracks = []

    def add(self, song):
        self.tracks.append(song)
        #parameter for song is string
        #no side effects

    def list_of_songs(self):
        return self.tracks
    #     #no parameters
    #     #return list of songs
    #     #no side effects
    