class LibraryItem:
    all_items = []

    def __init__(self, name, director, rating=0):
        self._validate_rating(rating)
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0
        self.reactions = {}
        LibraryItem.all_items.append(self)

    def _validate_rating(self, rating):
        if not isinstance(rating, int):
            raise TypeError("Rating must be an integer")
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")

    def play(self):
        self.play_count += 1

    def info(self):
        return f"{self.name} - {self.director} ({self.rating}) - Played {self.play_count} times"

   