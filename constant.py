MAIN_MENU = """
----------------------------------------------------------------------------------------
1) Listar las 5 canciones con más likes, vistas y comentarios

2) Listar las 5 canciones con mejor ratio.

3) Buscar una canción.

4) Agregar nueva fila.

5) Listar las 10 canciones con más duración.

6) Listar los 10 artistas con más reproducciones en total.

7) [SALIR]
----------------------------------------------------------------------------------------"""

USER_INPUT_OPTION_TO_MAIN_MENU = "Ingrese opción: "

PROGRAM_OFF = "[ [ OFF ] ]"

COLUMN_LIKES = "Likes"
COLUMN_VIEWS = "Views"
COLUMN_COMMENTS = "Comments"
COLUMN_TRACK = "Track"

SEARCH_SONG_BY_NAME = "Ingrese nombre de la cancion: "


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

SUCCESS_TO_ADD_ROW_IN_CSV_FILE = "Éxito al añadir"

ISLOADMUSICFORFILE = "Quiere agregar canciones manualmente?(1-no, 2-si):"