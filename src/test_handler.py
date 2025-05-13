import random

class TestHandler:
    @staticmethod
    def start_test(data, total_questions=10, passing_score=7):
        total_score = 0

        while total_score < total_questions:
            TestHandler.print_score(total_score)

            term_data = TestHandler.get_random_term(data)
            term, correct_definition, link = term_data

            definitions = TestHandler.generate_definitions(data, correct_definition)

            TestHandler.print_question(term, definitions)
            user_input = TestHandler.get_user_input()

            if user_input.lower() == 'exit':
                break
            if int(user_input) == definitions.index(correct_definition) + 1:
                print("Correct!")
                total_score += 1
            else:
                print("Incorrect!")
                TestHandler.print_correct_definition(correct_definition)

            TestHandler.print_link(link)
            input("Press Enter to continue...")

        TestHandler.game_over(total_score, passing_score)

    @staticmethod
    def get_random_term(data):
        term_index = random.randint(0, len(data) - 1)
        return data.iloc[term_index]

    @staticmethod
    def generate_definitions(data, correct_definition):
        definitions = [correct_definition]
        while len(definitions) < 3:
            random_index = random.randint(0, len(data) - 1)
            random_definition = data.iloc[random_index]['Definition']
            if random_definition not in definitions:
                definitions.append(random_definition)
        random.shuffle(definitions)
        return definitions

    @staticmethod
    def print_score(score):
        print(f"\nScore: {score}")

    @staticmethod
    def print_question(term, definitions):
        print(f"Question: {term}")
        for i, definition in enumerate(definitions, start=1):
            print(f"{i}. {definition}")

    @staticmethod
    def print_correct_definition(correct_definition):
        print(f"The correct definition is:\n{correct_definition}")

    @staticmethod
    def print_link(link):
        print(f"Link: {link}")

    @staticmethod
    def get_user_input():
        while True:
            user_input = input("\nEnter the correct definition ('exit' to quit): ").strip()

            if user_input.lower() == 'exit':
                return 'exit'
            if user_input.isdigit() and 1 <= int(user_input) <= 4:
                return user_input

            print("Invalid input. Please enter a number between 1 and 4 or 'exit'.")
            continue

    @staticmethod
    def game_over(score, passing_score):
        print("Game over!")
        if score >= passing_score:
            print("Congratulations! You passed the test!")
        else:
            print("Sorry! You didn't pass the test.")
