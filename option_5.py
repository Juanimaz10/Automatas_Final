from csv_file import CsvFile

class Option5:

    @staticmethod
    def execute():
        Option5.listTheTop10SongsWithTheMostDuration()

    @staticmethod
    def listTheTop10SongsWithTheMostDuration():
        csvFile = CsvFile()
        print(csvFile.lisTop10SongsByDuration())