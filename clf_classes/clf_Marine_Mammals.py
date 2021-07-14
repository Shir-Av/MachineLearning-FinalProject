from sklearn.model_selection import train_test_split

import algorithms
import audio_handler
import load_data
from write_file import write_file


def run(vector_size):

    # data_files, data_labels = load_data.load_data_by_species(type="Marine-Mammal")
    # X = audio_handler.get_feature_vector_2(data_files)
    # write_file(X, data_labels, '')

    if vector_size == 13:
        data_files, data_labels = load_data.load_data_from_file('Marine-Mammal-13.txt')
    elif vector_size == 25:
        data_files, data_labels = load_data.load_data_from_file('Marine-Mammal-25.txt')
    else:
        return

    train_set, test_set, train_labels, test_labels = train_test_split(data_files, data_labels, test_size=0.20)

    train_classes, encoded_classes = audio_handler.label_encoder(train_labels)
    test_classes = audio_handler.label_encoder_for_test(encoded_classes, test_labels)

    algorithms.knn(train_set, train_classes, test_set, test_classes, encoded_classes)
    algorithms.random_forest(train_set, train_classes, test_set, test_classes, encoded_classes)
    algorithms.svm(train_set, train_classes, test_set, test_classes, encoded_classes)
    algorithms.pca(train_set, train_classes, test_set, test_classes, encoded_classes)



