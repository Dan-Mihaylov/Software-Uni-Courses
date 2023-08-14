class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]


    @classmethod
    def from_photos_count(cls, photo_count: int):
        pages = photo_count // 4

        if photo_count % 4 != 0:
            pages += 1

        return cls(pages)

    def add_photo(self, label: str):
        for page in range(1, self.pages + 1):
            for slot in range(1, 5):
                if slot > len(self.photos[page - 1]):
                    self.photos[page - 1].append(label)
                    return f"{label} photo added successfully on page {page} slot {slot}"

        return f"No more free slots"

    def display(self):
        result = ["-----------",]

        for page in self.photos:
            per_page = []
            for photo in page:
                if photo:
                    per_page.append("[]")
            result.append(" ".join(per_page))
            result.append("-----------")
        return "\n".join(result)


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

