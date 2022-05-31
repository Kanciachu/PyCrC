def make_album(artist, title, number_of_songs = "" ):
    if number_of_songs:
        album = {"Artist": artist, "Title": title, "Number of songs": number_of_songs}
    else:
        album = {"Artist": artist, "Title": title}
    return album


msg1 = ""
msg2 = ""
while True:
    msg1 = input("What is the name of the band?")
    if msg1 == "q":
        break
    msg2 = input("What is the name of the album?")
    if msg2 == "q":
        break
    album1 = make_album(msg1, msg2)
    print(album1)