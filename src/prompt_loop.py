""" Main module to start the application """
import sys
import json
from utils.api.prompt_request import prompt_request

from rich.console import Console
from rich.markdown import Markdown
console = Console()

def question_loop():
    while True:
        usr_prompt = input("Ställ din fråga: ")
        if usr_prompt == "e":
            break
        answer = prompt_request(usr_prompt)['answer']
        console.print(Markdown(answer))

def main() -> None:
    """ For now just a dummy """

    question_loop()

if __name__ == '__main__':
    sys.exit(main())
