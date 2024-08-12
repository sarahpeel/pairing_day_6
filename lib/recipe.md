## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

nouns: song
verbs: add_to_playlist

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class Playlist():
    
    def add(self, song):
        #parameter for song is string
        #no side effects

    def list_of_songs(self):
        #no parameters
        #return list of songs
        #no side effects
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
playlist is empty to start with
"""
playlist = Playlist()
playlist.list_of_songs() == []

"""
add item to playlist
returns updated list
"""
playlist = Playlist()
playlist.add("song1")
playlist.list_of_songs() == ["song1"]

"""
add multiple items to playlist in one go
return updated list
"""
playlist = Playlist()
playlist.add("song1")
playlist.add("song2")
playlist.add("song3")
playlist.add("song4")
playlist.list_of_songs() == ["song1", "song2", "song3", "song4"]

"""
add the same song more than once
return a list of unique values
"""
playlist = Playlist()
playlist.add("song1")
playlist.add("song2")
playlist.add("song3")
playlist.add("song1")
playlist.list_of_songs() == ["song1", "song2", "song3"]


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
