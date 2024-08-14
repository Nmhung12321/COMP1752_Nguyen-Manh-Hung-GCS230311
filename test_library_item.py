from library_item import LibraryItem
import pytest

def test_default_rating():
    item = LibraryItem("Tom and Jerry", "Fred Quimby")
    assert item.name == "Tom and Jerry"
    assert item.director == "Fred Quimby"
    assert item.rating == 0
    assert item.play_count == 0
    
def test_video_details():
    item = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
    assert item.name == "Tom and Jerry"
    assert item.director == "Fred Quimby"
    assert item.rating == 4
    assert item.play_count == 0

def test_info():
    item = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
    assert item.info() == "Tom and Jerry - Fred Quimby (4) - Played 0 times"
    
def test_play_count():
    item = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
    assert item.play_count == 0
    item.play()
    assert item.play_count == 1
    item.play()
    assert item.play_count == 2
    assert item.info() == "Tom and Jerry - Fred Quimby (4) - Played 2 times"
    
def test_invalid_rating():
    with pytest.raises(ValueError):
        LibraryItem("Tom and Jerry", "Fred Quimby", -1)
        
def test_invalid_rating_type():
    with pytest.raises(TypeError):
        LibraryItem("Tom and Jerry", "Fred Quimby", "four")