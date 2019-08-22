import pandas
from sklearn import svm
import datetime as t


def write_(log):
    f = open('../logs/log_svm.txt', 'a')
    f.write('{0}\r\n'.format(log))
    f.close()


filenames = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv', '8.csv', '9.csv', '10.csv']
nu = [0.7, 0.5, 0.1, 0.04]
gamma = [0.8, 0.5, 0.3, 0.06]
scores = []
write_('{0} START CLASSIFICATION'.format(t.datetime.now()))

for n in nu:
    for g in gamma:
        write_('nu = {0}'.format(n))
        write_('gamma = {0}'.format(g))
        print('nu = {0}'.format(n))
        print('gamma = {0}'.format(g))
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
        nuSVC = svm.NuSVC(nu=n, kernel='rbf', gamma=g)
        write_('{0} start fitting...'.format(t.datetime.now()))
        print('{0} start fitting...'.format(t.datetime.now()))

        model = nuSVC.fit(X_train, y_train)

        write_('{0} fitting done '.format(t.datetime.now()))
        print('{0} fitting done '.format(t.datetime.now()))

        # test
        dataset = pandas.read_csv('../divided_files/' + test_file, index_col=None, header=None, sep=';')
        array = dataset.values
        X_test = array[:, 0:-1]  # features
        y_test = array[:, -1]  # labels

        score = model.score(X_test, y_test)
        scores.append(score)
        print('{0} score: {1}'.format(t.datetime.now(), score))
        write_('{0} score: {1}'.format(t.datetime.now(), score))

