from csv import reader
from datetime import date


# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file, delimiter=';')
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


def date_column_to_int(dataset, column):
    for row in dataset:
        d = row[column].strip().split('/')
        # print(d)
        row[column] = (date(int(d[0]) + 2000, int(d[1]), int(d[2])) - date(2000, 1, 1)).days


if __name__=='__main__':

    # Load dataset
    filename = 'kickstarter_no_id.csv'
    dataset = load_csv(filename)
    print("Loaded data file {0} with {1} rows and {2} columns".format(filename, len(dataset), len(dataset[0])))
    failed = 0
    successful = 0
    for row in dataset:
        if row[8] == 'failed':
            failed += 1
        else:
            successful += 1

    # print("Successful: {0}".format(successful))
    # print("Failed: {0}".format(failed))

    # convert class column to int
    lookup = str_column_to_int(dataset, 0)
    lookup2 = str_column_to_int(dataset, 1)
    lookup5 = str_column_to_int(dataset, 7)
    lookup6 = str_column_to_int(dataset, 8)

    # print(lookup)
    # print(lookup2)
    # print(lookup5)
    # print(lookup6)
    #f = open('dictionaries.txt', 'w')
    # f.write(lookup)
    # f.write(lookup2)
    # f.write(lookup5)
    # f.write(lookup6)
    # f.close()


    # convert string columns to float
    for i in [4, 5, 6]:
        str_column_to_float(dataset, i)
    # convert data columns to int
    for i in [2, 3]:
        date_column_to_int(dataset, i)

    f = open('kickstarter_token.csv', 'w')
    for d in dataset:
        f.write(';'.join([str(x) for x in d]) + '\n')
    f.close()
