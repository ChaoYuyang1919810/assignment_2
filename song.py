"""
Name: Chao Yuyang
Date Started: 2025-04-4
Brief Project Description: The Song Class Implementation.
"""


class Song:
    def __init__(self, title="", artist="", year=0, is_learned=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.year})"

    def mark_learned(self):
        self.is_learned = True

    def mark_unlearned(self):
        self.is_learned = False