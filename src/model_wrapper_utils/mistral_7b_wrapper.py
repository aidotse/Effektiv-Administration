
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from accelerate import init_empty_weights, load_checkpoint_and_dispatch

from rich.console import Console
from rich.markdown import Markdown
console = Console()

# Initialize Variables
model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
hf_auth = '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'

try:

    # Initialize Tokenizer & Model
    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="/data/.cache/huggingface/datasets",     
                                            token=hf_auth)
    model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="/data/.cache/huggingface/datasets", device_map="auto",     
                                                token=hf_auth)

    # generator = pipeline('text-generation', tokenizer=tokenizer, model=model, max_length=20000, 
    generator = pipeline('text-generation', tokenizer=tokenizer, model=model,  
                        torch_dtype=torch.bfloat16, 
                        num_return_sequences=1,
                        device_map="auto",
                        return_full_text=False,
                        max_new_tokens=512,
                        top_p=0.2,
                        top_k=4,
                        repetition_penalty=1.1,
                        temperature=0.01
                        )
except:
    pass

def prompt_model(sys_prompt, usr_prompt):
    prompt = """
    <s>[INST] <<SYS>>
    Jag är en svensk chatbot som svarar på frågor från dokument.
    Jag svarar endast på svenska.
    Jag svarar formellt, objektivt.
    Jag svarar endast om jag har tillgång till informationen annars svarar jag att jag inte har tillgång till informationen.


    <</SYS>>
    Dokumentet jag har tillgång till:
    {}

    Frågan som jag svarar på svenska till är:
    {}
    [/INST]
    """.format(sys_prompt, usr_prompt)
    generated = generator(prompt, do_sample=True)
    print("Hej [Användare], här kommer ditt automatiskt genererade svar:\n")
    sequences = []
    for seq in generated:
        # print(seq['generated_text'])
        sequences.append(seq['generated_text'])
        console.print(Markdown(seq['generated_text']))
    print()
    print("Med Vänliga Hälsningar,\nEffektiv-Administration,\nAISweden")
    return ' '.join(sequences)

    # return prompt
