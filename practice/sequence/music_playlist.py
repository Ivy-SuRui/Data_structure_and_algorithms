# create a class of song
class Song:
    def __init__(self,name):
        self.name = name
        self.next = None


# create a class of playlist
class Playlist:
    def __init__(self):
        self.head = None
        self.current = None

    # add songs
    def add_song(self,name):
        new_song = Song(name)
        if self.head == None:
            self.head = new_song
            self.current = self.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song


    # play the current song 
    def play_current(self):
        if self.current:
            print(f"You're now playing {self.current.name}")
        else:
            print("There is no song in your playlist.")

    # play the next song
    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_current()
        else:
            print("That's the end of this playlist.")


    # show the playlist
    def show_playlist(self):
        if self.head:
            temp = self.head
            while temp:
                print(f"{temp.name}", end = " -> ")
                temp = temp.next
            print("The end")
        else:
            print("You haven't added any song to this playlist.")

def main():
    loved_song = Playlist()
    loved_song.add_song("Love story")
    loved_song.add_song("Hello")
    loved_song.show_playlist()
    loved_song.play_current()
    loved_song.play_next()


if __name__ == "__main__":
    main()