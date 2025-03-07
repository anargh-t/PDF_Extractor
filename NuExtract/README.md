# NuExtract v1.5 Text Extraction

This project demonstrates how to use **NuExtract v1.5**, an open-source model by NuMind, to extract structured information from unstructured text and output it as JSON. NuExtract is lightweight, multilingual, and optimized for "pure extraction" (no hallucination).

## Features
- Extracts data from text using a predefined JSON template.
- Runs on CPU (or GPU with sufficient memory).
- Based on the `numind/NuExtract-v1.5` model from Hugging Face.

## Prerequisites
- Python 3.8 or higher
- Required libraries:
  - `torch` (PyTorch)
  - `transformers` (Hugging Face)
- At least 8 GB of RAM (for CPU usage) or a GPU with 4+ GB VRAM (optional).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/anargh-t/NuExtract.git
   cd nuextract-demo
2. Create a virtual environment (optional but recommended):
    ```bash
   python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

3. Install dependencies:
   ```bash
   pip install torch transformers

## Usage
1. Edit nuextract.py to modify the text and template variables with your own data if desired.

2. Run the script:
    ```bash
   python nuextract.py

## Notes
* **CPU Usage:** The script defaults to CPU to avoid GPU memory issues. Change `device = "cuda"` in `main()` if you have a compatible GPU.

* **Memory:** 'NuExtract v1.5' requires ~7-8 GB of memory. For smaller GPUs, try `numind/NuExtract-v1.5` by updating `model_name`.

* **Customization:** Modify the `template` to extract different fields from your text.

## Troubleshooting
* **Memory Error:** If you encounter a `CUDA out of memory error`, ensure `device = "cpu"` or use a smaller model.

* **Slow Performance**: CPU execution is slower than GPU. Be patient during model loading and inference.

## License
This project is licensed under the MIT License. The NuExtract model is provided under the MIT License by NuMind.

## Acknowledgments
* Built with NuExtract v1.5 by NuMind.
* Powered by Hugging Face Transformers.




