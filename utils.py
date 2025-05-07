try:
    import torch
except ImportError:
    import os
    os.system("pip install torch")
    import torch
try:
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
except ImportError:
    import os
    os.system("pip install transformers")
    from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_script(prompt, length, creativity):
    """
    Generates a YouTube script using GPT-2.

    Args:
        prompt (str): The input topic for generating the script.
        length (int): The desired length of the script in sentences or words.
        creativity (float): The temperature for the generation (controls randomness).

    Returns:
        str: The generated script.
    """
    # Tokenize the input and generate a response
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(
        input_ids,
        max_length=length * 50,  # Rough estimate for length in words
        temperature=creativity,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
    )

    script = tokenizer.decode(output[0], skip_special_tokens=True)
    return script
