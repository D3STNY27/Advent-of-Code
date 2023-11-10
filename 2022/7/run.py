MAX_SIZE = 100000
TOTAL_DISK_SPACE = 70000000
REQUIRED_SIZE = 30000000

def get_dir_size(path, file_system):
    if not file_system[path]['folders']:
        if not file_system[path]['files']:
            return 0
        else:
            return sum([x[0] for x in file_system[path]['files']])
    else:
        total_file_size = sum([x[0] for x in file_system[path]['files']])
        total_folder_size = sum([get_dir_size(x, file_system) for x in file_system[path]['folders']])
        return (total_file_size + total_folder_size)

with open('input.txt', 'r') as file_in:
    lines = [line.strip() for line in file_in.readlines()]
    
    current_directory = ''
    file_system = {}
    file_storage = {}

    for line in lines:
        tokens = line.split()
        
        if len(tokens)==3:
            if tokens[2]=='/':
                current_directory = 'root'
            elif tokens[2]=='..':
                current_directory = '/'.join(current_directory.split('/')[:-1])
            else:
                current_directory += f'/{tokens[2]}'
        else:
            if tokens[0]=='$' and tokens[1]=='ls':
                file_system[current_directory] = {
                    'files': [],
                    'folders': []
                }
            elif tokens[0]=='dir':
                file_system[current_directory]['folders'].append(current_directory + f'/{tokens[1]}')
            else:
                file_system[current_directory]['files'].append((int(tokens[0]), tokens[1]))


for key, value in file_system.items():
    file_storage[key] = get_dir_size(key, file_system)

free_space = TOTAL_DISK_SPACE -file_storage['root']
space_to_delete = REQUIRED_SIZE - free_space

storage = list(file_storage.items())
storage.sort(key=lambda x: x[1])

print(space_to_delete)
for key in storage:
    if key[1] < space_to_delete:
        print(key[0], key[1], 'Too Small')
    else:
        print(key[0], key[1], '[FOUND]')
        break