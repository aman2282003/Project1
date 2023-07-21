from pytube import YouTube       # to run this install pytube
link = input("Enter the video link")
youtube_1 = YouTube(link)
# for downloading title of video
# print(youtube_1.title)
# for downloading thumbanil pic of video
# print(youtube_1.thumbnail_url)
# videos = youtube_1.streams.filter(only_audio=True)   for downloading only audio
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()


strm = int(input("Enter the option:"))
videos[strm].download()
print("downloaded sucessfully")
