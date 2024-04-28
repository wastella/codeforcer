from get_problem import get_problem
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import streamlit as st
import os

st.title('Codeforcer')
st.header("Codeforcer - AI Generated Editorials")
with st.form("my-form"):
   url = st.text_input("Problem URL:")
   submit_button = st.form_submit_button("Submit")
if submit_button:
    problem = get_problem(url)

    messages =[{"role": "user", "content" :  "Please write a solution to the following competitive programming problem in C++, make sure to include a paragraph at the end explaining the solution:{}".format(url)}]

    tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-6.7b-instruct", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-6.7b-instruct", trust_remote_code=True)

    inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
    # tokenizer.eos_token_id is the id of <|EOT|> token
    outputs = model.generate(inputs, max_new_tokens=512, do_sample=False, top_k=50, top_p=0.95, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
    output = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)

    st.write(output)
