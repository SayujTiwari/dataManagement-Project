import json
from otherFunctions import selectionSort

songs = []

def newUser(username, password):
    return {
        "username": username,
        "password": password,
        "favs": []
    }

def newSong(title, artist, genre):
    return {
        "title": title,
        "artist": artist,
        "genre": genre
    }

songs.append(newSong("Shape of You", "Ed Sheeran", "Pop"))
songs.append(newSong("Out of Luck", "Lil Tecca", "Hip Hop"))
songs.append(newSong("Search and Destroy", "Drake", "Hip Hop"))
songs.append(newSong("Blinding Lights", "The Weeknd", "Pop"))
songs.append(newSong("Dance Monkey", "Tones and I", "Pop"))
songs.append(newSong("Sicko Mode", "Travis Scott", "Hip Hop"))
songs.append(newSong("Bad Guy", "Billie Eilish", "Pop"))
songs.append(newSong("Watermelon Sugar", "Harry Styles", "Pop"))
songs.append(newSong("ROXANNE", "Arizona Zervas", "Hip Hop"))
songs.append(newSong("Havana", "Camila Cabello", "Pop"))

def display_songs():
    for song in songs:
        print("Title:", song["title"])
        print("Artist:", song["artist"])
        print("Genre:", song["genre"])
        print()  # Add an empty line between each song

def filter_songs(title):
    filtered_songs = []
    for song in songs:
        if song["title"].lower() == title.lower():
            filtered_songs.append(song)
    return filtered_songs

def sort_songs():
    songs_copy = songs.copy()
    selectionSort(songs_copy)
    return songs_copy

def add_favs(user):
    userAddFav = input("What song do you want to add to your favorites list: ").lower()
    found = False

    for song in songs:
        if userAddFav == song["title"].lower():
            user["favs"].append(song)
            found = True
            break

    if found:
        print("Song added to favorites list.")
    else:
        print("Song not found")

def remove_favs(user):
    remChoice = input("Enter the song to remove from favorites: ").lower()
    found = False

    for song in user["favs"]:
        if remChoice == song["title"].lower():
            user["favs"].remove(song)
            found = True
            print("Song removed from favorites.")
            break

    if not found:
        print("Song not found in the favorites list.")

def display_favs(user):
    favs = user["favs"]
    if not favs:
        print("Favorites list is empty.")
        return

    print("Songs in the favorites list:")
    for song in favs:
        print("Title:", song["title"])
        print("Artist:", song["artist"])
        print("Genre:", song["genre"])
        print()  # Add an empty line between each song

def menu(user):
    while True:
        print("     Menu     ")
        print("1. Display all songs")
        print("2. Filter songs by title")
        print("3. Sort songs by title")
        print("4. Add songs to favorites")
        print("5. Remove songs from favorites")
        print("6. Display favorites list")
        print("7. Logout")
        choice = input("Choose menu option: ")
        print()

        if choice == "1":
            display_songs()
        elif choice == "2":
            userFilter = input("Enter the name of a song you want to search for: ")
            # Call the function to filter songs by title
            filtered = filter_songs(userFilter)

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
            sortedSongs = sort_songs()
            for song in sortedSongs:
                print("Title:", song["title"])
                print("Artist:", song["artist"])
                print("Genre:", song["genre"])
                print()
        elif choice == "4":
            add_favs(user)
        elif choice == "5":
            remove_favs(user)
        elif choice == "6":
            display_favs(user)
        elif choice == "7":
            print("Logged out successfully.")
            return

# Main login menu
def main_login():
    users = load_users()
    while True:
        selection = get_menu_selection()
        if selection == "1":
            print("\nRegistration")
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(users, username, password)
        elif selection == "2":
            print("\nLogin")
            username = input("Enter username: ")
            password = input("Enter password: ")
            check_user(users, username, password)
        else:
            print("Invalid selection")

def get_menu_selection():
    print("User Login System")
    print("1. Create new user")
    print("2. Login")
    return input("Selection (1-2): ")

def load_users():
    with open("users.json", "r") as file:
        return json.load(file)
 

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

def register_user(users, username, password):
    search = linear_search(users, username, "username")
    if search == -1:
        print("Successfully registered.")
        user = newUser(username, password)
        users.append(user)
        save_users(users)
        menu(user)  # Pass the current user to the menu function
    else:
        print("Username already taken.")

def linear_search(an_array, item, key):
    for i in range(len(an_array)):
        if an_array[i][key] == item:
            return i
    return -1

def check_user(users, username, password):
    u_index = linear_search(users, username, "username")
    if u_index == -1:
        print("Username not found.")
    else:
        if users[u_index]["password"] == password:
            print(f"\nWelcome {username}.")
            menu(users[u_index])  # Pass the current user to the menu function
        else:
            print("Incorrect password.")

# Run the program
main_login()
