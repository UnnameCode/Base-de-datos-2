# Bases de datos 2, 2023 - Actividad preparatoria
#una lista de tuplas como una versión de una "bd" "key/value"
class Playlist:

    numQueries = 0
    
    def __init__(self) -> None:
        self.playlist = []

    def addRow(self, pArtist, pSong, pGenre, pTime):
        newSong = {"artist": pArtist, "song": pSong, "genre": pGenre, "time":pTime}
        self.playlist.append(newSong)

    def printDB(self):
        print(self.playlist)

    def addArtist(artist):
        pass

    def addSong(artist, song):
        pass

    def loadDataFromCSV(self, file):
        with open(file) as f:
            for line in f:
                line = line.strip()
                values = line.split(sep=';')                
                record = {"artist":values[0], "song":values[1], "genre":values[2], "time":values[3]}
                self.playlist.append(record)
            
    #filtrado con una funcion de alto orde (filter) y una funcion lambda
    def filterPlayList(self, songName):
        filteredList = list ( filter( lambda x: x["song"] == songName , self.playlist ) )
        print(filteredList)

    #filtrado con list comprehennsion
    def filterPlayList(self, genre):
        filteredList = [ d for d in self.playlist if d ["genre"] == genre ]
        print(filteredList)


    