from project.song import Song


class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = [x for x in self.args]

    def add_song(self, song: Song):

        if self.published:
            return f"Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):

        if self.published:
            return f"Cannot remove songs. Album is published."

        if all(x.name != song_name for x in self.songs):
            return f"Song is not in the album."

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):

        result = [f"Album {self.name}"]

        for song in self.songs:
            result.append(f"== {song.get_info()}")

        return "\n".join(result)

