from csv_file import CsvFile


class Option2:

    @staticmethod
    def execute():
        Option2.listTheTop5SongsWithTheBestRating()

    @staticmethod
    def listTheTop5SongsWithTheBestRating():
        csvFile = CsvFile()
        print(csvFile.calculateRatingViewsDividedByLikes())