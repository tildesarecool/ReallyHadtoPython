# this is a simple script from youtube video
# https://www.youtube.com/watch?v=zT7niRUOs9o
# which I'm adapting and customizing:
# 0. convert entirely to CLI-based operation for inputting URL/download location
# 1. overly simplistic progress bar (print a # every second)
# 2. paste in youtube url when prompted
# 3. paste in download path
# 3a default to a downlaod folder if none is specified based environment variables e.g. %userprofile%\Downloads folder versus hard absolute path (done except env variable based)
# 4. save settings (?)
# 5. point at txt file with list of URLs to queue download (and/or downlaod multiple videos at once)
# 6. make sure to print out file name of downloaded mp4 file and/or final path. maybe absolute path. - done mostly
# 7. offer to open download folder location to get to that new mp4 file in explorer
# 8. put in extra cli option to "turn on verbose mode" or debugging or whatever - this displays values of the exceptions
# x. no idea how but add playlist downlaod support

# pip install pytube
from pytube import YouTube as yt
import os
# import time

#CURDIR = os.getcwd()
#get_is_dir = os.path.isdir(curdir)
#determine_if_path_exists = os.path.exists(curdir)

# I'm going to try and make a CLI version, no tkinter

ENV_VAR_UPROFILE = os.environ['USERPROFILE']
DOWNLOADS_FOLDER = "\Downloads"
DEFAULT_DL_DIR = ENV_VAR_UPROFILE + DOWNLOADS_FOLDER


def validate_path(path):
    # dir_path = input(f"Enter path or leave blank for default ({DEFAULT_DL_DIR}): ").strip()     # strip/trim out any extra spaces at start/ending of string
    try:
        if os.path.isdir(path) and os.path.exists(path):
            return path
    except Exception as e:
        print(f"Invalid path: {path}")
        exit()


def validate_url(url):
    try:
        yt(url)
        return True
            #yturl = yt(url)
#        print(yturl)
    except Exception as e:
        print(f"via validate_url - error is: {e}")
        print(f"also via validate_url - there's been an exception")
        return False

def download_video(url, save_path):
    if validate_url(url) and validate_path(save_path):
        yturl = yt(url)
        streams = yturl.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        file_info = highest_res_stream.download(output_path=save_path)
        
        print("Video downloaded successfully!")
        print(f"download path is {save_path}")
        print(f"Video downloaded to \"{save_path}\\{highest_res_stream.default_filename}\" ")
        
        # print(f"The value that highest_res_stream.download(output_path=save_path) returns is {highest_res_stream.download(output_path=save_path)}")
        print(f"The value that highest_res_stream.download(output_path=save_path) returns is {file_info}")
        print(f"value of highest_res_stream.exists_at_path() is {highest_res_stream.exists_at_path(file_info)}")
    else:
        print("via download_video - invalid url")
        return        

def get_downloads_path():
    
    if validate_path(DEFAULT_DL_DIR):    
        dir_path = input(f"Enter path or leave blank for default ({DEFAULT_DL_DIR}): ").strip()     # strip/trim out any extra spaces at start/ending of string
        if dir_path == "":
            dir_path = DEFAULT_DL_DIR
        try:
            if os.path.isdir(dir_path) and os.path.exists(dir_path):
                print(f"Download folder: {dir_path}")
                return dir_path
        except Exception as e:
            print(f"Via get_downloads_path - The error is: {e}")
    else:
        print("Invalid path")
        exit()

def get_video_url():
    #vidurl = input("Enter URL: ").strip()     # strip/trim out any extra spaces at start/ending of string
    vidurl = "https://www.youtube.com/watch?v=zT7niRUOs9o"
    if not validate_url(vidurl):
        #print("invalid url")
        return
    try:
        print(f"Downloading video URL {vidurl} as mp4 at highest value")
        return vidurl
    except Exception as e:
        print(f"via get_video_url, The error is: {e}")

if __name__ == '__main__':
    downloadpath_value = get_downloads_path()
    vurl = get_video_url()
    #print(f"the determination is that curdir is a folder, answer is {get_is_dir}")
    #print(f"does curdir exist ? - answer is {determine_if_path_exists}")
    #print(f"value returned from downloads path is {downloadpath_value}")
    #print(f"value returned from get_video_url() is {vurl}")
    download_video(vurl, downloadpath_value)
    #pass

