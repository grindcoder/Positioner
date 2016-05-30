DOWNLOAD_DIRS = [
    "F:\scaricati_prova",  # Cartella download. Per esempio, Bittorrent > Impostazioni > Cartelle > Sposta i download completati in...
]

DESTINATION_DIR = "F:\scaricati_prova"

dst_dir1 = "F:\MOVIES\Da smistare"  # Cartella dei film
dst_dir2 = "F:\MUSIC\Da smistare"   # Cartella musica

FILES_MAPPING = {
    'videos' : {
        'exts' :(
            '.avi',
            '.mp4',
            '.mkv'
        ),
        'destination' : "\\Videos"
    },

    'musics' : {
        'exts' : (
            '.mp3',
            '.mp4',
            '.flac',
         ),
        'destination' : '\\Musics'
    },
    'torrents' : {
        'exts' : (
            '.torrent',

        ),
        'destination' : "\\Torrents"
    },
    'documents' : {
        'exts' : (
            '.pdf',
            '.doc',
            '.docx',
            '.txt',
        ),
        'destination' : "\\Documents"
    },

    'programs' : {
        'exts' : ('.exe','.msi'),
        'destination' : '\\Programs'
    },

    # 'images' : {
    #     'exts' : ('.jpg','.png','.tiff'),
    #     "destination" : '\\Images'
    # }
}