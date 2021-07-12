from youtube_dl import YoutubeDL
import promptlib
import threading
import eel
import os

eel.init("web")


def convert(path):
    file = os.listdir(path)
    for f in file:
        if f[-1] == "4":
            f = path + r"/" + f
            new_name = list(f)
            new_name[-1] = "3"
            new_name = "".join(new_name)

            mp4_file = f
            mp3_file = new_name
            videoclip = VideoFileClip(mp4_file)
            audioclip = videoclip.audio
            audioclip.write_audiofile(mp3_file)
            audioclip.close()
            videoclip.close()

    for f in file:
        if f[-1] == "4":
            new_path = path + r"/" + f
            os.remove(new_path)
    eel.enable_btn()


first_run = True


def download(link, vid_type):
    global first_run
    if first_run:
        path = "web/music"
        path = os.getcwd() + "/" + path
        first_run = False
    else:
        path = os.getcwd()

    try:
        if not os.path.isdir(path):
            os.mkdir(path)
        os.chdir(path)
        path = os.getcwd()
        ydl = YoutubeDL()
        ydl.add_default_info_extractors()
        ydl.extract_info(link, download=True)

        if vid_type == "mp4":
            eel.enable_btn()

    except:
        eel.warning("Please double check your parameters")
        eel.enable_btn()
        return

    if vid_type == "mp3":
        convert(path)


@eel.expose
def get_data_py(link, vid_type):
    download(link, vid_type)

@eel.expose
def select_directory():
    prompter = promptlib.Files()
    dir = prompter.dir()
    warning = True
    if dir == "":
        eel.warning("No file selected")
        pass
    else:
        for file in os.listdir(dir):
            if file[-3:] == "mp3" or file[-3:] == "mp4":
                warning = False
                eel.receive_path(dir)
                break
        if warning:
            eel.warning("Could not find suitable file to play (mp3 or mp4)")


eel.start("index.html")
