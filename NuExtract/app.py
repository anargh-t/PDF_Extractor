from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import json
import os
import webbrowser
from threading import Timer

app = Flask(__name__, template_folder='templates')
CORS(app)  # Enable CORS for all routes
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize model and tokenizer
model_name = "numind/NuExtract-v1.5"
device = "cpu"

try:
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16).to(device).eval()
    tokenizer = AutoTokenizer.from_pretrained(model_name)
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None
    tokenizer = None

def load_template(template_type):
    try:
        template_path = os.path.join('templates', f'{template_type}.json')
        with open(template_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading template: {str(e)}")
        return None

def extract_info(text, template):
    if not model or not tokenizer:
        raise Exception("Model or tokenizer not properly initialized")
        
    try:
        prompt = f"""<|input|>\n### Template:\n{json.dumps(template, indent=4)}\n### Text:\n{text}\n\n<|output|>"""
        
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                max_new_tokens=4000,
                temperature=0.0
            )
        output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        json_output = output.split("<|output|>")[1].strip()
        return json.loads(json_output)
    except Exception as e:
        print(f"Error in extraction: {str(e)}")
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if not model or not tokenizer:
        return jsonify({'success': False, 'error': 'Model not properly initialized'})
        
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'})
            
        text = data.get('text', '')
        template_type = data.get('template_type', 'research_paper')
        
        if not text:
            return jsonify({'success': False, 'error': 'No text provided'})
            
        template = load_template(template_type)
        if not template:
            return jsonify({'success': False, 'error': f'Template {template_type} not found'})
            
        result = extract_info(text, template)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def open_browser():
    webbrowser.open('http://127.0.0.1:8080')

if __name__ == '__main__':
    # Open browser automatically after a short delay
    Timer(1.5, open_browser).start()
    # Run the app with specific host and port
    app.run(debug=True, host='127.0.0.1', port=8080, use_reloader=False) 