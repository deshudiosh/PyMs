import configparser
import math

import pyexr


def write_to_file(exr_path: str, result_file_path: str):
    config = configparser.ConfigParser()
    config['vray_depth'] = exr_with_alpha(exr_path)

    with open(result_file_path, "w") as f:
        config.write(f)


def exr_with_alpha(path: str):
    exr = pyexr.open(path)

    dist_list = exr.get("PG.VrayDepthCalculator.B").flatten().astype(float)
    alpha_list = exr.get("A", precision=pyexr.UINT).flatten().astype(float)

    min_dist = math.inf
    max_dist = -math.inf

    for idx, dist_val in enumerate(dist_list):
        if alpha_list[idx] != 0:
            max_dist = dist_val if dist_val > max_dist else max_dist
            min_dist = dist_val if dist_val < min_dist else min_dist

    return {'min': abs(max_dist), 'max': abs(min_dist)}
