import os
import sys

os.chdir("./model_wrapper")
sys.path.append(os.getcwd())

from llama2_chat_wrapper import Llama2ChatCompletion

model = Llama2ChatCompletion(
    model_path='/data/dev/llama/llama-2-13b-chat/',
    tokenizer_path='tokenizer.model',
    max_seq_len=512,
    max_batch_size=4,
    temperature=0.6,
)

def prompt(system_message: str, user_messages):
    return model.query(system_message, user_messages)


if __name__ =="__main__":
    system_message = 'Du ar en chattbott som ska svara pa svenska.'
    messages = ['Hur lagar man kyckling?']

    # model.query(system_message=system_message, user_messages=messages)
    print(prompt(system_message, messages))
    ...
    
