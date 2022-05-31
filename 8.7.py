def make_album(artist, title, number_of_songs = "" ):
    if number_of_songs:
        album = {"Artist": artist, "Title": title, "Number of songs": number_of_songs}
    else:
        album = {"Artist": artist, "Title": title}
    return album

album1 = make_album("bmth", "sepeternal")

print(album1)