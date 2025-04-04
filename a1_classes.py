from song import Song
from songcollection import SongCollection

SONGS_FILE = "songs.json"

"""
Name: Chao Yuyang
Date Started: 2025-04-04
Brief Project Description: Song List 1.0 with OOP implementation.
"""

def main():
    """Main program logic."""
    print("Song List 1.0 - by Yuyang Chao")
    song_collection = SongCollection()
    load_songs_from_file(song_collection, SONGS_FILE)
    print(f"{len(song_collection.songs)} songs loaded.\n")

    choice = ""
    while choice != "Q":
        show_menu()
        choice = input(">>> ").strip().upper()

        if choice == "D":
            display_song_list(song_collection)
        elif choice == "A":
            add_new_song(song_collection)
        elif choice == "C":
            complete_song(song_collection)
        elif choice == "Q":
            save_songs_to_file(song_collection, SONGS_FILE)
            print(f"\n{len(song_collection.songs)} songs saved to {SONGS_FILE}")
            print("Make some music!")
        else:
            if choice:  # Don't show error for empty input
                print("Invalid menu choice")
        print()


def show_menu():
    """Display menu options."""
    print("Menu:")
    print("D - Display songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")


def load_songs_from_file(collection, filename):
    """Load songs from JSON file into the SongCollection."""
    try:
        collection.load_songs(filename)
    except FileNotFoundError:
        print("No existing file found. Starting with an empty collection.")


def save_songs_to_file(collection, filename):
    """Save songs from SongCollection to JSON file."""
    collection.save_songs(filename)


def display_song_list(collection):
    """Display formatted list of songs."""
    if not collection.songs:
        print("No songs to display")
        return

    learned_count = collection.get_number_of_learned_songs()
    unlearned_count = collection.get_number_of_unlearned_songs()

    max_title = max(len(song.title) for song in collection.songs) if collection.songs else 0
    max_artist = max(len(song.artist) for song in collection.songs) if collection.songs else 0

    for i, song in enumerate(collection.songs, 1):
        prefix = "* " if not song.is_learned else "  "
        print(f"{i}. {prefix}{song.title:<{max_title}} - {song.artist:<{max_artist}} ({song.year})")

    print(f"\n{learned_count} songs learned, {unlearned_count} songs still to learn")


def add_new_song(collection):
    """Add a new song to the SongCollection."""
    print("Enter details for new song")
    while True:
        title = input("Title: ").strip()
        if title:
            break
        print("Title can't be blank!")

    while True:
        artist = input("Artist: ").strip()
        if artist:
            break
        print("Artist can't be blank!")

    while True:
        year_str = input("Year: ").strip()
        if year_str.isdigit() and int(year_str) > 0:
            year = int(year_str)
            break
        print("Invalid year - must be positive number")

    new_song = Song(title, artist, year)
    collection.add_song(new_song)
    print(f"\n{title} by {artist} ({year}) added")


def complete_song(collection):
    """Mark a song as learned."""
    unlearned_songs = [song for song in collection.songs if not song.is_learned]
    if not unlearned_songs:
        print("No more songs to learn!")
        return

    while True:
        try:
            print("Enter song number to mark as learned")
            num = int(input(">>> "))
            if 1 <= num <= len(collection.songs):
                selected_song = collection.songs[num - 1]
                if selected_song.is_learned:
                    print(f"You already know {selected_song.title}")
                else:
                    selected_song.mark_learned()
                    print(f"Congratulations! Learned {selected_song.title}")
                break
            print("Invalid song number")
        except ValueError:
            print("Please enter a number")


if __name__ == "__main__":
    main()
