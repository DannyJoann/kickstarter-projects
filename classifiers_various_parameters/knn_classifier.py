import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
import datetime as t
import numpy as np

def write_(log):
    f = open('../logs/log_knn.txt', 'a')
    f.write('{0}\r\n'.format(log))
    f.close()


filenames = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv', '8.csv', '9.csv', '10.csv']
metrics = ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
scores = []
write_('{0} START kNN CLASSIFICATION'.format(t.datetime.now()))
for metric in metrics:
    for n in range(1, 11):
        write_('metric = {0}'.format(metric))
        write_('n = {0}'.format(n))
        test_file = filenames[0]
        frames = []
        frame = pandas.DataFrame()
        for j in range(1, len(filenames)):
            dataset = pandas.read_csv('../divided_files/' + filenames[j], index_col=None, header=None, sep=';')
            frames.append(dataset)
        frame = pandas.concat(frames)
        array = frame.values

        X_train = array[:, 0:-1]  # features
        y_train = array[:, -1]  # labels
        knn = KNeighborsClassifier(n_neighbors=n, metric=metric)
        write_('{0} start fitting...'.format(t.datetime.now()))
        print('{0} start fitting...'.format(t.datetime.now()))

        knn.fit(X_train, y_train)

        write_('{0} fitting done '.format(t.datetime.now()))
        print('{0} fitting done '.format(t.datetime.now()))

        # test
        dataset = pandas.read_csv('../divided_files/' + test_file, index_col=None, header=None, sep=';')
        array = dataset.values
        X_test = array[:, 0:-1]  # features
        y_test = array[:, -1]  # labels

        score = knn.score(X_test, y_test)
        scores.append(score)
        print('{0} score: {1}'.format(t.datetime.now(), score))
        write_('{0} score: {1}'.format(t.datetime.now(), score))

