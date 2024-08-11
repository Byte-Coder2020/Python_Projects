import os
import sys
from tqdm import tqdm


def create_subfolders(src_folder, dst_folder):
    # 获取源文件夹中的所有子文件夹
    subfolders = [f.name for f in os.scandir(src_folder) if f.is_dir()]

    # 使用 tqdm 创建进度条
    for subfolder in tqdm(subfolders, desc="Creating folders", unit="folder"):
        dst_subfolder_path = os.path.join(dst_folder, subfolder)
        if not os.path.exists(dst_subfolder_path):
            os.makedirs(dst_subfolder_path)


if __name__ == "__main__":
    # 检查输入的参数数量
    if len(sys.argv) != 3:
        print("Usage: python script.py <src_folder> <dst_folder>")
        sys.exit(1)

    src_folder = sys.argv[1]
    dst_folder = sys.argv[2]

    # 检查源文件夹是否存在
    if not os.path.exists(src_folder):
        print(f"Source folder '{src_folder}' does not exist.")
        sys.exit(1)

    # 检查目标文件夹是否存在，不存在则创建
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
        print(f"Created destination folder: {dst_folder}")

    create_subfolders(src_folder, dst_folder)
