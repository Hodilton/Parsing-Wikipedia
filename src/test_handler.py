import random

class TestHandler:
    QUESTIONS_PER_TEST = 10
    PASSING_SCORE = 7

    @staticmethod
    def start(definitions_data):
        score = 0
        while score < TestHandler.QUESTIONS_PER_TEST:
            TestHandler._display_score(score)

            question, correct_answer, link = TestHandler._select_question(definitions_data)
            options = TestHandler._generate_options(definitions_data, correct_answer)

            TestHandler._display_question(question, options)
            user_choice = TestHandler._get_user_choice()

            if user_choice == 'exit':
                break

            if int(user_choice) == options.index(correct_answer) + 1:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
                TestHandler._show_correct_answer(correct_answer)

            TestHandler._show_reference_link(link)
            input("Press Enter to continue...")

        TestHandler._display_final_result(score)

    @staticmethod
    def _select_question(definitions_data):
        random_index = random.randint(0, len(definitions_data) - 1)
        row = definitions_data.iloc[random_index]
        return row['Term'], row['Definition'], row['Link']

    @staticmethod
    def _generate_options(definitions_data, correct_answer):
        options = [correct_answer]
        while len(options) < 3:
            random_index = random.randint(0, len(definitions_data) - 1)
            option = definitions_data.iloc[random_index]['Definition']
            if option not in options:
                options.append(option)
        random.shuffle(options)
        return options

    @staticmethod
    def _display_score(score):
        print(f"\nScore: {score}")

    @staticmethod
    def _display_question(term, options):
        print(f"Question: {term}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    @staticmethod
    def _get_user_choice():
        while True:
            choice = input("\nEnter the correct option (1-3) or 'exit' to quit: ").strip()
            if choice.lower() == 'exit':
                return 'exit'
            if choice.isdigit() and 1 <= int(choice) <= 3:
                return choice
            print("Invalid input. Please enter 1, 2, 3 or 'exit'.")

    @staticmethod
    def _show_correct_answer(answer):
        print(f"The correct answer is:\n{answer}")

    @staticmethod
    def _show_reference_link(link):
        print(f"Reference: {link}")

    @staticmethod
    def _display_final_result(score):
        print("\nTest completed!")
        if score >= TestRunner.PASSING_SCORE:
            print("Congratulations! You passed!")
        else:
            print("You didn't pass. Try again!")
        print(f"Final score: {score}/{TestRunner.QUESTIONS_PER_TEST}")