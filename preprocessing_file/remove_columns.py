def load_file(file_path):
    with open(file_path) as f:
        return f.read()


def save_file(file_path, file_content):
    with open(file_path, 'w') as f:
        f.write(file_content)


content = load_file("../kickstarter_no_id.csv")
result = ''
excluded_columns = [0, 7]

for line in content.split('\n'):
    result += '{}\n'.format(';'.join(x for i, x in enumerate(line.split(';')) if i not in excluded_columns))

save_file("../preprocessing_file/kickstarter_selection.csv", result)
