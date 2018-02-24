#!python
import tools

file_name = "../data/train.csv"


count_labels = {}

with open(file_name, 'r') as f:
    f.next()

    for l in f:
        line = tools.read_line_image(l)

        img, label = tools.transform_array_to_labeled_matrix(line)

        if label in count_labels:
            count_labels[label] += 1
        else:
            count_labels[label] = 1


print count_labels



