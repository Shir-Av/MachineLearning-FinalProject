import itertools
import warnings

import numpy as np
import math
from collections import Counter

import matplotlib.pyplot as plt
from sklearn import svm

from sklearn.metrics import recall_score, precision_score, accuracy_score, r2_score
from sklearn.metrics import confusion_matrix, f1_score, classification_report

# KNN
from sklearn.neighbors import KNeighborsClassifier

# SVM
from sklearn.svm import LinearSVC, SVC
import joblib

# PCA
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

# Random Forest
from sklearn.ensemble import RandomForestClassifier



def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.PuRd, rotation=45):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    """
    # print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=rotation)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


# ------------------------------------------------ KNN ------------------------------------------------
def knn(train_set, train_classes, test_set, test_classes, encoded_classes):
    # Machine Learning Parameters
    n_neighbors = 1  # Number of neighbors for kNN Classifier

    # KNN Classifier
    model_knn = KNeighborsClassifier(n_neighbors=n_neighbors)

    # kNN
    model_knn.fit(train_set, train_classes)

    # Predict using the Test Set
    predicted_labels = model_knn.predict(test_set)

    print('------------------------ KNN - Results ------------------------')
    # Recall - the ability of the classifier to find all the positive samples
    print("Recall: ", recall_score(test_classes, predicted_labels, average=None, zero_division=1))

    # Precision - The precision is intuitively the ability of the classifier not to
    # label as positive a sample that is negative
    print("Precision: ", precision_score(test_classes, predicted_labels, average=None, zero_division=1))

    # F1-Score - The F1 score can be interpreted as a weighted average of the precision
    # and recall
    print("F1-Score: ", f1_score(test_classes, predicted_labels, average=None, zero_division=1))

    # Accuracy - the number of correctly classified samples
    print("Accuracy: %.2f  ," % accuracy_score(test_classes, predicted_labels, normalize=True),
          accuracy_score(test_classes, predicted_labels, normalize=False))
    print("Number of samples:", test_classes.shape[0])
    print()

    # Compute confusion matrix
    cnf_matrix = confusion_matrix(test_classes, predicted_labels)
    np.set_printoptions(precision=2)

    rotation = 45
    if len(encoded_classes) > 18:
        rotation = 90
    # Plot non-normalized confusion matrix
    plt.figure(figsize=(18, 13))
    plot_confusion_matrix(cnf_matrix, classes=encoded_classes,
                          title='KNN', rotation=rotation)


# ------------------------------------------------ SVM ------------------------------------------------
def svm(train_set, train_classes, test_set, test_classes, encoded_classes):
    # model_svm = LinearSVC(random_state=0, tol=1e-5, max_iter=5000)
    svclassifier = SVC(kernel='rbf', C=10.0, gamma=0.1)

    # SVM

    svclassifier.fit(train_set, train_classes)

    # Predict using the Test Set

    predicted_labels = svclassifier.predict(test_set)

    print('------------------------ SVM - Results ------------------------')
    # Recall - the ability of the classifier to find all the positive samples
    print("Recall: ", recall_score(test_classes, predicted_labels, average=None, zero_division=1))

    # Precision - The precision is intuitively the ability of the classifier not to
    # label as positive a sample that is negative
    print("Precision: ", precision_score(test_classes, predicted_labels, average=None, zero_division=1))

    # F1-Score - The F1 score can be interpreted as a weighted average of the precision
    # and recall
    print("F1-Score: ", f1_score(test_classes, predicted_labels, average=None, zero_division=1))

    # Accuracy - the number of correctly classified samples
    print("Accuracy: %.2f  ," % accuracy_score(test_classes, predicted_labels, normalize=True),
          accuracy_score(test_classes, predicted_labels, normalize=False))
    print("Number of samples:", test_classes.shape[0])
    print()
    # Compute confusion matrix
    cnf_matrix = confusion_matrix(test_classes, predicted_labels)
    np.set_printoptions(precision=2)

    rotation = 45
    if len(encoded_classes) > 18:
        rotation = 90
    # Plot non-normalized confusion matrix
    plt.figure(figsize=(18, 13))
    plot_confusion_matrix(cnf_matrix, classes=encoded_classes,
                          title='SVM', rotation=rotation)


# ------------------------------------------------ PCA ------------------------------------------------
def pca(train_set, train_classes, test_set, test_classes, encoded_classes):
    X = scale(train_set)
    y = scale(test_set)
    pca = PCA(n_components=5)
    train_set = pca.fit_transform(X)
    test_set = pca.transform(y)

    # model_svm = LinearSVC(random_state=0, tol=1e-5, max_iter=5000)
    svclassifier = SVC(kernel='rbf', C=10.0, gamma=0.1)

    # SVM
    svclassifier.fit(train_set, train_classes)


    # Predict using the Test Set
    predicted_labels = svclassifier.predict(test_set)

    print('------------------------ PCA - Results ------------------------')
    # Recall - the ability of the classifier to find all the positive samples
    print("Recall: ", recall_score(test_classes, predicted_labels, average=None, zero_division=1))

    # Precision - The precision is intuitively the ability of the classifier not to
    # label as positive a sample that is negative
    print("Precision: ", precision_score(test_classes, predicted_labels, average=None, zero_division=1))

    # F1-Score - The F1 score can be interpreted as a weighted average of the precision
    # and recall
    print("F1-Score: ", f1_score(test_classes, predicted_labels, average=None, zero_division=1))

    # Accuracy - the number of correctly classified samples
    print("Accuracy: %.2f  ," % accuracy_score(test_classes, predicted_labels, normalize=True),
          accuracy_score(test_classes, predicted_labels, normalize=False))
    print("Number of samples:", test_classes.shape[0])
    print()
    # Compute confusion matrix
    cnf_matrix = confusion_matrix(test_classes, predicted_labels)
    np.set_printoptions(precision=2)

    rotation = 45
    if len(encoded_classes) > 18:
        rotation = 90
    # Plot non-normalized confusion matrix
    plt.figure(figsize=(18, 13))
    plot_confusion_matrix(cnf_matrix, classes=encoded_classes,
                          title='PCA', rotation=rotation)


# ------------------------------------------------ Random Forest ------------------------------------------------
def random_forest(train_set, train_classes, test_set, test_classes, encoded_classes):
    n_estimators = 100

    model = RandomForestClassifier(n_estimators=n_estimators)

    model.fit(train_set, train_classes)

    predicted_labels = model.predict(test_set)

    print('------------------------ Random Forest - Results ------------------------')
    # Recall - the ability of the classifier to find all the positive samples
    print("Recall: ", recall_score(test_classes, predicted_labels, average=None, zero_division=1))

    # Precision - The precision is intuitively the ability of the classifier not to
    # label as positive a sample that is negative
    print("Precision: ", precision_score(test_classes, predicted_labels, average=None, zero_division=1))

    # F1-Score - The F1 score can be interpreted as a weighted average of the precision
    # and recall
    print("F1-Score: ", f1_score(test_classes, predicted_labels, average=None, zero_division=1))

    # Accuracy - the number of correctly classified samples
    print("Accuracy: %.2f  ," % accuracy_score(test_classes, predicted_labels, normalize=True),
          accuracy_score(test_classes, predicted_labels, normalize=False))
    print("Number of samples:", test_classes.shape[0])
    print()

    # Compute confusion matrix
    cnf_matrix = confusion_matrix(test_classes, predicted_labels)
    np.set_printoptions(precision=2)

    rotation = 45
    if len(encoded_classes) > 18:
        rotation = 90
    # Plot non-normalized confusion matrix
    plt.figure(figsize=(18, 13))
    plot_confusion_matrix(cnf_matrix, classes=encoded_classes,
                          title='Random Forest', rotation=rotation)



def knn_combined_clf(train_set, train_classes, test_set, test_classes, encoded_classes):
    # Machine Learning Parameters
    n_neighbors = 3  # Number of neighbors for kNN Classifier

    # KNN Classifier
    model_knn = KNeighborsClassifier(n_neighbors=n_neighbors)

    # kNN
    model_knn.fit(train_set, train_classes)

    # Predict using the Test Set
    predicted_labels = model_knn.predict(test_set)

    predicted_decoded_labels = []
    for label in predicted_labels:
        predicted_decoded_labels.append(encoded_classes[label])

    label_count = Counter(predicted_decoded_labels)

    threshold_label = []
    for i, label_i in enumerate(label_count.most_common()):
        print(label_i)
        if i >= len(test_classes):
            break
        threshold_label.append(label_i[0])

    print('------------------------ KNN-Combined Record- Results ------------------------')
    print('Threshold: ', math.sqrt(len(label_count)) - 1)
    print('Predicted labels: ', predicted_decoded_labels)
    print('Predicted labels: ', label_count)
    print('Threshold label: ', threshold_label)
    print('True labels: ', test_classes)
    print()


def svm_combined_clf(train_set, train_classes, test_set, test_classes, encoded_classes):
    # model_svm = LinearSVC(random_state=0, tol=1e-5, max_iter=5000)
    svclassifier = SVC(kernel='rbf', C=10.0, gamma=0.1)

    # SVM
    svclassifier.fit(train_set, train_classes)

    predicted_labels = svclassifier.predict(test_set)

    predicted_decoded_labels = []
    for label in predicted_labels:
        predicted_decoded_labels.append(encoded_classes[label])

    label_count = Counter(predicted_decoded_labels)

    threshold_label = []
    for i, label_i in enumerate(label_count.most_common()):
        print(label_i)
        if i >= len(test_classes):
            break
        threshold_label.append(label_i[0])

    print('------------------------ SVM-Combined Record- Results ------------------------')
    print('Threshold: ', math.sqrt(len(label_count)) - 1)
    print('Predicted labels: ', predicted_decoded_labels)
    print('Predicted labels: ', label_count)
    print('Threshold label: ', threshold_label)
    print('True labels: ', test_classes)
    print()


def rf_combined_clf(train_set, train_classes, test_set, test_classes, encoded_classes):
    n_estimators = 100

    model = RandomForestClassifier(n_estimators=n_estimators)

    model.fit(train_set, train_classes)

    predicted_labels = model.predict(test_set)

    predicted_decoded_labels = []
    for label in predicted_labels:
        predicted_decoded_labels.append(encoded_classes[label])

    label_count = Counter(predicted_decoded_labels)

    threshold_label = []
    for i, label_i in enumerate(label_count.most_common()):
        print(label_i)
        if i >= len(test_classes):
            break
        threshold_label.append(label_i[0])


    print('------------------------ Random Forest-Combined Record- Results ------------------------')
    print('Threshold: ', math.sqrt(len(label_count)) - 1)
    print('Predicted labels: ', predicted_decoded_labels)
    print('Predicted labels: ', label_count)
    print('Threshold label: ', threshold_label)
    print('True labels: ', test_classes)
    print()
