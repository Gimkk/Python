#task8-6

def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'

print(city_country("sydney", "australia"))
print(city_country("paris", "france"))
print(city_country("london", "england"))

#task8-7
print("\n")

def make_album(artist, album_title):
    albums = {artist:album_title}
    return albums

album = make_album("coldplay", "album 1")
print(album)
album.update(make_album("linkin park", "album abc"))
print(album)

#task8-8
print("\n")

albums = dict()
while True:
    artist = input("Enter artist name (press q to quit):")
    if artist == "q":
        break
    album_title = input("Enter album title (press q to quit):")
    if album_title == "q":
        break
    albums.update(make_album(artist, album_title))

print(albums)