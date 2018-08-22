import sys

import click

import vray_depth_calc_PyEXR


@click.command()
@click.argument("path")
def cli(path):
    try:
        click.echo(">>> path: (%s)" % path)
        vray_depth_calc_PyEXR.output_min_max("assets/VrayZdepthCalculator_RGBA.exr")
    except BaseException as e:
        click.echo(e)


if getattr(sys, 'frozen', False):
    cli(sys.argv[1:])
else:
    vray_depth_calc_PyEXR.output_min_max("assets/VrayZdepthCalculator_RGBA.exr")
