"""
    Author: Sloth
    Date: 6/22/2024
    Description: Script that uses Robocopy to move all backed-up ROMS/BIOS files to an SD-Card.
"""

from subprocess import call
from os import listdir


def main() -> None:
    copy_roms(r"D:\roms", r"F:\Emulation\roms")
    copy_bios(r"D:\bios", r"F:\Emulation\bios")


def copy_roms(source: str, destination_folder: str) -> None:
    consoles: listdir = listdir(source)
    for console in consoles:
        console_destination = fr"{destination_folder}\{console}"
        console_source = fr"{source}\{console}"
        robocopy(console_source, console_destination)


def copy_bios(source: str, destination: str) -> None:
    robocopy(source, destination)


def robocopy(source: str, destination: str) -> None:
    call(["robocopy", source, destination, "*.*", "/COPY:DAT", "/DCOPY:DAT", "/E"])

if __name__ == '__main__':
    main()