import OpenEXR


def exr_with_alpha(path: str):
    exr = OpenEXR.InputFile(path)
    (alpha_list, dist_list) = exr.channels("AB")

    alpha_list = array.array('f', alpha_list)
    dist_list = array.array('f', dist_list)

    min_dist = math.inf
    max_dist = -math.inf

    for idx, dist_val in enumerate(dist_list):
        if alpha_list[idx] != 0:
            max_dist = dist_val if dist_val > max_dist else max_dist
            min_dist = dist_val if dist_val < min_dist else min_dist

    print(min_dist, max_dist)


def exr_without_alpha(path: str):
    exr = OpenEXR.InputFile(path)
    dist_list = exr.channel("B")

    dist_list = array.array('f', dist_list)

    min_dist = math.inf
    max_dist = -math.inf

    for dist_val in dist_list:
        max_dist = dist_val if dist_val > max_dist else max_dist
        min_dist = dist_val if dist_val < min_dist else min_dist

    print(min_dist, max_dist)