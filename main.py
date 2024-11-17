import os
lines_list = []

files_dir = "text_files"

poem_filepath = os.path.join(files_dir, "poem.txt")

with open("new_poem_filepath", "r", encoding="utf-8") as file:
    for line in file.readlines():
        if line.endswith(",\n"):
            new_line = line.replace(",","")
            lines_list.append(new_line)
        else:
            lines_list.append(line)
print(lines_list)

new_poem_filepath = os.path.join(files_dir, "new_poem_filepath")
with open("new_poem_filepath", "w", encoding="utf-8") as file:
    poem = "".join(lines_list)
    file.write(poem)


with open("new_poem_filepath", "a", encoding="utf-8") as file:
    file.write("\n Михайлюк Артем")