from aoc_inputs import get_input
import re

# commands = get_input()
commands = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e   
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
command_list = commands.split('\n')


def walk_through_commands(limit: 100000):
    # this ignores the top '/' dir
    pat_cd_dir = r"\$\scd\s([a-zA-Z])\s"
    pat_move_up = r"\$\scd\s(\.\.)\s"
    pat_file_size = r"^(\d*)\s"
    pat_contains_dir = r"^dir\s(\w*)"
    pat_ls = r"\$\sls"
    for i, cmd in enumerate(command_list):
        dr = re.match(pat_cd_dir, cmd)
        if dr:
            file_size = 0
            contents = dir_contents(dir_name=dr.group(1), command_str='\n'.join(command_list[i:]))
            files = [item for item in contents if 'dir ' not in item]
            file_size += sum([int(re.match(r"(\d*)", f).group()) for f in files])
            if file_size > limit:
                pass
            sub_dirs = [item.split('dir ')[1] for item in dir_contents(dr) if 'dir ' in item]



def dir_contents(dir_name: str, command_str: str = commands) -> list:
    cd_dir_command = f"$ cd {dir_name}\n$ ls\n"
    start_point = command_str.find(cd_dir_command) + len(cd_dir_command)
    end_point = command_str.find('\n$', start_point)
    return command_str[start_point: end_point].split('\n')


def return_dir_details():
    dir_pat = r"\$\scd\s([a-zA-Z/]*)"
    all_dirs = [dr for dr in re.findall(dir_pat, commands) if dr != '']
    dir_details = {}
    for dr in all_dirs:
        contents = dir_contents(dr)
        files = [item for item in contents if 'dir ' not in item]
        file_size = sum([int(re.match(r"(\d*)", f).group()) for f in files])
        sub_dirs = [item.split('dir ')[1] for item in dir_contents(dr) if 'dir ' in item]
        dir_details[dr] = {'contents': contents, 'files': files, 'file_size': file_size, 'sub_dirs': sub_dirs}
    return dir_details


def dirs_to_remove(dir_details: dict, limit=100000):
    dir_list = []
    for dr, details in dir_details.items():
        if details['file_size'] > limit:
            dir_list.append(dr)
    return dir_list


def sub_dirs_to_remove(dir_details: dict, dir_list: list):
    if dir_list is None:
        dir_list = []
    for top_dir, details in dir_details.items():
        for dr in dir_list:
            if dr in details['sub_dirs']:
                dir_list.append(top_dir)
    return list(set(dir_list))


def part_1_test():
    dir_details = return_dir_details()
    remove_list = dirs_to_remove(dir_details)
    remove_list = sub_dirs_to_remove(dir_details, remove_list)
    for dr in remove_list:
        dir_details.pop(dr)
    total = 0
    for dir, details in dir_details.items():
        total += details['file_size']


def item_size(item: str):
    size = 0
    size_pat = r"(\d*)"
    size_match = re.match(size_pat, item)
    if size_match and size_match.group().isnumeric():
        size += int(size_match.group())
    return size


def sub_dir_list(current_dir: str, dir_list=None):
    if dir_list is None:
        dir_list = []
    sub_dirs = [item.split('dir ')[1] for item in dir_contents(current_dir) if 'dir ' in item]
    if len(sub_dirs) > 0:
        for sd in sub_dirs:
            dir_list.append(sd)
            sub_dir_list(current_dir=sd, dir_list=dir_list)
    return dir_list


def sub_dir_size(current_dir: str, total_dir_size=0, limit=100000):
    total_dir_size += dir_size(current_dir)
    sub_dirs = [item.split('dir ')[1] for item in dir_contents(current_dir) if 'dir ' in item]
    if len(sub_dirs) > 0:
        for sd in sub_dirs:
            total_dir_size += dir_size(current_dir)
            if total_dir_size > limit:
                return None
            else:
                sub_dir_size(current_dir=sd, total_dir_size=total_dir_size)
    return total_dir_size


def dir_size(dir_name: str):
    contents = dir_contents(dir_name)
    files = [item for item in contents if 'dir ' not in item]
    return sum([int(re.match(r"(\d*)", f).group()) for f in files])


def part_1():
    dir_pat = r"\$\scd\s([a-zA-Z/]*)"
    dir_details = return_dir_details()
    remove_list = dirs_to_remove(dir_details)
    remove_list = sub_dirs_to_remove(dir_details, remove_list)
    for dr in remove_list:
        dir_details.pop(dr)
    total_size = 0
    for dr, details in dir_details.items():
        total_size += details['file_size']
        for sd in details['sub_dirs']:
            total_size += dir_details.get(sd).get('file_size')
    return total_size


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
