# A Python Script to Download 
import re
import pytube  
from pytube import Playlist
from pytube import YouTube


YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR ='/home/usama/Documents/isl'

#ADD playlist URL 
playlist = Playlist('https://www.youtube.com/playlist?list=PLCu0Ci-4EKuCNdaQM4UkVhG8rj8xVwzZN	')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))
#Download Video Files
for url in playlist.video_urls:
    print(url)
    try:
        youtube = pytube.YouTube(url)  
        video = youtube.streams.first()
        print(youtube.title)
        video.download(DOWNLOAD_DIR)
    except:
    	print("ERRORR" )
# physically downloading the audio track
#for video in playlist.videos:
 #   audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
  #  audioStream.download(output_path=DOWNLOAD_DIR)
   # print("MOVING")

print("DONE")
