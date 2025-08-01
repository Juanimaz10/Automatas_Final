from csv_file import CsvFile

class Option4:

    @staticmethod
    def execute():
        Option4.AddMusicInNewRowInExcel()

    @staticmethod
    def AddMusicInNewRowInExcel():
        csvFile = CsvFile()
        print(csvFile.addMusicToCsvFile())