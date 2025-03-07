from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import json

# Load the model and tokenizer
model_name = "numind/NuExtract-v1.5"
device = "cpu"  # Force CPU usage
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16).to(device).eval()
tokenizer = AutoTokenizer.from_pretrained(model_name)

text = """
We introduce Mistral 7B, a 7-billion-parameter language model engineered for superior performance.
It uses grouped-query attention (GQA) and sliding window attention (SWA). Released under Apache 2.0 license.
"""

template = """
{
    "Model": {
        "Name": "",
        "Parameters": "",
        "Architecture": []
    },
    "Usage": {
        "License": ""
    }
}
"""


def extract_info(model, tokenizer, text, template):
    # Format the prompt as NuExtract expects
    prompt = f"""<|input|>\n### Template:\n{json.dumps(json.loads(template), indent=4)}\n### Text:\n{text}\n\n<|output|>"""

    # Tokenize and generate output
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=4000,  # Adjust based on output length
            temperature=0.0  # Use 0 for pure extraction
        )
    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Extract the JSON part after "<|output|>"
    json_output = output.split("<|output|>")[1].strip()
    return json.loads(json_output)


# Run the extraction
result = extract_info(model, tokenizer, text, template)
print("Extracted JSON:")
print(json.dumps(result, indent=4))