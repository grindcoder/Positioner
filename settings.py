DOWNLOAD_DIRS = [
    "F:\scaricati_prova",  # Cartella download. Per esempio, Bittorrent > Impostazioni > Cartelle > Sposta i download completati in...
]

DESTINATION_DIR = "F:\POSIZIONATI_DA_SMISTARE"

dst_dir1 = "F:\MOVIES\Da smistare"  # Cartella dei film
dst_dir2 = "F:\MUSIC\Da smistare"  # Cartella musica

FILES_MAPPING = {
    'videos' : {
        'exts' :(
            '.avi',
            '.mp4',
            '.mkv'
        ),
        'destination' : "videos"
    },

    'musics' : {
        'exts' : (
            '.mp3',
         ),
        'destination' : 'musics'
    },
    'torrents' : {
        'exts' : (
            '.torrent',

        ),
        'destination' : "torrents"
    },
    'documents' : {
        'exts' : (
            '.pdf',
            '.doc',
            '.docx',
            '.txt',
        ),
        'destination' : "documents"
    }
}