import json

from .file_handler import FileHandler
from utils.utilities import Raise

class JsonHandler(FileHandler):
    def write(self, data_path, data, overwrite):
        try:
            with open(data_path, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            Raise.try_error(e)
            return False
        return True
    def read(self, data_path):
        try:
            with open(data_path, 'r') as file:
                data = json.load(file)
        except Exception as e:
            Raise.try_error(e)
            data = None
        return data