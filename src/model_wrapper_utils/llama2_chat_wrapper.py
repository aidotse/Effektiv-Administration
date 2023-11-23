import os
import sys

os.chdir("/data/dev/llama")
sys.path.append(os.getcwd())

from typing import List, TypedDict
from llama import Llama, Dialog

class Message(TypedDict):
    role: str
    content: str

class Llama2ChatCompletion:
    def __init__(
        self, 
        model_path: str, 
        tokenizer_path: str, 
        max_seq_len: int, 
        max_batch_size: int,
        temperature: float
    ):
        self.generator = Llama.build(
            ckpt_dir=model_path,
            tokenizer_path=tokenizer_path,
            max_seq_len=max_seq_len,
            max_batch_size=max_batch_size
        )
        self.temperature = temperature
    def query(self, system_message, user_messages):
        user_input = []
        user_input.append({
            'role': 'system',
            'content': system_message
        })
        for user_message in user_messages:
            user_input.append({
                'role': 'user',
                'content': user_message
            })
        dialogs: List[Dialog] = [user_input]
        results = self.generator.chat_completion(
            dialogs,
            max_gen_len=None,
            temperature=self.temperature,
            top_p=0.9
        )
        for result in results:
            print(result['generation']['content'])