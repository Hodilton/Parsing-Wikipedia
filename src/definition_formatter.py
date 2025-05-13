import re


class DefinitionFormatter:
    @staticmethod
    def format_definition(definition):
        definition = re.sub(r'\[\d+]', '', definition)
        definition = DefinitionFormatter._remove_text_before_dash(definition)
        definition = DefinitionFormatter.remove_after_dot(definition)
        definition = DefinitionFormatter.upper_one_letter(definition, 0)
        return definition

    @staticmethod
    def _remove_text_before_dash(text):
        dash_pos = text.find('—')
        return text[dash_pos + 1:].strip() if dash_pos != -1 else text

    @staticmethod
    def remove_after_dot(text):
        match = re.search(r'\. [А-Я]', text)
        return text[:match.start() + 1].strip() if match else text

    @staticmethod
    def format_term(term):
        formatted_term = DefinitionFormatter.upper_one_letter(term, 0)
        return formatted_term

    @staticmethod
    def upper_one_letter(text, index):
        return text[:index] + text[index].upper() + text[index + 1:]