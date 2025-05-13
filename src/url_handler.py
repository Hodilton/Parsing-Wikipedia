import requests
from bs4 import BeautifulSoup

from .definition_formatter import DefinitionFormatter
from utils.utilities import Raise


class UrlFetcher:
    @staticmethod
    def fetch(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            Raise.try_error(e)
            return None


class DefinitionParser:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser') if html_content else None

    def parse(self, url):
        if not self.soup:
            return []

        term_definition_link = []
        for item in self.soup.select('.mw-parser-output p'):
            if item.find('b'):
                term = item.find('b').text.strip()
                formatted_term = DefinitionFormatter.format_term(term)

                definition = item.text.strip().replace(term, '').strip()
                formatted_definition = DefinitionFormatter.format_definition(definition)

                term_definition_link.append({
                    'Term': formatted_term,
                    'Definition': formatted_definition,
                    'Link': url
                })
                break

        return term_definition_link


class UrlHandler:
    @staticmethod
    def parse_definitions(urls):
        definitions = []
        total_urls = len(urls)

        for index, url in enumerate(urls, start=1):
            print(f'Parsing {index}/{total_urls}...')

            html_content = UrlFetcher.fetch(url)
            if html_content is None:
                continue

            parser = DefinitionParser(html_content)
            try:
                definitions.extend(parser.parse(url))
            except Exception as e:
                Raise.try_error(e)

        return definitions
