from model_wrapper_utils.llama2_chat_hf_wrapper import prompt_model

# TODO
# create a function here, allowing us to choose model, then returning a prompt_model function
# exmaple usage in main.py: prompt_model = initialize_model('llama2-chat...

# from llama2_chat_wrapper import Llama2ChatCompletion

# model = Llama2ChatCompletion(
#     model_path='/data/dev/llama/llama-2-13b-chat/',
#     tokenizer_path='tokenizer.model',
#     max_seq_len=512,
#     max_batch_size=4,
#     temperature=0.6,
# )

# def prompt(system_message: str, user_message: str):
#     print('sölkjdf')
    # return model.query(system_message, user_messages)


# if __name__ =="__main__":
#     system_message = 'Du ar en chattbott som ska svara pa svenska.'
#     messages = ['Hur lagar man kyckling?']

#     # model.query(system_message=system_message, user_messages=messages)
#     print(prompt(system_message, messages))
#     ...
    
