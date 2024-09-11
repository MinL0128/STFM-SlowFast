# import _pickle
# import pickle
#
# del pickle  # 尝试删除可能存在的变量或模块
# import numpy as np
#
# # filename = "C:/Users/Dell-7920A0\Downloads\greeting/greeting_fjy_fhj_L_dark/dvSave-2021_12_17_14_33_19.npy"
# filename = "G:\Bullying10K_data\zgreeting\greeting_fjy_fhj_L_dark/dvSave-2021_12_17_14_33_19.npy"
# # filename ="G:/Bullying10K_data/zgreeting/greeting_fjy_fhj_L_dark/dvSave-2021_12_17_14_33_19.npy"
# try:
#     data = np.load(filename, allow_pickle=True)
# except _pickle.UnpicklingError as e:
#     print(f"Error loading file {filename}: {e}")
#     data = None  # 返回None或者其他适当的值，表示加载失败
#
# if data is not None:
#     # 继续处理加载成功的数据
#     print("File loaded successfully!")
#     # 进行其他操作...
# else:
#     # 处理加载失败的情况
#     print("Unable to load file. Skipping...")
import os
import numpy as np
import _pickle

def load_and_process_file(file_path):
    try:
        data = np.load(file_path, allow_pickle=True)
        # Process the loaded data (add your processing logic here)
        # print(f"File {file_path} loaded successfully!")
        # Additional processing...
        return True
    except _pickle.UnpicklingError as e:
        print(f"Error loading file {file_path}: {e}")
        return False
    except EOFError:
        print(f"EOFError: The file {file_path} is empty or not properly formatted.")
        return False

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")

def process_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".npy"):
                file_path = os.path.join(root, file_name)
                if not load_and_process_file(file_path):
                    # If loading fails, delete the file
                    delete_file(file_path)



directory_path = "/root/autodl-tmp/Bullying10K_data/walking"
process_files_in_directory(directory_path)

# import numpy as np

# def check_npy_file(file_path):
#     try:
#         # 尝试加载 .npy 文件，设置 allow_pickle=True
#         data = np.load(file_path, allow_pickle=True)

#         # 如果成功加载，输出文件信息
#         print(f"File '{file_path}' is a valid .npy file.")
#         print(f"Shape: {data.shape}")
#         print(f"Data type: {data.dtype}")
#     except Exception as e:
#         # 如果加载失败，输出错误信息
#         print(f"Error loading file '{file_path}': {e}")
#         print("The file may be corrupted or not a valid .npy file.")

# # 用法示例
# file_path_to_check = "/root/autodl-tmp/Bullying10K_data/greeting/greeting_bf_hzq_R_dark/dvSave-2022_09_10_00_55_41.npy"
# check_npy_file(file_path_to_check)