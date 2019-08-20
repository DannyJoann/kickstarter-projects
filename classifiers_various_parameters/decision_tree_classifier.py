import pandas
import datetime as t
from sklearn.tree import DecisionTreeClassifier


def write_(log):
    f = open('../logs/log_tree.txt', 'a')
    f.write('{0}\r\n'.format(log))
    f.close()


filenames = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv', '8.csv', '9.csv', '10.csv']
max_d = [2, 6, 10, 50, 100, 500, 1000,  None]
scores = []
write_('{0} START CLASSIFICATION'.format(t.datetime.now()))
for d in max_d:
    write_('Max depth = {0}'.format(d))
    print('Max depth = {0}'.format(d))
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
    dec_tree = DecisionTreeClassifier(max_depth=d, random_state=0)
    write_('{0} start fitting...'.format(t.datetime.now()))
    print('{0} start fitting...'.format(t.datetime.now()))

    model = dec_tree.fit(X_train, y_train)

    write_('{0} fitting done '.format(t.datetime.now()))
    print('{0} fitting done '.format(t.datetime.now()))
    # test
    dataset = pandas.read_csv('../divided_files/' + test_file, index_col=None, header=None, sep=';')
    array = dataset.values
    X_test = array[:, 0:-1]  # features
    y_test = array[:, -1]  # label
    score = model.score(X_test, y_test)
    scores.append(score)
    print('{0} score: {1}'.format(t.datetime.now(), score))
    write_('{0} score: {1}'.format(t.datetime.now(), score))
