from os import listdir
from os.path import isdir, join

def directory_traversal(path, file_by_ext):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_traversal(join(path, element), file_by_ext)
        else:
            extension = element.split(".")[-1]
            if extension not in file_by_ext:
                file_by_ext[extension] = []
            file_by_ext[extension].append(element)

print_result = []
result = {}

directory = input()
directory_traversal(directory, result)

result = sorted(result.items(), key=lambda x: x[0])

for extension, files in result:
    print_result.append(f".{extension}\n")

    for file in sorted(files):
        print_result.append(f"- - - {file}\n")

with open("./report.txt", "w") as file:
    file.write("".join(print_result))

