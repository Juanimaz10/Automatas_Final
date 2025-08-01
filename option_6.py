from csv_file import CsvFile

class Option6:

    @staticmethod
    def execute():
        Option6.listTop10ArtistsByViews()

    @staticmethod
    def listTop10ArtistsByViews():
        csvFile = CsvFile()
        print(csvFile.listTop10ArtistsByViews())