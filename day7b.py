with open(r'day7_input.txt') as f:
    file = f.read()
    f.close()

file = file.split('\n')
file.pop()

dirs = {}
curr_dir = []
names = []  # need to name folders in dict as entire path to deal with repeated names

for line in file:
    # command
    if line[0] == '$':
        if line[2:4] == 'cd':
            if line[5:] == '..':
                curr_dir.pop()
                names.pop()
            else:
                bottom_folder = line[5:]
                curr_dir.append(bottom_folder)

                name = '/'.join(curr_dir)
                names.append(name)

                if name not in dirs:
                    dirs.update({f'{name}': 0})

    # file or folder
    else:
        if line[:3] != 'dir':
            size = line.split(' ')[0]
            for folder in names:
                dirs[folder] += int(size)

req_space = 30000000 - (70000000 - dirs['/'])
sorted_dirs = dict(sorted(dirs.items(), key=lambda item: item[1]))

for folder in sorted_dirs:
    value = sorted_dirs[folder]
    if value > req_space:
        break

print(f'Result: {value}')