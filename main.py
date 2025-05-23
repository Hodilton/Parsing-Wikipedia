from file_work.file_processor import FileProcessor
from src.url_handler import DefinitionHandler
from src.test_handler import TestHandler

from utils.utilities import Raise

if __name__ == '__main__':
    json_params = {'folder_path': "data",
                   'file_name': "links",
                   'extension': 'json'}

    csv_params = {'folder_path': "data",
                  'file_name': "definitions",
                  'extension': 'csv'}

    try:
        data_json = FileProcessor.read_file(json_params)
        term_definitions = DefinitionHandler.extract_definitions(data_json["urls"])

        FileProcessor.write_file(csv_params, term_definitions, overwrite=True)
        data_csv = FileProcessor.read_file(csv_params)

        TestHandler.start(data_csv)

    except Exception as e:
        Raise.try_error(e)
