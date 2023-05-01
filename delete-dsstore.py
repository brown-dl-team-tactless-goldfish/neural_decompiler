import os

def remove(starting_path, relative_path):
    if 'git' in relative_path:
        return
    curr_path = starting_path + relative_path
    everything = sorted(list(os.listdir(curr_path)))
    subdirs = [x for x in everything if os.path.isdir(curr_path + '/' + x)]

    if os.path.isfile(curr_path + '/.DS_Store'):
        print('FOUND ONE! ', curr_path + '/.DS_Store')
        os.remove(curr_path + '/.DS_Store')
    
    for dir in subdirs:
        remove(starting_path, relative_path + '/' + dir)

remove(os.path.dirname(os.path.realpath(__file__)), '')
        