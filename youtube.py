import pytube
from pytube import YouTube,Playlist
print("*****Welcome to YouTube Downloader*****")
print("***************************************")
print("YouTube video-->press 1")
print("YouTube PlayList-->press 2")
print("For exit-->press 3")
y=int(input("Enter here:"))

if(y==1):
    link=input("please input any youtube link:")
    youtube_1=YouTube(link)
    print(youtube_1.title)
    print(youtube_1.thumbnail_url)
    videos=youtube_1.streams.all()
#for audio
#videos=youtube_1.streams.filter(only_audio=True)
    vid=list(enumerate(videos))
    for i in vid:
        print(i)
    print()
    strm=int(input("enter:"))
    videos[strm].download()
    print("successfully")

#playlist
elif(y==2):
    link = input("please input youtube Playlist link:")
    py = Playlist("link")
    print(f'Downloading:{py.title}')
    for video in py.videos:
        video.streams.first().download()
    print("***successfully Downloaded***")
    print("Thank you")
else:
    print("byyy")