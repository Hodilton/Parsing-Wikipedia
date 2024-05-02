import json
import os

import pandas as pd


class Raise:
    @staticmethod
    def try_error(exception):
        print("An error occurred:", exception)

    @staticmethod
    def specified_dict_error(specified_keys):
        print(f"Required keys are not specified: {', '.join(specified_keys)}.")

    @staticmethod
    def file_not_found_error(file_path):
        print(f"File '{file_path}' not found.")

    @staticmethod
    def file_found_error(file_path):
        print(f"File '{file_path}' already exists.")

    @staticmethod
    def folder_not_found_error(folder_path):
        print(f"Folder '{folder_path}' not found.")

    @staticmethod
    def data_load_error():
        print(f"Data is not loaded.")

    @staticmethod
    def format_file_error():
        print(f"This file format is not supported")


class Check:
    @staticmethod
    def dictionary_specified(dictionary, specified):
        for key in specified:
            if key not in dictionary:
                return False
        return True

    @staticmethod
    def check_image_filename(file_name):
        return file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp'))

    @staticmethod
    def images_found_error(folder_path):
        print(f"No images found in folder '{folder_path}\\'.")

class Print:
    @staticmethod
    def json(data):
        print(json.dumps(data, indent=4))

    @staticmethod
    def csv(data):
        pd.set_option('display.max_columns', None)
        print(f"{data.head()}")
