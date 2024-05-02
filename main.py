from file_work.file_processor import FileProcessor
from url_handler import UrlHandler
from test_handler import TestHandler

from utils.utilities import Raise, Print

if __name__ == '__main__':
    json_params = {'folder_path': "data",
                   'file_name': "links",
                   'extension': 'json'}

    csv_params = {'folder_path': "data",
                  'file_name': "definitions",
                  'extension': 'csv'}

    try:
        data_json = FileProcessor.read_file(json_params)
        term_definitions = UrlHandler.parse_definitions(data_json["urls"])

        FileProcessor.write_file(csv_params, term_definitions)
        data_csv = FileProcessor.read_file(csv_params)

        TestHandler.start_test(data_csv)

    except Exception as e:
        Raise.try_error(e)
