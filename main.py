from pytube import Playlist


url = "https://www.youtube.com/playlist?list=PLDyJYA6aTY1lpbNh66kFpF62QpJyzliT2"

cur_dir = "./"

# playlist = Playlist(url)
# print('Number of videos in playlist: %s' % len(playlist.video_urls))
# playlist.download_all()


playlist = Playlist(url)

for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(cur_dir)