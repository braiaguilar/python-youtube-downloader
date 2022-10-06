from pytube import YouTube, Playlist, Channel
from prompt_toolkit import prompt

option = prompt('''

>>> What do you want to do?:
    1. Download a YouTube video or audio
    2. Download videos or audios from a YouTube playlist
    3. Download videos or audios from a YouTube channel
    4. Exit

''')

if option == '1':
    option2 = prompt('''>>> Select a download option:
    1. Video with audio
    2. Video only
    3. Audio only
    4. Exit

    ''')
    if option2 == '4':
        exit()
    elif option2 != '1' and option2 != '2' and option2 != '3':
        print('>>> Invalid option.')
        exit()
    url = prompt('>>> Enter the video URL: ')
    path = prompt(
        '>>> Destination path (leave blank for current directory): ') or '.'
    print('>>> The video will be downloaded in the highest resolution posible.')
    print('>>> Downloading...')
    yt = YouTube(url)
    if option2 == '1':
        yt = yt.streams.get_highest_resolution()
    elif option2 == '2':
        yt = yt.streams.filter(only_video=True)[0]
    elif option2 == '3':
        yt = yt.streams.filter(only_audio=True)[0]
    yt.download(path)
    print('>>> Successful download!')

elif option == '2':
    option2 = prompt('''>>> Select a download option:
    1. Videos with audio
    2. Videos only
    3. Audios only
    4. Exit

    ''')
    if option2 == '4':
        exit()
    elif option2 != '1' and option2 != '2' and option2 != '3':
        print('>>> Invalid option.')
        exit()
    url = prompt('>>> Enter the playlist URL: ')
    path = prompt(
        '>>> Enter download path (leave blank for current directory): ') or '.'
    print('>>> The videos will be downloaded in the highest resolution posible.')
    print('>>> Downloading...')
    p = Playlist(url)
    for video in p.videos:
        if option2 == '1':
            p = video.streams.get_highest_resolution()
        elif option2 == '2':
            p = video.streams.filter(only_video=True)[0]
        elif option2 == '3':
            p = video.streams.filter(only_audio=True)[0]
        p.download(path)
    print('>>> Videos downloaded successfully!')

elif option == '3':
    option2 = prompt('''>>> Select a download option:
    1. Videos with audio
    2. Videos only
    3. Audios only
    4. Exit

    ''')
    if option2 == '4':
        exit()
    elif option2 != '1' and option2 != '2' and option2 != '3':
        print('>>> Invalid option.')
        exit()
    url = prompt('>>> Enter the channel URL: ')
    path = prompt(
        '>>> Enter download path (leave blank for current directory): ') or '.'
    print('>>> The videos will be downloaded in the highest resolution posible.')
    print('>>> Downloading...')
    c = Channel(url)
    for video in c.videos:
        if option2 == '1':
            c = video.streams.get_highest_resolution()
        elif option2 == '2':
            c = video.streams.filter(only_video=True)[0]
        elif option2 == '3':
            c = video.streams.filter(only_audio=True)[0]
        elif option2 == '4':
            exit()
        c.download(path)
    print('>>> Videos downloaded successfully!')

elif option == '4':
    exit()

else:
    print('>>> Invalid option.')
    exit()
