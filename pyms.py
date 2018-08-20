import sys

import click

import vray_depth_calc_ImageIO


@click.command()
@click.argument("path")
def cli(path):
    # click.echo("path: (%s)" % path)
    vray_depth_calc_ImageIO.test(path)

if getattr(sys, 'frozen', False):
    cli(sys.argv[1:])
