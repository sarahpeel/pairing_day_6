from lib.track_list import Playlist

"""
playlist is empty to start with
"""
def test_playlist_is_empty():
    playlist = Playlist()
    assert playlist.list_of_songs() == []

"""
add item to playlist
returns updated list
"""
def test_add_song_to_playlist():
    playlist = Playlist()
    playlist.add("song1")
    assert playlist.list_of_songs() == ["song1"]

"""
add multiple items to playlist in one go
return updated list
"""
def test_add_multiple_songs():
    playlist = Playlist()
    playlist.add("song1")
    playlist.add("song2")
    playlist.add("song3")
    playlist.add("song4")
    assert playlist.list_of_songs() == ["song1", "song2", "song3", "song4"]

"""
add the same song more than once
return a list of unique values
"""
# def test_add_duplicate_song_and_return_unique_list():
#     playlist = Playlist()
#     playlist.add("song1")
#     playlist.add("song2")
#     playlist.add("song3")
#     playlist.add("song1")
#     assert playlist.list_of_songs() == ["song1", "song2", "song3"]




# list_inp = [100, 75, 100, 20, 75, 12, 75, 25] 

# res_list = []

# for item in list_inp: 
#     if item not in res_list: 
#         res_list.append(item) 

# print("Unique elements of the list using append():\n")    
# for item in res_list: 
#     print(item)

# list_inp = [100, 75, 100, 20, 75, 12, 75, 25] 

# set_res = set(list_inp) 
# print("The unique elements of the input list using set():\n") 
# list_res = (list(set_res))
 
# for item in list_res: 
#     print(item)