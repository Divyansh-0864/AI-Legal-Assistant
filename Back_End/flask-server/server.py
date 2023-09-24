from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from flask_cors import CORS 
app = Flask(__name__)

CORS(app, resources={r"/generate": {"origins": "*"}})

# Load GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
model = GPT2LMHeadModel.from_pretrained("gpt2-large", pad_token_id=tokenizer.eos_token_id)

@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        # Get user input from request JSON
        user_input = request.json['user_input']

        # Encode user input
        input_ids = tokenizer.encode(user_input, return_tensors='pt')

        # Generate text until the output length reaches 100 characters
        output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)

        # Decode and return the generated text
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        return jsonify({"generated_text": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
