import os, shutil

def copy_dir_without_hidden(source_dir, destination_dir):
    """
    Recursively copies all files from source_dir to destination_dir, 
    without all the hidden files (i.e. files with names beginning with '.')

    ### Params
    source_dir - the path of the source directory to be copied
    destination_dir - the path of the directory to copy files into

    ### Returns
    Nothing!
    """
    # if the destination directory doesn't already exist, make it!
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

    for item in os.listdir(source_dir):
        # skipping hidden files
        if item[0] == '.':
            continue

        item_path = f"{source_dir}/{item}" # path of original file
        destination_path = f"{destination_dir}/{item}" # path of copy

        dirnames_to_skip = ["leetcode_data_FINAL", "extra_data_FINAL", "frontend", "model_checkpoints", "random_asm", "archive"]

        # if the item is a directory, then recurse on the directory!

        if os.path.isdir(item_path) and item_path.split('/')[-1] not in dirnames_to_skip:

            copy_dir_without_hidden(item_path, destination_path)
        # if the item is a file, copy it to destination
        else:  

            try:
                shutil.copy(item_path, destination_path)
                print("copied " + item_path)
            except:
                pass


if __name__ == "__main__":
    # path of current directory (where this script is!) this is the directory that will be copied
    source_dir = f"{os.path.dirname(os.path.realpath(__file__))}/.."

    destination_dir = source_dir + f"/../dl_final_project_no_hidden"

    copy_dir_without_hidden(source_dir, destination_dir)

    print("destination: ", destination_dir)

