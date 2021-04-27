import pytube
import os
import pathlib

def download_folder():
    return os.path.join(pathlib.Path().home(), 'Downloads')

os.system("cls")
url = input("Input URL: ") 
video = pytube.YouTube(url)
 
stream = video.streams.get_by_itag(140)
os.system("cls")
print("Downloading ...")
stream.download(output_path=download_folder())
print(f"\nFile Saved in: {str(download_folder())}")
