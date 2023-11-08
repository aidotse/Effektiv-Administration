""" Main module to start the application """
import sys

from model_wrapper.model_wrapper import prompt

def main() -> None:
    """ For now just a dummy """

    system_message = 'You are a chatbot who likes beatboxing in your answers'
    messages = ['How do you cook chicken tikka masala?']

    # model.query(system_message=system_message, user_messages=messages)
    print(prompt(system_message, messages))
    return 0




if __name__ == '__main__':
    sys.exit(main())
