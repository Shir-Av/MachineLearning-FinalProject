import numpy as np


def write_file(data, labels, file_name):
    data_to_write = ''
    for index in range(len(data)):
        data_to_write += str(data[index]) + ' @@@ ' + labels[index] + '\n'

    # np.save(file_name, data_to_write)

    f = open(file_name+".txt", "w")
    f.write(data_to_write)
    f.close()
    print('write successfully')


