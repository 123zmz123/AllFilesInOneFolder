import os, shutil
from pathlib import Path

def copy_to_one_folder(src: str, dst: str, file_extention: []):
    if not os.path.exists(src):
        print("Source path not exist!")
    if not os.path.exists(dst):
        print("destination path not exist!")
    for root, dirs, files in os.walk(src, True):
        for each_file in files:
            if os.path.splitext(each_file)[1] in file_extention:
                shutil.copy(os.path.join(root, each_file), dst)
    pass


def example():
    # src = "D:\\iWork\\embedded\\移植ucosToG64\\Micrium_EVBS912XEP100_uCOS-II"
    # dst = "D:\\iWork\\embedded\\移植ucosToG64\\ucosii_Xep100_Flat"
    src = "D:\\iWork\\embedded\\移植ucosToG64\\UcosII_G64_48V20170618"
    dst = "D:\\iWork\\embedded\\移植ucosToG64\\ucosii_G64_Flat"
    file_type = [".s",".S",".C",".c",".H",".h",".prm",".PRM"]
    copy_to_one_folder(src,dst,file_type)
    pass



if __name__ == '__main__':
    example()

    pass
