import os

def remove(curr_path):
    if 'git' in curr_path:
        return
    print(curr_path)
    everything = sorted(list(os.listdir(curr_path)))
    subdirs = [x for x in everything if os.path.isdir(curr_path + '/' + x)]

    if os.path.isfile(curr_path + '/.DS_Store'):
        print('FOUND ONE! ', curr_path + '/.DS_Store')
        os.remove(curr_path + '/.DS_Store')
    
    for dir in subdirs:
        remove(curr_path + '/' + dir)

if __name__ == "__main__":
    remove('.') # start at dl_final_project!
        
        