import sys

import click
import pyexr

import vray_depth_PyEXR


@click.command()
@click.argument("what_to_do")
@click.option("-o1", "--option1")
@click.option("-o2", "--option2")
def cli(what_to_do: str, option1, option2):
    click.echo(f">>> PyMs.exe {what_to_do} -{option1} -{option2}")

    if what_to_do == "vray_depth":
        vray_depth_PyEXR.write_to_file(option1, option2)


if getattr(sys, 'frozen', False):
    cli(sys.argv[1:])
else:
    # this code executes only if not run from frozen EXE
    vray_depth_PyEXR.write_to_file("C:/Users/pawelgrze/AppData/Local/Autodesk/3dsMax/2017 - 64bit/ENU/temp/vray_depth.exr", "PyMs.ini")
    # exr = pyexr.open("C:/Users/pawelgrze/AppData/Local/Autodesk/3dsMax/2017 - 64bit/ENU/temp/vray_depth.exr")
    # print(exr.channels)
