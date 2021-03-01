# To print the disk usage of the current directory
# Author Sandip Dutta

# -------------------------------------------
import shutil
import os
# -------------------------------------------
# GLOBALS
bytes_to_giga_bytes = 1024 * 1024 * 1024
blue_bg = u"\u001b[44;1m"  # Blue
green_bg = u"\u001b[42;1m"  # Green
red_bg = u"\u001b[41;1m"  # red
reset = u"\u001b[0m"  # make output non sticky
MAX_LENGTH = int(os.get_terminal_size().columns * 0.25)
# ---------------------------------------------

# Get disk usage analysis
total_space, used_space, free_space = shutil.disk_usage(os.getcwd())


def get_length(space, total_space=total_space):
    # Gives value of length of data
    percent = (space / total_space) * MAX_LENGTH
    return int(percent)


# Transform to appropriate length
total_space_len, used_space_len, free_space_len = get_length(total_space), get_length(used_space),\
    get_length(free_space)


def get_value_bar(space_value, space_len, bgcolor, space_name, reset=reset):
    # Generates printable bar for display
    # Space value - value of space to display
    # bgcolor - selects background colour
    # space_name - The name of the space, total space, used space
    # or free space
    # reset - resets the coloured output
    space_val_gb = round(space_value / bytes_to_giga_bytes, 2)

    left_len = " " * (space_len)

    output_string = f"{space_name}\t{space_val_gb} GB\t{bgcolor} {left_len} {reset}"
    return output_string


print('-' * MAX_LENGTH)
print(f"Space analysis Report")
print('-' * MAX_LENGTH)
print(f'Utility called from {os.getcwd()}')
print(get_value_bar(total_space, total_space_len, blue_bg, "Total Space"))
print(get_value_bar(used_space, used_space_len, red_bg, "Used Space"))
print(get_value_bar(free_space, free_space_len, green_bg, "Free Space"))
