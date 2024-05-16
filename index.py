from functions.youtube import *

class WebDownloaderMenu():
    def __init__(self):
        self.ShowMenu()
    
    def ShowMenu(self):
        options = [
            "1. Youtube",
            "2. Facebook",
            "3. Twitter",
            "4. Instagram"
        ]
        print("Select the Plataform")
        for i in options:
            print(i)
        select = int(input("\n"))

        if select == 1:
            self.YouTubeOption()

    def YouTubeOption(self):
        options = [
            "1. Video",
            "2. Music"
        ]
        print("\nWhat do you want to download?")
        for i in options:
            print(i)
        select = int(input("\n"))

        if select == 1:
            url = str(input("\nPaste here the link of the video:\n"))
            quality_list = GetVideoQuality(url)
            print("\nChoose the resolution you want it:")
            n=1
            for i in quality_list:
                print(f"{n}. {i['resolution']}")
                n+=1
            res = int(input("\n"))
            print(f"\nYou have chosen {quality_list[res-1]['resolution']}.")
            namefile = str(input("\nEnter a name for the file:\n"))
            VideoDownload_mp4(url, quality_list[res-1]['resolution'], namefile)

        elif select == 2:
            url = str(input("\nPaste here the link of the video:\n"))
            name = str(input("\nEnter a name for the file:\n"))
            VideoDownload_mp3(url, name)
    
    def FacebookOption(self):
        pass

    def TwitterOption(self):
        pass

    def InstagramOption(self):
        pass

    def StayOrLeave(self):
        pass

start = WebDownloaderMenu()