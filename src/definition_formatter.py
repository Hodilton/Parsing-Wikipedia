import re


class DefinitionFormatter:
    @staticmethod
    def format_definition(definition):
        without_square_brackets = re.sub(r'\[\d+\]', '', definition)

        without_before_the_dash = DefinitionFormatter.remove_to_dash(without_square_brackets)

        without_after_dot = DefinitionFormatter.remove_after_dot(without_before_the_dash)

        formatted_definition = DefinitionFormatter.upper_one_letter(without_after_dot, 0)

        return formatted_definition
    # def format_definition(definition):
    #     print(f"Original definition: {definition}")
    #
    #     without_square_brackets = re.sub(r'\[\d+\]', '', definition)
    #     print(f"Without square brackets: {without_square_brackets}")
    #
    #     without_before_the_dash = DefinitionFormatter.remove_to_dash(without_square_brackets)
    #     print(f"Without before the dash: {without_before_the_dash}")
    #
    #     if not without_before_the_dash or len(without_before_the_dash) < 2:
    #         print(f"Skipping formatting due to short or empty string: {without_before_the_dash}")
    #         return without_before_the_dash
    #
    #     without_after_dot = DefinitionFormatter.remove_after_dot(without_before_the_dash)
    #     print(f"Without after dot: {without_after_dot}")
    #
    #     if not without_after_dot or len(without_after_dot) < 2:
    #         print(f"Skipping formatting due to short or empty string: {without_after_dot}")
    #         return without_after_dot
    #
    #     formatted_definition = DefinitionFormatter.upper_one_letter(without_after_dot, 0)
    #     print(f"Formatted definition: {formatted_definition}")
    #
    #     return formatted_definition

    @staticmethod
    @staticmethod
    def remove_to_dash(text):
        found_dash = False
        inside_brackets = False
        formatted_text = ''
        temp_text = ''

        for char in text:
            if char == '(':
                inside_brackets = True
            elif char == ')':
                inside_brackets = False
            elif char == '—' and not inside_brackets and not found_dash:
                found_dash = True
                formatted_text += temp_text.strip()
                temp_text = ''
            elif inside_brackets:
                continue
            elif found_dash:
                formatted_text += char
            else:
                temp_text += char

        return formatted_text.strip() if found_dash else text.strip()

    @staticmethod
    def remove_after_dot(text):
        match = re.search(r'\. [А-Я]', text)

        if match:
            formatted_text = text[:match.start() + 1].strip()
        else:
            formatted_text = text.strip()

        return formatted_text

    @staticmethod
    def format_term(term):
        formatted_term = DefinitionFormatter.upper_one_letter(term, 0)
        #formatted_term = re.sub(r'\([^()]*\)', '', formatted_term)
        return formatted_term

    @staticmethod
    def upper_one_letter(text, index):
        return text[:index] + text[index].upper() + text[index + 1:]