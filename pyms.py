import sys

import click

import vray_depth_calc_OpenEXR


@click.command()
@click.argument("path")
def cli(path):
    # click.echo("path: (%s)" % path)
    # vray_depth_calc_ImageIO.test(path)
    try:
        vray_depth_calc_OpenEXR.exr_with_alpha(path)
    except BaseException as e:
        click.echo(e)


if getattr(sys, 'frozen', False):
    cli(sys.argv[1:])
else:
    vray_depth_calc_OpenEXR.exr_with_alpha("assets/VrayZdepthCalculator_RGBA.exr")


