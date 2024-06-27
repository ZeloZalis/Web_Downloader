from functions.youtube import *

class WebDownloaderMenu():
    def __init__(self):
        self.showMenu()
    
    def showMenu(self):
        OPTIONS = [
            "1. Youtube",
            "2. Facebook",
            "3. Twitter",
            "4. Instagram"
        ]
        print("Select the Plataform")
        for i in OPTIONS:
            print(i)
        select = int(input("\n"))

        if select == 1:
            self.youtubeOption()

    def youtubeOption(self):
        OPTIONS = [
            "1. Video",
            "2. Music"
        ]
        print("\nWhat do you want to download?")
        for i in OPTIONS:
            print(i)
        select = int(input("\n"))

        if select == 1:
            url = str(input("\nPaste here the link of the video:\n"))
            quality_list = get_video_quality(url)
            print("\nChoose the resolution you want it:")
            n = 1
            for i in quality_list:
                print(f"{n}. {i['resolution']}")
                n += 1
            res = int(input("\n"))
            print(f"\nYou have chosen {quality_list[res-1]['resolution']}.")
            file_name = str(input("\nEnter a name for the file:\n"))
            video_download_mp4(url, quality_list[res-1]['resolution'], file_name)

        elif select == 2:
            url = str(input("\nPaste here the link of the video:\n"))
            name = str(input("\nEnter a name for the file:\n"))
            video_download_mp3(url, name)
    
    def facebookOption(self):
        pass

    def twitterOption(self):
        pass

    def instagramOption(self):
        pass

    def stay_or_leave(self):
        pass

start = WebDownloaderMenu()