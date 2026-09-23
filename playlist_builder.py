#Benjamin Torres

#1. Building the list
playlist = ["Family Ties","Power","Homecoming","Flashing Lights"]
new_song = input("please input a new song")
new_song = new_song.strip().title()

#2. Modifying the list
print("Number of songs:", len(playlist))
print("Number of songs:", len(playlist))
playlist.remove("Flashing Lights")
del playlist[2]
print("Alphabetical order:", sorted(playlist))
playlist.sort()
playlist.reverse()

#3. Check it & Show it off
print("Power" in playlist)
for song in playlist:
    print(song.upper())

#4. Final Boss — for i in range()
for i in range(len(playlist)):
    print(i + 1, playlist[i])