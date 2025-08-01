MAIN_MENU = """
----------------------------------------------------------------------------------------

1) List the 5 songs with the most likes, views, and comments
2) List the 5 songs with the best ratio
3) Search for a song
4) Add a new row
5) List the 10 songs with the longest duration
6) List the 10 artists with the most total plays
7) Show the csv file
8) [Exit]
----------------------------------------------------------------------------------------"""

USER_INPUT_OPTION_TO_MAIN_MENU = "Insert the option you want to execute: "

PROGRAM_OFF = "[ [ OFF ] ]"

COLUMN_LIKES = "Likes"
COLUMN_VIEWS = "Views"
COLUMN_COMMENTS = "Comments"
COLUMN_TRACK = "Track"

SEARCH_SONG_BY_NAME = "Insert the name of the song: " 


REGULARS_VALIDATIONS = {
    'Artist': r'^[A-Za-z0-9\s]+$',
    'Title': r'^[A-Za-z0-9\s]+$',
    'Url_spotify': r'^(https?://)?(open\.)?(spotify\.)?(com/)?(track/)?[A-Za-z0-9]+$',
    'Track': r'^[A-Za-z0-9\s]+$',
    'Album': r'^[A-Za-z0-9\s]+$',
    'Album_type': r'^(compilation|album|single)$',
    'Uri': r'^(spotify:)?(track:)?[A-Za-z0-9]+$',
    'Duration_ms': r'^\d+(\.\d+)?$',
    'Url_youtube': r'^(https?://)?(www\.)?(youtube\.com?)?/?(watch\?)?(v=)?[A-Za-z0-9_-]+$'
}

SUCCESS_TO_ADD_ROW_IN_CSV_FILE = "Successfully added a new row to the CSV file."

ISLOADMUSICFORFILE = " do you want to add songs manually? (1-no, 2-yes): "