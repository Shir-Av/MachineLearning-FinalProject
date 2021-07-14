import fnmatch
import os


def load_data_by_animal_type(type_a='Marine-Mammal', type_b='Birds', path='./data-set/'):
    path_a = path + type_a + '/'
    path_b = path + type_b + '/'

    data_files = []
    data_labels = []

    for root, dirnames, filenames in os.walk(path_a):
        for filename in fnmatch.filter(filenames, '*.wav'):
            data_files.append(os.path.join(root, filename))
            data_labels.append(type_a)

    for root, dirnames, filenames in os.walk(path_b):
        for filename in fnmatch.filter(filenames, '*.wav'):
            data_files.append(os.path.join(root, filename))
            data_labels.append(type_b)

    print("found %d audio files in %s" % (len(data_files), data_labels))

    return [data_files, data_labels]

def load_data_by_species(type, path='./data-set/'):
    path = path + type + '/'

    data_files = []
    data_labels = []

    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.wav'):
            temp = root.split('/')
            label = temp[len(temp) - 1]

            data_files.append(os.path.join(root, filename))
            data_labels.append(label)

    print("found %d audio files in %s" % (len(data_files), data_labels))

    return [data_files, data_labels]


def load_data_from_file(filename):
    train_set = []
    train_labels = []
    with open(filename, 'r') as file_handle:
        vector = []
        for v in file_handle:
            if v.strip().__contains__(' @@@ '):
                split = v.split(' @@@ ')
                label = split[len(split) - 1].strip()
                train_labels.append(label)

                splited_numbers = split[0].split(' ')
                for num in splited_numbers:

                    num = num.replace('[', '').replace(']', '').replace(',', '')
                    if num == '':
                        continue
                    vector.append(float(num))
                train_set.append(vector)
                vector = []
            else:
                sp = v.split()
                for num in sp:
                    num = num.replace('[', '').replace(']', '').replace(',', '')
                    if num == '':
                        continue
                    vector.append(float(num))

    return [train_set, train_labels]





