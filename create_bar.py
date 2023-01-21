import os
import shutil
import imageio.v2 as imageio
import numpy as np


def find_bright_mixed(rgb):
    return [int(rgb[0]//1.4), int(rgb[1]//1.4), int(rgb[2]//1.4)]


def assign_colors(colors):
    return [colors[0], find_bright_mixed(colors[1]), colors[2]]


def create_png(pixels, intersection, colors, image_stack):
    color_arr = assign_colors(colors)
    base_color = color_arr[0]
    mixed_color = color_arr[1]
    secondary_color = color_arr[2]

    data = np.full((1, pixels, 3), fill_value=base_color, dtype=np.uint8)
    py_path = os.path.abspath(__file__)
    py_dir = os.path.dirname(py_path)
    py_dir_tmp = py_dir + "\\tmp\\"
    os.chdir(py_dir)

    try:
        os.mkdir('tmp')
    except FileExistsError:
        print("""
            
            exception FileExistsError: Folder already exists!
            Program did not shutdown gracefully on last run!

            """)
    for i in range(0, pixels+intersection):
        if i < pixels:
            data[0, i] = secondary_color
            if i < pixels-2:
                data[0, i+1] = mixed_color
                data[0, i+2] = mixed_color

            if i > intersection:
                data[0, i-(intersection-1)] = mixed_color
                data[0, i-intersection] = mixed_color
                data[0, i-(intersection+1)] = base_color
        else:
            remainder = i-intersection
            data[0, remainder-1] = base_color
            data[0, remainder] = mixed_color
        if not i % 10:
            new_image = py_dir_tmp + str(i+1) + ".png"
            imageio.imwrite(new_image, data)
            image_stack.append(imageio.imread(new_image))


def stitch_gif(filename, image_stack):
    imageio.mimsave(filename, image_stack, format='GIF', duration=0.015)


def cleanup():
    shutil.rmtree('tmp')


def create_bar(pixels, colors, intersection, filename):
    image_stack = []
    create_png(pixels, intersection, colors, image_stack)
    stitch_gif(filename, image_stack)
    cleanup()
