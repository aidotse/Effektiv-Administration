""" Main module to start the application """
import sys
import json
from prompt_request import prompt_request
# from model_wrapper import prompt_model
# from query_wrapper import preform_query
from test_prompts.test_prompts import test_prompts, standard_prompts

from rich.console import Console
from rich.markdown import Markdown
console = Console()



def run_standard_prompts():
    output = []
    for prompt in standard_prompts:
        query_string = prompt
        result = preform_query(query_string)
        answer = prompt_model(str(result), prompt)
        output.append({
            "usr_prompt": prompt,
            "answer": answer
        })
    with open("test_results/test_output.json", "w+") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
    

def question_loop():
    while True:
        usr_prompt = input("Ställ din fråga: ")
        if usr_prompt == "e":
            break
        answer = prompt_request(usr_prompt).json()['answer']
        
        console.print(Markdown(answer))
        # print(prompt_request(usr_prompt))
        # query_string = usr_prompt
        # result = preform_query(query_string)
        #print("dokument som hittades: ",[res["filepath"] for res in result])
        #print("results:")
        # print(str(result))
        # prompt_model(str(result), usr_prompt)


def main() -> None:
    """ For now just a dummy """

    # if sys.argv[1] == 'test':
    #     run_standard_prompts()
    #     return 0

    # sys_prompt = test_prompts[0]["sys_prompt"]
    # usr_prompt = test_prompts[0]["usr_prompt"]
    question_loop()



#could create user interface in json file that can be edited...

if __name__ == '__main__':
    sys.exit(main())

