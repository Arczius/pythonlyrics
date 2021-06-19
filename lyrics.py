#use the command "pip install lyricsgenius to install"
import lyricsgenius
genius = lyricsgenius.Genius("your token")

row = "------------"

print("what is the name of the artist?")
artistName = input("-")
artist = genius.search_artist(artistName, max_songs=3, sort="popularity")
print(row)

print("what is the name of the song?")
songName = input("-")
print(row)

song = genius.search_song(songName, artist.name)

print(song.lyrics)
