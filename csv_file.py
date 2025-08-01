import re
import pandas as pd
from pandas import read_csv
from constant import COLUMN_LIKES, COLUMN_COMMENTS, COLUMN_VIEWS, COLUMN_TRACK, SUCCESS_TO_ADD_ROW_IN_CSV_FILE, REGULARS_VALIDATIONS, ISLOADMUSICFORFILE
import csv

class CsvFile:
    def __init__(self) -> None:
        self.__csvFile = read_csv("./resources/listado_temas_2023.csv", low_memory=False).drop_duplicates(subset=[COLUMN_TRACK])

    # --- Option 1 ---
    def removeParenthesesInSongNames(self):
        self.__csvFile[COLUMN_TRACK] = self.__csvFile[COLUMN_TRACK].str.replace(r"\(.*?\)", "", regex=True) 

    @property
    def top5TracksMostLikes(self):
        return self.__csvFile.nlargest(5, COLUMN_LIKES)[[COLUMN_TRACK, COLUMN_LIKES]]

    @property
    def top5TracksMostViews(self):
        return self.__csvFile.nlargest(5, COLUMN_VIEWS)[[COLUMN_TRACK, COLUMN_VIEWS]]

    @property
    def top5TracskMostComments(self):
        return self.__csvFile.nlargest(5, COLUMN_COMMENTS)[[COLUMN_TRACK, COLUMN_COMMENTS]]

    # --- Option 2 ---
    def calculateRatingViewsDividedByLikes(self):
        self.__csvFile['Ratio'] = ((self.__csvFile['Likes'] / self.__csvFile['Views'] ) * 100).fillna(0).astype(int) 
        result = self.__csvFile.nlargest(5, 'Ratio')[['Track', 'Ratio']] 
        result['Ratio'] = result['Ratio'].astype(str) + '%'
        return result.to_string(index=False)

    # --- Option 3 ---
    def searchSongByName(self, nameOfSong):
        self.__csvFile = self.__csvFile.dropna(subset=['Track']) 
        result = self.__csvFile[self.__csvFile['Track'].str.contains(nameOfSong, case=False)] 
        result = result['Track']
        return result.to_string(index=False, header=True)

    # --- Option 4 ---
    def validate_input(self, field_name, input_value):
        if field_name in REGULARS_VALIDATIONS:
            if re.match(REGULARS_VALIDATIONS[field_name], input_value):
                return True
            else:
                print(f"Entrada inválida para {field_name}.")
                return False
        else:
            return True

    def addMusicToCsvFile(self):
        new_row = []
        fields = [',','Index', 'Artist', 'Url_spotify', 'Track', 'Album', 'Album_type', 'Uri', 'Danceability', 'Energy', 'Key', 'Loudness', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Duration_ms', 'Url_youtube', 'Title', 'Channel', 'Views', 'Likes', 'Comments', 'Licensed', 'official_video', 'Stream']
        used_fields = ['Artist', 'Url_spotify', 'Track', 'Album', 'Album_type', 'Uri', 'Duration_ms', 'Url_youtube', 'Title']
        input_file_path = './Resources/Canciones nuevas.csv'
        output_file_path = './Resources/Listado temas 2023.csv'
        loadSongbyFile = int(input(ISLOADMUSICFORFILE))
        if loadSongbyFile == 2:
            for field in fields:
                if field in used_fields:
                    while True:
                        user_input = input(f"Ingrese el valor para '{field}': ")
                        if field == "Duration_ms":
                            user_input = float(user_input) * 60000
                            user_input = str(user_input)
                        if self.validate_input(field, user_input):
                            new_row.append(user_input)
                            break
                else:
                    new_row.append('')

            with open('./resources/listado_temas_2023.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(new_row)
            return SUCCESS_TO_ADD_ROW_IN_CSV_FILE
        
        with open(input_file_path, 'r', newline='') as infile, open(output_file_path, 'a', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=fields)

            for row in reader:
                processed_row = {}
                for field in fields:
                    input_value = row.get(field, '') if field in used_fields else ''
                    if field == "Duration_ms":
                        input_value = float(input_value) * 60000
                        input_value = str(input_value)
                    if self.validate_input(field, input_value):
                        processed_row[field] = input_value
                    else:
                        processed_row[field] = ''  
                writer.writerow(processed_row)
        return SUCCESS_TO_ADD_ROW_IN_CSV_FILE

    # --- Option 5 ---
    def lisTop10SongsByDuration(self, top10=10):
        csvFileSorted = self.__csvFile.sort_values(by='Duration_ms', ascending=False)
        topSongsMostDurations = csvFileSorted.head(top10).copy()        
        topSongsMostDurations['Duration'] = topSongsMostDurations['Duration_ms'].apply(lambda x: "{:02d}:{:02d}:{:02d}".format(int(x // 3600000), int((x % 3600000) // 60000), int((x % 60000) // 1000)))
        return topSongsMostDurations[['Track', 'Duration']].to_string(index=False)

    # --- Option 6 ---
    def listTop10ArtistsByViews(self):
        csv_file_sorted = self.__csvFile.sort_values(by='Views', ascending=False)
        top_10_artists_by_views = csv_file_sorted.drop_duplicates(subset=["Artist"]).head(10)[['Artist', 'Views']]
        return top_10_artists_by_views.to_string(index=False, header=True).replace('.0','')

# --- Option 7: FUNCION fuera de la clase ---
def show_csv_file():
    csv_file = pd.read_csv('resources/canciones_nuevas.csv')  
    csv_string = csv_file.to_string(index=False, header=True)
    return csv_string.replace('.0', '')

