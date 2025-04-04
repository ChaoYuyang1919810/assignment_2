"""
Name: Chao Yuyang
Date Started: 2025-04-04
Brief Project Description: The Use case test for SongCollection Class.
"""

from songcollection import SongCollection
from song import Song

def run_tests():
    """Test SongCollection class."""
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    assert not song_collection.songs

    print("\nTest loading songs:")
    song_collection.load_songs('songs.json')
    assert song_collection.songs

    print("\nTest adding new song:")
    initial_count = len(song_collection.songs)
    song_collection.add_song(Song("New Song", "New Artist", 2023, False))
    assert len(song_collection.songs) == initial_count + 1

    print("\nTest sorting - year:")
    song_collection.sort("year")
    for i in range(len(song_collection.songs) - 1):
        current = song_collection.songs[i]
        next_song = song_collection.songs[i + 1]
        assert (current.year, current.title.lower()) <= (next_song.year, next_song.title.lower())

    print("\nTest sorting - artist:")
    song_collection.sort("artist")
    for i in range(len(song_collection.songs) - 1):
        current = song_collection.songs[i]
        next_song = song_collection.songs[i + 1]
        assert (current.artist.lower(), current.title.lower()) <= (next_song.artist.lower(), next_song.title.lower())

    print("\nTest sorting - title:")
    song_collection.sort("title")
    for i in range(len(song_collection.songs) - 1):
        current = song_collection.songs[i]
        next_song = song_collection.songs[i + 1]
        assert (current.title.lower(), current.year) <= (next_song.title.lower(), next_song.year)

    print("\nTest saving songs:")
    test_filename = 'test_output.json'
    song_collection.save_songs(test_filename)
    new_collection = SongCollection()
    new_collection.load_songs(test_filename)
    assert len(new_collection.songs) == len(song_collection.songs)
    for original, loaded in zip(song_collection.songs, new_collection.songs):
        assert original.title == loaded.title
        assert original.artist == loaded.artist
        assert original.year == loaded.year
        assert original.is_learned == loaded.is_learned

    print("\nTest counts:")
    learned = song_collection.get_number_of_learned_songs()
    unlearned = song_collection.get_number_of_unlearned_songs()
    assert learned + unlearned == len(song_collection.songs)
    song_collection.add_song(Song("Learned Song", "Artist", 2023, True))
    assert song_collection.get_number_of_learned_songs() == learned + 1
    assert song_collection.get_number_of_unlearned_songs() == unlearned

    print("\nAll tests passed!")

run_tests()