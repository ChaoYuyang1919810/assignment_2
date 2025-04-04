"""
Name: Chao Yuyang
Date Started: 2025-04-2
Brief Project Description: Song List GUI application using Kivy and OOP principles.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

from songcollection import SongCollection
from song import Song

# Color constants
LEARNED_COLOR = [0.2, 0.7, 0.3, 1]  # Green
UNLEARNED_COLOR = [0.8, 0.2, 0.2, 1]  # Red

class SongListApp(App):
    """Main application class for Song List GUI."""
    status_text = StringProperty("Welcome to Song List 2.0")
    sort_by = StringProperty("title")  # Default sort by title

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.song_collection = SongCollection()
        self.sort_options = {'title': 'Title', 'artist': 'Artist', 'year': 'Year'}

    def build(self):
        """Build the Kivy GUI."""
        self.root = Builder.load_file('app.kv')
        self.song_collection.load_songs('songs.json')
        self.update_song_list()
        return self.root

    def update_status_count(self):
        """Update the learned/unlearned counts."""
        learned = self.song_collection.get_number_of_learned_songs()
        unlearned = self.song_collection.get_number_of_unlearned_songs()
        self.root.ids.status_label.text = f"To learn: {unlearned}  Learned: {learned}"

    def update_song_list(self):
        """Refresh the song buttons display."""
        song_list = self.root.ids.song_list
        song_list.clear_widgets()

        # Sort songs and create buttons
        self.song_collection.sort(self.sort_by)
        for song in self.song_collection.songs:
            button = Button(
                text=str(song),
                background_color=LEARNED_COLOR if song.is_learned else UNLEARNED_COLOR,
                size_hint_y=None,
                height=70,
                on_press=lambda instance, s=song: self.toggle_song_status(s)
            )
            song_list.add_widget(button)

        self.update_status_count()

    def toggle_song_status(self, song):
        """Toggle learned status of a song."""
        song.is_learned = not song.is_learned
        self.update_song_list()
        self.status_text = f"Marked {song.title} as {'learned' if song.is_learned else 'unlearned'}"

    def add_song(self):
        """Handle adding new song with validation."""
        title = self.root.ids.title_input.text.strip()
        artist = self.root.ids.artist_input.text.strip()
        year_str = self.root.ids.year_input.text.strip()

        if not (title and artist and year_str):
            self.status_text = "Complete all fields"
            return

        try:
            year = int(year_str)
            if year <= 0:
                self.status_text = "Year must be > 0"
                return
        except ValueError:
            self.status_text = "Invalid year"
            return

        self.song_collection.add_song(Song(title, artist, year))
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.update_song_list()
        self.status_text = f"Added {title} by {artist}"

    def change_sort(self, sort_key):
        """Handle sorting changes."""
        self.sort_by = sort_key.lower()
        self.update_song_list()

    def on_stop(self):
        """Save songs when app closes."""
        self.song_collection.save_songs('songs.json')

    def clear_inputs(self):
        """Clear Inputs."""
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.status_text = f"All inputs are cleared."

if __name__ == '__main__':
    SongListApp().run()