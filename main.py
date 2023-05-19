# create the easier stuff first
from otherFunctions import selectionSort
import json

#advanced (crate login system to save username, passoword, favs)


def newUser(username, password):
    return {
        "username": username,
        "password": password,
        "favs": []
    }


#basic project
songs = []
favs = []


def newSong(title, artist, genre):
    return {
        "title": title,
        "artist": artist,
        "genre": genre
    }

songs.append(newSong("Shape of You", "Ed Shearen", "Pop"))
songs.append(newSong("Out of Luck", "Lil Tecca", "Hip Hop"))
songs.append(newSong("Search and Destroy", "Drake", "Hip Hop"))


def display_songs():
    for song in songs:
        print("Title:", song["title"])
        print("Artist:", song["artist"])
        print("Genre:", song["genre"])
        print()  # Add an empty line between each song

def filterSongs(title):
    filtered_songs = []
    for song in songs:
        if song["title"].lower() == title.lower():
            filtered_songs.append(song)

    return filtered_songs


def sortSongs():
    songs_copy = songs.copy()
    selectionSort(songs_copy)
    return songs_copy



def addFavs():
    userAddFav = input("What song do you want to add to your favorites list: ").lower()
    found = False

    for song in songs:
        if userAddFav == song["title"].lower():
            favs.append(song)
            found = True
            break

    if found:
        print("Song added to favorites list.")
        print("Favorites list:\n")
        for song in favs:
            print("Title:", song["title"])
            print("Artist:", song["artist"])
            print("Genre:", song["genre"])
            print()  # Add an empty line between each song
    else:
        print("Song not found")


def removeFavs():
    remChoice = input("Enter the song to remove from favorites: ").lower()
    found = False

    for song in favs:
        if remChoice == song["title"].lower():
            favs.remove(song)
            found = True
            print("Song removed from favorites.")
            break

    if not found:
        print("Song not found in the favorites list.")


def displayFavs():
    if not favs:
        print("Favorites list is empty.")
        return

    print("Songs in the favorites list:")
    for song in favs:
        print("Title:", song["title"])
        print("Artist:", song["artist"])
        print("Genre:", song["genre"])
        print()  # Add an empty line between each song


def menu():
    while True:
        print("     Menu     ")
        print("1.Display all songs")
        print("2.Filter songs by title")
        print("3.Sort songs by title")
        print("4.Add songs to favs")
        print("5.Remove songs from favs")
        print("6.Display fav list")
        choice = input("Choose menu option: ")
        print()

        if choice == "1":
            display_songs()
        elif choice == "2":
            userFilter = input("Enter the name of a song you want to search for: ")
            # Call the function to filter songs by title
            filtered = filterSongs(userFilter)

            # Check if any songs were found
            if len(filtered) > 0:
                print("Matching songs found:")
                for song in filtered:
                    print("Title:", song["title"])
                    print("Artist:", song["artist"])
                    print("Genre:", song["genre"])
                    print()
            else:
                print("No matching songs found.")
        elif choice == "3":
            sortedSongs = sortSongs()
            for song in sortedSongs:
                print("Title:", song["title"])
                print("Artist:", song["artist"])
                print("Genre:", song["genre"])
                print()
        elif choice == "4":
            addFavs()
        elif choice == "5":
            removeFavs()
        elif choice == "6":
            displayFavs()

# run program
menu()
