import configparser
import math

import pyexr


def output_min_max(path: str):
    config = configparser.ConfigParser()
    config['VRAY_DEPTH_CALC'] = exr_with_alpha(path)

    with open("PyMs.ini", "w") as f:
        config.write(f)


def exr_with_alpha(path: str):
    exr = pyexr.open(path)

    dist_list = exr.get("B").flatten().astype(float)
    alpha_list = exr.get("A", precision=pyexr.UINT).flatten().astype(float)

    min_dist = math.inf
    max_dist = -math.inf

    for idx, dist_val in enumerate(dist_list):
        if alpha_list[idx] != 0:
            max_dist = dist_val if dist_val > max_dist else max_dist
            min_dist = dist_val if dist_val < min_dist else min_dist

    return {'min': abs(max_dist), 'max': abs(min_dist)}
