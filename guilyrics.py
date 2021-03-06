#use "pip install lyricsgenius" to install the lyricsgenius
#and use "pip install pysimplegui" to install pysimplegui
import lyricsgenius
import PySimpleGUI as sg
genius = lyricsgenius.Genius("your token")

sg.theme('Material1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('What is the name of the artist?'), sg.InputText()],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('PythonLyrics Gui', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    artistName = values[0]
    songName = values[1]

    artist = genius.search_artist(artistName, max_songs=3, sort="popularity")
    song = genius.search_song(songName, artist.name)

    print(song.lyrics)

window.close()