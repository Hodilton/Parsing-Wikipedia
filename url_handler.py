import requests

from bs4 import BeautifulSoup
from definition_formatter import DefinitionFormatter

from utils.utilities import Raise


class UrlHandler:
    @staticmethod
    def parse_definitions(urls):
        definitions = []
        total_urls = len(urls)

        for index, url in enumerate(urls, start=1):
            print(f'Parsing {index}/{total_urls}...')

            try:
                definitions.extend(UrlHandler.parse_definition(url))
            except Exception as e:
                Raise.try_error(e)
                return

        return definitions

    @staticmethod
    def parse_definition(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            Raise.try_error(e)
            return

        term_definition_link = []
        for item in soup.select('.mw-parser-output p'):
            if item.find('b'):
                term = item.find('b').text.strip()
                formatted_term = DefinitionFormatter.format_term(term)

                definition = item.text.strip().replace(term, '').strip()
                formatted_definition = DefinitionFormatter.format_definition(definition)

                #print(f"{formatted_term}\n{formatted_definition}\n{url}\n\n")

                term_definition_link.append({'Term': formatted_term, 'Definition': formatted_definition, 'Link': url})
                break

        return term_definition_link
