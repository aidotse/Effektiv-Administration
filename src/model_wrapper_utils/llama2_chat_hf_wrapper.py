
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from accelerate import init_empty_weights, load_checkpoint_and_dispatch

# Initialize Variables
model_name = "meta-llama/Llama-2-13b-chat-hf"
hf_auth = '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'

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
                     top_p=0.99,
                     top_k=50,
                     repetition_penalty=1.1,
                     temperature=0.01
                     )

def prompt_model(sys_prompt, usr_prompt):
    prompt = """
    <s>[INST] <<SYS>>
    Jag är en svensk chattbott som ska hjälpa genom att besvara frågor på svenska. 
    Här är mina instruktioner:
    * Jag svarar endast på svenska och aldrig på engelska.
    * Till min hjälp har jag dokument. 

    Svara endast på svenska!

    Här är dokumenten:
    {}
    <</SYS>>
    {} ge mig ett svar på svenska! [/INST]
    """.format(sys_prompt, usr_prompt)
    generated = generator(prompt, do_sample=True, temperature=0.01)
    print("Hej [Användare]")
    for seq in generated:
        print(seq['generated_text'])
    print("Med Vänliga Hälsningar,\nEffektiv-Administration,\nAISweden")
    # return prompt