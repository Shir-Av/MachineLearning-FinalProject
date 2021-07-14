import itertools

import numpy as np




import algorithms
from audio_handler import label_encoder_for_test, label_encoder, get_feature_vector_25
from combined_handler import cut_a_single_record

import load_data


def run():


    data_files, data_labels = load_data.load_data_from_file('Marine-Mammal-25.txt')


    record_name = 'spinner-and-stripted'
    test_files, test_labels = cut_a_single_record(f'./clf_classes/{record_name}')
    print(test_files)
    print(test_labels)


    #
    train_classes, encoded_classes = label_encoder(data_labels)
    test_classes = label_encoder_for_test(encoded_classes, test_labels)

    test_set = get_feature_vector_25(test_files)


    algorithms.svm_combined_clf(data_files, train_classes, test_set, test_labels, encoded_classes)
    algorithms.rf_combined_clf(data_files, train_classes, test_set, test_labels, encoded_classes)
    algorithms.knn_combined_clf(data_files, train_classes, test_set, test_labels, encoded_classes)