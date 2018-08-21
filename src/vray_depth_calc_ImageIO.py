import OpenEXR

import array

import math

import imageio


def test(path_dist, path_alpha):
    imageio.plugins.freeimage.download()

    img_dist = imageio.imread(path_dist)
    img_alpha_list = list(imageio.imread(path_alpha).flat)

    min_dist = math.inf
    max_dist = -math.inf

    for idx, dist_val in enumerate(img_dist.flat):
        if img_alpha_list[idx] > 0:
            max_dist = dist_val if dist_val > max_dist else max_dist
            min_dist = dist_val if dist_val < min_dist else min_dist

    print(min_dist, max_dist)


# test.py("assets/VrayZdepthCalculator_RGB.exr", "assets/VrayZdepthCalculator_A.exr")
