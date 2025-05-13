import requests
from bs4 import BeautifulSoup

from .definition_formatter import DefinitionFormatter
from utils.utilities import Raise

class DefinitionHandler:
    @staticmethod
    def extract_definitions(urls):
        definitions = []

        for index, url in enumerate(urls, start=1):
            print(f'Processing {index}/{len(urls)}...')

            html_content = WebPageFetcher.fetch(url)
            if not html_content:
                continue

            extractor = DefinitionExtractor(html_content)
            try:
                definition = extractor.extract(url)
                if definition:
                    definitions.append(definition)
            except Exception as e:
                handle_error(e)

        return definitions

class WebPageFetcher:
    @staticmethod
    def fetch(url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            Raise.try_error(e)
            return None


class DefinitionExtractor:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser') if html_content else None

    def extract(self, url):
        if not self.soup:
            return []

        paragraphs = self.soup.select('.mw-parser-output p')
        for paragraph in paragraphs:
            if paragraph.find('b'):
                return self._process_paragraph(paragraph, url)
        return []

    def _process_paragraph(self, paragraph, url):
        term = paragraph.find('b').text.strip()
        formatted_term = DefinitionFormatter.format_term(term)

        definition = paragraph.text.strip().replace(term, '').strip()
        formatted_definition = DefinitionFormatter.format_definition(definition)

        return {
            'Term': formatted_term,
            'Definition': formatted_definition,
            'Link': url
        }
