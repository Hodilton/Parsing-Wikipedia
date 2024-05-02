import os

from utils.utilities import Raise


class PathValidator:
    @staticmethod
    def for_read(folder_path, file_name, expansion):
        if not PathValidator.validate_path(folder_path, "directory"):
            Raise.folder_not_found_error(fr"{PathValidator.get_project_relative_path()}\{folder_path}")
            return False

        path = PathValidator.get_full_path(folder_path, file_name, expansion)

        if not PathValidator.validate_path(path, "file"):
            Raise.file_not_found_error(fr"{PathValidator.get_project_relative_path()}\{path}")
            return False

        return True

    @staticmethod
    def for_write(folder_path, file_name, expansion, overwrite):
        if not PathValidator.validate_path(folder_path, "directory"):
            Raise.folder_not_found_error(fr"{PathValidator.get_project_relative_path()}\{folder_path}")
            return False

        path = PathValidator.get_full_path(folder_path, file_name, expansion)

        if PathValidator.validate_path(path, "file") and not overwrite:
            Raise.file_found_error(fr"{PathValidator.get_project_relative_path()}\{path}")
            return False

        return True

    @staticmethod
    def validate_path(file_path, check_type=None):
        if check_type == 'file' and not os.path.isfile(file_path):
            return False

        if check_type == 'directory' and not os.path.isdir(file_path):
            return False

        if not os.path.exists(file_path):
            return False

        return True

    @staticmethod
    def get_full_path(folder_path, file_name, expansion):
        return os.path.join(folder_path, file_name + '.' + expansion)

    @staticmethod
    def get_project_relative_path():
        current_dir = os.getcwd()
        project_dir = os.path.abspath(__file__)

        while not os.path.isfile(os.path.join(project_dir, '__init__.py')):
            project_dir = os.path.dirname(project_dir)

        relative_path = os.path.relpath(current_dir, start=project_dir)
        return relative_path

        #return os.path.relpath(os.getcwd(), start=os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
