from library_item import LibraryItem

library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2)
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)

def get_name(video_id):
    item = library.get(video_id)
    return item.name if item else None

def get_director(video_id):
    item = library.get(video_id)
    return item.director if item else None

def get_rating(video_id):
    item = library.get(video_id)
    return item.rating if item else None

def get_play_count(video_id):
    item = library.get(video_id)
    return item.play_count if item else None

def list_all():
    return "\n".join(f"{key}: {val.name}" for key, val in library.items())

def add_video(video_id, name, director, rating, play_count=0):
    if video_id not in library:
        library[video_id] = LibraryItem(name, director, rating, play_count)
        return True
    return False

def increment_play_count(video_id):
    if video_id in library:
        library[video_id].play_count += 1

def update_rating(video_id, new_rating):
    if video_id in library:
        library[video_id].rating = new_rating
        return True
    return False       

def get_all_video_ids():
    return list(library.keys())

def list_by_director(director_name):
    filtered_videos = [item.name for item in library.values() if item.director.lower() == director_name.lower()]
    return "\n".join(filtered_videos) if filtered_videos else None

def get_key_by_name(movie_name):
    for key, item in library.items():
        if item.name.lower() == movie_name.lower():
            return key
    return None

def list_by_rating(rating):
    filtered_videos = [(item.name, item.director) for item in library.values() if item.rating == rating]
    return "\n".join(f"Video name: {name}\nDirector name: {director} \nRating: {rating}" for name, director in filtered_videos) if filtered_videos else None

def list_by_director(director_name):
    filtered_videos = [(item.name, item.rating) for item in library.values() if item.director.lower() == director_name.lower()]
    if filtered_videos:
        return "\n".join(f"Video name: {name}\nRating: {rating}" for name, rating in filtered_videos)
    return None
