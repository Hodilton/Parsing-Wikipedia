from .handler_factory import FileHandlerFactory
from .path_validator import PathValidator

from utils.utilities import Raise, Check

class FileProcessor:
    @staticmethod
    def read_file(path_params):
        specified_keys = ["folder_path", "file_name", "extension"]

        if not Check.dictionary_specified(path_params, specified_keys):
            Raise.specified_dict_error(specified_keys)
            return None

        folder_path = path_params.get('folder_path', '')
        file_name = path_params.get('file_name', '')
        expansion = path_params.get('extension', '')

        data = None
        path = PathValidator.get_full_path(folder_path, file_name, expansion)

        if PathValidator.for_read(folder_path, file_name, expansion):
            file_handler = FileHandlerFactory.create_handler(expansion)
            data = file_handler.read(path)

        if data is not None:
            print(fr"Data '{PathValidator.get_project_relative_path()}\{path}' read successfully.")
        else:
            print(fr"Data '{PathValidator.get_project_relative_path()}\{path}' was not read.")

        return data

    @staticmethod
    def write_file(path_params, data, overwrite=True):
        specified_keys = ["folder_path", "file_name", "extension"]

        if not Check.dictionary_specified(path_params, specified_keys):
            Raise.specified_dict_error(specified_keys)
            return False

        folder_path = path_params.get('folder_path', '')
        file_name = path_params.get('file_name', '')
        expansion = path_params.get('extension', '')

        is_success = False
        path = PathValidator.get_full_path(folder_path, file_name, expansion)

        if PathValidator.for_write(folder_path, file_name, expansion, overwrite):
            file_handler = FileHandlerFactory.create_handler(expansion)
            is_success = file_handler.write(path, data, overwrite)

        if is_success:
            print(fr"Data '{PathValidator.get_project_relative_path()}\{path}' written successfully.")
        else:
            print(fr"Data '{PathValidator.get_project_relative_path()}\{path}' was not written.")

        return is_success
