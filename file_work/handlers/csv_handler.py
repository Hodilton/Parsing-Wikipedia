import pandas as pd

from .file_handler import FileHandler
from utils.utilities import Raise


class CsvHandler(FileHandler):
    def write(self, data_path, data, overwrite):
        try:
            data_frame = pd.DataFrame(data)
            #data_frame = data_frame.where(pd.notna(data_frame), None)
            data_frame.to_csv(data_path, index=False)
        except Exception as e:
            Raise.try_error(e)
            return False
        return True

    def read(self, data_path):
        try:
            data = pd.read_csv(data_path)
        except Exception as e:
            Raise.try_error(e)
            data = None
        return data