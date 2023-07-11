# MediaArchiver

## Description
MediaArchiver is a very simple tool that given a directory containing different photos or videos moves them into another directory and sorts them in subdirectories, one for each month and year.

In other words from a directory of your choice that contains (for example) some photos taken in October 2022 and some others in July 2023 you will end up, after choosing your desired directory of destination, with two subdirectories: "2022" and "2023", and each of them will have a subdirectory: "October" and "July" respectively.

## Usage
**First:** run the script

```bash
python3 main.py
```

**Second:** (following instructions on the screen): Copy-paste the **absolute** path to the directory where the medias are located, as the script is asking you to do

**Third:** (following instructions on the screen): Choose wheter to create a subdirectory for each year, month and day or only for each year and month

**Fourth:** (following instructions on the screen): Copy-paste the **absolute** path to the directory where you want the medias to be stored in the end. Keep in mind that a bunch of different subdirectories will be created.

**DONE!**

## Further improvements
- Improve "user-friendly-ness" for specifying the directories

- Add GUI

## Mind that
This tool has been written in a very short time, don't expect it to be caring of user-related errors (e.g.: specifying one of the two paths) or to be very user-friendly. 
It is not guaranteed that any of the improvements above will be made.
