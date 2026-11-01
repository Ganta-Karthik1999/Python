class playlist:
    def __init__(self):
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed : {song}")
    def list_songs(self):
        for song in self.songs:
           print(f"-{song}")

    def temp_method():
        print("This is a temp method !!!")

if __name__ == '__main__':
    p1 = playlist()
    p1.add_song("chippi chippi")
    p1.add_song("ducky ducky song")
    p1.list_songs()
    print("=======================")

    p1.remove_song("chippi chippi")
    p1.list_songs()

    # this is how we delete a method  
    del playlist.temp_method()


