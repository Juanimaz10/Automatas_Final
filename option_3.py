from constant import SEARCH_SONG_BY_NAME
from csv_file import CsvFile


class Option3:

    @staticmethod
    def execute():
        Option3.SearchForAMusicBySongName()

    @staticmethod
    def SearchForAMusicBySongName():
        csvFile = CsvFile()
        print(csvFile.searchSongByName(str(input(SEARCH_SONG_BY_NAME))))