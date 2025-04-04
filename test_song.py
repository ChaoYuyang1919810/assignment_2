"""
Name: Chao Yuyang
Date Started: 2025-04-04
Brief Project Description: The Use Case test for Song Class.
"""

from song import Song

def run_tests():
    """Test Song class."""
    print("Test empty song:")
    default_song = Song()
    assert default_song.title == ""
    assert default_song.artist == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    print("\nTest initial-value song:")
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    assert initial_song.title == "My Happiness"
    assert initial_song.artist == "Powderfinger"
    assert initial_song.year == 1996
    assert initial_song.is_learned

    print("\nTest marking methods:")
    initial_song.mark_unlearned()
    assert not initial_song.is_learned
    initial_song.mark_learned()
    assert initial_song.is_learned

    print("\nAll tests passed!")

run_tests()