import os

# Functions:
def insert_to_filename(dir_p,split):

    old_names = os.listdir(dir_p)
    old_names = sorted(old_names)
    # once sorted, get the shortest name from the list and obtain the length:
    min_length = len(old_names[0])

    for name in old_names:
        # just one digit in the old name
        if len(name) == min_length:
            new_name = "{}000{}".format(name[:split], name[split+4:])
            os.rename(os.path.join(dir_p, name), os.path.join(dir_p, new_name))

        # two digits
        elif len(name) == min_length+1:
            new_name = "{}00{}".format(name[:split], name[split+4:])
            os.rename(os.path.join(dir_p, name), os.path.join(dir_p, new_name))

        # three digits
        elif len(name) == min_length+2:
            new_name = "{}0{}".format(name[:split], name[split+4:])
            os.rename(os.path.join(dir_p, name), os.path.join(dir_p, new_name))

    return


# Get current files
dir_path = "/home/lito/Documents/EdgeBrain/earthrover/datasets/Broccoli/180905_092602_rgb"

# In order to insert our text, we split the old name into a head and a tail
split_index = 18
names = os.listdir(dir_path)
names = sorted(names)
print(names[0][:split_index])
print(names[0][split_index+4:])
# rename files:
insert_to_filename(dir_path, split_index)
print(os.listdir(dir_path))
