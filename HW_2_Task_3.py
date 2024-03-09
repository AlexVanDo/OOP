def get_combination(files):
    sorted_files = {}
    for id_, file_name in enumerate(files):
        with open(file_name, "r", encoding="utf-8") as locals()[f"file{id_}"]:
            lines = eval(f"file{id_}").readlines()
            num_of_lines = len(lines)
            sorted_files[file_name] = num_of_lines
    sorted_files = sorted(sorted_files.items(), key=lambda x: x[1])
    sorted_files = dict(sorted_files)
    new_file = open("Combinated_file.txt", "w+", encoding="utf-8")

    for key, value in sorted_files.items():
        with open(key, "r", encoding="utf-8") as file:
            lines = file.readlines()
            lines = "".join(lines)
            new_file.write(f'{key}\n{value}\n{lines}\n')
    
    new_file.close()


get_combination(["file_1.txt", "file_2.txt", "file_3.txt"])