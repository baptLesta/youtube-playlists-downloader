# youtube-playlists-downloader

`sudo youtube-dl -U`
`brew install ffmpeg`

## Installation
Create a .env like with the FOLDER_PATH string. eg:  

```.env
FOLDER_PATH=${HOME}/Music
```

Run, in the root project:
```
chmod u+x youtube-playlists-downloader.py
./youtube-playlists-downloader.py
```

## Create alias
Add in you ~/.zshrc:
```
alias maree-basse='python <YOUR_PATH_TO_THIS_APP_FOLDER>/youtube-playlists-downloader/youtube-playlists-downloader.py'
```
