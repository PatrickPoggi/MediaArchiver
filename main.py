# This is a sample Python script.
import collections
import os
import queue
import shutil
import datetime

medias = []
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November","December"]

def is_media(entry):
    # Check if it is a media of any kind, particularly video or photo shot on iPhone.
    extension = "." + entry.name.split(".")[-1].lower()
    media_extensions = [
        ".mp4", ".mkv", ".avi", ".mov", ".jpg", ".png", ".heic", ".jpeg", ".gif", ".bmp", ".aae",
        ".m4v", ".mpg", ".mpeg", ".3gp", ".3g2", ".m2v", ".m4v", ".m2ts", ".mts", ".flv", ".f4v",
        ".wmv", ".vob", ".webm", ".ts", ".mxf", ".m2p", ".mod", ".tod", ".mpe", ".mpv", ".mp2",
        ".mp3", ".wav", ".aac", ".wma", ".flac", ".alac", ".amr", ".ogg", ".oga", ".opus",
        ".ac3", ".eac3", ".dts", ".dtshd", ".mpa", ".mka", ".tta", ".aiff", ".aif", ".aifc",
        ".ape", ".mac", ".spx", ".ra", ".wv", ".wvc", ".m4a", ".m4b", ".m4p", ".m4r", ".3ga",
        ".adt", ".adts", ".caf", ".qcp", ".wave", ".wave64", ".bwf"
    ]
    return extension in media_extensions


def locate_medias():
    print("Please tell me where your medias are located as an absolute path: ")
    dirs = []
    path = input()
    dirs.append(path)
    print("You entered: " + path)
    print("Now I will try to locate all your medias in this path...")
    while len(dirs) > 0:
        path = dirs.pop()
        # print("Now I am in path: " + path)
        try:
            dir_entries = os.scandir(path)
        except PermissionError:
            print("Permission denied: " + path)
            continue
        else:
            for entry in dir_entries:
                if entry.is_dir():
                    dirs.append(entry.path)
                else:
                    if is_media(entry):
                        medias.append(entry)
            # At this point we have 2 data structures, media and paths
    # Out of the loop, we have all the medias in the medias list
    print("Found " + str(len(medias)) + " medias in total.")


def manage_medias(dest_root):
    ''' Iterate over all medias and sort them into folders according to their creation date: we want to create a folder
    for each year and month or for every year, month and day depending on the user's choice. '''
    choice = "0";
    while choice not in ["1", "2"]:
        choice = input("Would you like to sort your medias by"+
                       "\n\t(1) - Year and month\n\tor by\n\t(2) - Year, month and day?\n")
        print("You entered: " + choice)
    dir_to_create = []
    for media in medias:
        # assert media.isinstance(os.dirEntry)
        # Get the creation date of the media
        creation_date = media.stat().st_birthtime
        # Convert the creation date to a datetime object
        creation_date = datetime.datetime.fromtimestamp(creation_date)
        # Get the year, month and day of the creation date
        year = creation_date.year
        month = creation_date.month
        day = creation_date.day
        # Check if the year folder already exists
        if not os.path.exists(dest_root + "/" + str(year)) and not dest_root + "/" + str(year) in dir_to_create:
            dir_to_create.append(dest_root + "/" + str(year))
        # Check if the month folder already exists
        if not os.path.exists(dest_root + "/" + str(year) + "/" + months[month - 1]) \
                and not dest_root + "/" + str(year) + "/" + months[month - 1] in dir_to_create:
            dir_to_create.append(dest_root + "/" + str(year) + "/" + months[month - 1])
        if choice == "2":
            # Check if the day folder already exists
            if not os.path.exists(dest_root + "/" + str(year) + "/" + months[month-1] + "/" + str(day)) \
                    and not dest_root + "/" + str(year) + "/" + months[month-1] + "/" + str(day) in dir_to_create:
                dir_to_create.append(dest_root + "/" + str(year) + "/" + months[month-1] + "/" + str(day))

    # Now we have all the directories to create in the dir_to_create list
    # We can create them
    for dir in dir_to_create:
        if not os.path.exists(dir):
            os.mkdir(dir)
    # Now we can move the medias
    for media in medias:
        # assert media.isinstance(os.dirEntry)
        # Get the creation date of the media
        creation_date = media.stat().st_birthtime
        # Convert the creation date to a datetime object
        creation_date = datetime.datetime.fromtimestamp(creation_date)
        # Get the year, month and day of the creation date
        year = creation_date.year
        month = creation_date.month
        day = creation_date.day
        # Move the media to the right folder
        if choice == "1":
            print("Moving " + media.path + " to " + dest_root + "/" + str(year) + "/" + months[month-1])
            # shutil.move(media.path, dest_root + "/" + str(year) + "/" + str(month))
            shutil.move(media.path, os.path.join(dest_root, str(year), months[month-1], media.name))
        else:
            print("Moving " + media.path + " to " + dest_root + "/" + str(year) + "/" + months[month-1] + "/" + str(day))
            # shutil.move(media.path, dest_root + "/" + str(year) + "/" + str(month) + "/" + str(day))
            shutil.move(media.path, os.path.join(dest_root, str(year), months[month-1], str(day), media.name))


if __name__ == '__main__':
    print('MediaArchiver started...')
    locate_medias()
    dest_root = input("Please tell me the root directory where you want to store your medias\n: ")
    # Now we have all the medias in the medias list
    manage_medias(dest_root) # This will create the folders and move the medias
    print("MediaArchiver finished.")
