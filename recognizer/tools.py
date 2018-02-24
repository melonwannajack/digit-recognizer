#!python
from PIL import Image
import numpy as np


def transform_array_to_labeled_matrix(array, shape=28):
    label = None
    if len(array) == shape * shape + 1:
        label = array[0]
        array = array[1:]
    img = np.array(array).reshape(shape, shape)
    return img, label


def read_line_image(line):
    return map(int, line.split(','))


def show_string_as_image(line):
    line_array = read_line_image(line)
    matrix, label = transform_array_to_labeled_matrix(line_array)
    image = Image.fromarray(matrix.astype('uint8'))
    image.show()
