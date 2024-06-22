"""
    Author: Sloth
    Date: 6/19/2024
    Description: Script that uses Robocopy to move all ROMS to a hard drive as a backup.
"""

from subprocess import call
from os import listdir, makedirs

def main() -> None:
    copy_roms(r"F:\Emulation\roms", r"D:\roms")
    copy_bios(r"F:\Emulation\bios", r"D:\bios")


def copy_roms(source: str, destination: str) -> None:
    folders: list[str] = [
        source + r"\n3ds",
        source + r"\nds",
        source + r"\psx",
        source + r"\ps2",
        source + r"\ps3",
        source + r"\switch",
        source + r"\wii",
        source + r"\xbox360"
    ]

    for folder in folders:
        folder_name: str = folder.split('\\')[-1]
        destination_folder: str = fr"{destination}\{folder_name}"
        makedirs(destination_folder)
        files: listdir = listdir(folder)
        for file in files:
            if (file != "metadata.txt" and file != "systeminfo.txt"):
                robocopy(folder, destination_folder, file)


def copy_bios(source: str, destination: str) -> None:
    makedirs(destination)
    robocopy(source, destination, "*")


def robocopy(source: str, destination: str, file: str) -> None:
    if file == "*":
        file = "*.*"
        
    call(["robocopy", source, destination, file, "/COPY:DAT", "/DCOPY:DAT", "/E"])


if __name__ == '__main__':
    main()