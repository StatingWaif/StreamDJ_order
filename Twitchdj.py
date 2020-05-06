import requests
from bs4 import BeautifulSoup as bs
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

class Twitchdj:
    def __init__(self, url):
        self.twitch_url = url
        self.session = requests.Session()
        content = self.session.get(url).text
        soup = bs(content, 'lxml')
        tmp = soup.find('button', attrs={'id': 'add_track_b'})['onclick'].replace('add_track(', '').replace(')', '')
        
        self.channel = int(tmp)

    def add_song(self, yt_url, author, ui):
        if '/playlist' in yt_url:
            content = self.session.get(yt_url).text

            soup = bs(content, 'lxml')

            links = soup.find_all('a', attrs={'class':"pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link"})

            count = 0

            for i in range(len(links)):
                music_source = links[i]['href']
                new_url = f'https://www.youtube.com{music_source}'
    
                data = {'url': new_url, 'author': author}

                self.session.post(f'https://streamdj.ru/includes/back.php?func=add_track&channel={self.channel}', data=data)
                
                count += 1
            
                ui.LOGS.setText(f'Done {count}/{len(links)}')

        else:
            data = {'url': yt_url, 'author': author}
            self.session.post(f'https://streamdj.ru/includes/back.php?func=add_track&channel={self.channel}', data=data)

            now = datetime.now()

            time_now = f'{now.hour}:{now.minute}:{now.second}'

            ui.LOGS.setText(f'Done ({time_now})')