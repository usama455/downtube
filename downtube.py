# # A Python Script to Download 
# import re
# import pytube  
# from pytube import Playlist
# from pytube import YouTube


# YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
# DOWNLOAD_DIR ='/Users/usama/Documents/docs/justForFun/downtube'

# #ADD playlist URL 
# playlist = Playlist('https://www.youtube.com/playlist?list=PLSRoq0WroQEcsuSqVDOGPfDKbZNfL66Cw')

# # this fixes the empty playlist.videos list
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

# print(len(playlist))
# #Download Video Files
# # for url in playlist.video_urls:
# #     print(url)
# #     try:
# #         youtube = pytube.YouTube(url)  
# #         video = youtube.streams.first()
# #         print(youtube.title)
# #         video.download(DOWNLOAD_DIR)
# #     except:
# #     	print("ERRORR" )
# # physically downloading the audio track
# for video in playlist.videos:
#    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
#    if audioStream:
#       audioStream.download(output_path=DOWNLOAD_DIR)
#       print("MOVING")
#    else:
#       print("No audio stream found for this video.")

# print("DONE")

import yt_dlp

# Input the URL of the YouTube playlist
playlist_url = 'https://www.youtube.com/playlist?list=PLSRoq0WroQEf9-je_CxotXMKl-xgqqHz_'

# Output directory where the MP3 files will be saved
output_directory = "./downloaded_songs"

# Create options for downloading audio as MP3
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
}

# Create a YouTube downloader instance using yt-dlp
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("Download completed. Check the 'downloaded_songs' directory for your MP3 files.")
