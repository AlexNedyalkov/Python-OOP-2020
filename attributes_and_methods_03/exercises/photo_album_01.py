"""
    1. Photo Album
Create a class called PhotoAlbum. Upon initialization it should receive pages (int).
It should also have one more attribute: photos (empty matrix).
The amount of sub lists must be equal to the number of pages. The class should also have 3 more methods:
    • from_photos_count(photos_count: int) – creates a new instance of PhotoAlbum
     with pages x`of the photos count (each page can contain 4 photos)
    • add_photo(label:str) – add the photo in the next possible page and slot and return
    "{label} photo added successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}".
     If there are no free slots left, return "No more free spots"
    • display() – return a string representation of each page and the photos in it.
    Each photo is marked with "[]" and the page separation is made using 11 dashes (-).
    For example, if we have 1 page and 2 photos:
"""
class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages: int = pages
        self.photos = [[] for _ in range(self.pages)]
        self.page_number = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(int(photos_count // 4))

    def add_photo(self, label: str):
        if len(self.photos[self.page_number]) == 4:
            if self.page_number >= self.pages - 1:
                return "No more free spots"
            self.page_number += 1
        self.photos[self.page_number].append(label)
        return  f"{label} photo added successfully on page {self.page_number + 1} slot {len(self.photos[self.page_number])}"

    def display(self):
        result = ""
        for page in range(self.pages):
            result += '-' * 11 + "\n"
            result += ' '.join('[]' for x in self.photos[page]) + '\n'
        result += '-' * 11
        return result


"""
return a string representation of each page and the photos in it. 
Each photo is marked with "[]" and the page separation is made using 11 dashes (-).
"""

album = PhotoAlbum(3)
album = PhotoAlbum.from_photos_count(21)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
