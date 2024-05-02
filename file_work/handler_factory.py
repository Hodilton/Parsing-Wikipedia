from .handlers.file_handler import FileHandler
from .handlers.csv_handler import CsvHandler
from .handlers.json_handler import JsonHandler


class FileHandlerFactory:
    @staticmethod
    def create_handler(extension):
        if extension == 'csv':
            return CsvHandler()
        elif extension == 'json':
            return JsonHandler()
        else:
            return FileHandler()