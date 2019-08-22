import pandas
import datetime as t
from sklearn.ensemble import RandomForestClassifier

def write_(log):
    f = open('../logs/log_forest.txt', 'a')
    f.write('{0}\r\n'.format(log))
    f.close()


# Load dataset
filenames = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv', '8.csv', '9.csv', '10.csv']
scores = []
write_('{0} START CLASSIFICATION'.format(t.datetime.now()))
for i in range(0, len(filenames)):
    write_('{0} iteration {1}'.format(t.datetime.now(), i))
    print('{0} iteration {1}'.format(t.datetime.now(), i))

    frames = []
    frame = pandas.DataFrame()
    for j in range(0, len(filenames)):
        if j != i:
            write_('{0} train filename:  {1}'.format(t.datetime.now(), filenames[j]))
            dataset = pandas.read_csv('../divided_files/' + filenames[j], index_col=None, header=None, sep=';')
            frames.append(dataset)
    frame = pandas.concat(frames)
    array = frame.values

    X_train = array[:, 0:-1]  # features
    y_train = array[:, -1]  # labels

    random_forest = RandomForestClassifier(max_depth=10, random_state=0, n_estimators=1000)
    write_('{0} start fitting...'.format(t.datetime.now()))
    print('{0} start fitting...'.format(t.datetime.now()))

    model = random_forest.fit(X_train, y_train)

    write_('{0} fitting done '.format(t.datetime.now()))
    print('{0} fitting done '.format(t.datetime.now()))

    # test
    test_file = filenames[i]
    dataset = pandas.read_csv('../divided_files/' + test_file, index_col=None, header=None, sep=';')
    array = dataset.values
    X_test = array[:, 0:-1]  # features
    y_test = array[:, -1]  # labels

    score = model.score(X_test, y_test)
    scores.append(score)
    print('{0} score: {1}'.format(t.datetime.now(), score))
    write_('{0} score: {1}'.format(t.datetime.now(), score))
    test_file = None

result = sum(scores) / float(len(scores))

write_('{0} result: {1}'.format(t.datetime.now(), result))
print('{0} result: {1}'.format(t.datetime.now(), result))

