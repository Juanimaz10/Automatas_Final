from csv_file import CsvFile

class Option1:

    @staticmethod
    def execute():
        Option1.ListTheTop5SongsWithTheMostViewsLikesAndComments()

    @staticmethod
    def ListTheTop5SongsWithTheMostViewsLikesAndComments():
        csvFile = CsvFile()
        csvFile.removeParenthesesInSongNames()
        songs = {1: csvFile.top5TracksMostLikes, 2: csvFile.top5TracksMostViews, 3: csvFile.top5TracskMostComments}
        for i in range(1, len(songs) + 1):
            print(f"\n\n{songs[i].to_string(index=False)}")