from pytubefix import YouTube

yt_url = input("Enter ytURL: ")
yt = YouTube(yt_url)

stream = yt.streams.get_audio_only()
print(stream.title)
print("Downloading...")

vid_dir = r'C:\Users\user\Documents\Rockstar Games\GTA V\User Music'
if stream:
    stream.download(output_path=vid_dir, mp3=True)
    print('Download successful!')
else:
    print('Download failed!')