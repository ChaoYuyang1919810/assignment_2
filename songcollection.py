
"""
Name: Chao Yuyang
Date Started: 2025-04-2
Brief Project Description: The SongCollection Class Implementation.
"""

import json
from song import Song

class SongCollection:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_number_of_unlearned_songs(self):
        return sum(not song.is_learned for song in self.songs)

    def get_number_of_learned_songs(self):
        return sum(song.is_learned for song in self.songs)

    def load_songs(self, filename):
        with open(filename, 'r') as file:
            songs_data = json.load(file)
            for song_data in songs_data:
                title = song_data.get('title', '')
                artist = song_data.get('artist', '')
                year = song_data.get('year', 0)
                is_learned = song_data.get('learned', False)
                self.add_song(Song(title, artist, year, is_learned))

    def save_songs(self, filename):
        songs_data = [{'title': song.title, 'artist': song.artist, 'year': song.year, 'learned': song.is_learned} for song in self.songs]
        with open(filename, 'w') as file:
            json.dump(songs_data, file, indent=4)

    def sort(self, key):
        key_funcs = {
            'year': lambda s: s.year,
            'artist': lambda s: s.artist.lower(),
            'title': lambda s: s.title.lower(),
        }
        primary_func = key_funcs.get(key, key_funcs['year'])  # default to year if invalid key
        self.songs.sort(key=lambda song: (primary_func(song), song.title.lower()))

    def __str__(self):
        return "\n".join(str(song) for song in self.songs)