from flask import Flask, request, jsonify
import openai
import os
import time
from flask_cors import CORS
import deepl




# Constants
#CHATGPT_MODEL = "gpt-4-0613"
CHATGPT_MODEL = "gpt-3.5-turbo"
CHATGPT_URL =  "https://api.openai.com/v1/chat/completions"

app = Flask(__name__)
CORS(app)

@app.route('/process_text', methods=['POST'])
def process_text():
    global CHATGPT_MODEL 

    data = request.get_json()
    response_text = "If this sentence is shwon, something went wrong"
    text = data['text']
   # model = data['model']
    mode =  data['mode']

    print(f"""before: {text}""")

    #if model == 'ChatGPT':
    #    CHATGPT_MODEL = "gpt-3.5-turbo"
    #elif model == 'GPT4':
    #    CHATGPT_MODEL = "gpt-4"
    #elif model == 'DEEPL':
    #    pass
    #else:
    #    return jsonify({'error': 'Invalid model name'}), 400

    if mode == 'ChatGPT':
        response_text = translate_with_chatgpt(text)
   # elif mode == 'complete':
   #     response_text = complete_with_chatgpt(text)
    elif mode == 'DeepL':
        response_text = translate_with_deepl(text)
    #response_text = translate_with_chatgpt(text)
    print(response_text)

    return jsonify({'result': response_text})


def translate_with_chatgpt(text):
    prompt = f"""以下の英文を日本語に翻訳してください。\n\nOriginal Text:\n{text}\n\n翻訳した文:"""
    data = create_chat_completion_with_retry(prompt, retries=3, delay=5)        
    translated_text = data["choices"][0]["message"]["content"].strip() # type: ignore
    
    print(f"""{translated_text}""")
    return translated_text

def create_chat_completion_with_retry(prompt, retries=3, delay=5):
    global CHATGPT_MODEL
    for _ in range(retries):
        try:
            data = openai.ChatCompletion.create(
                model= CHATGPT_MODEL,
                messages= [{"role": "user", "content": prompt}]
            )
            return data
        except Exception as e:  
            print(f"Request failed with {e}, retrying...")
            time.sleep(delay)  # Wait for 'delay' seconds before next retry

    # If control reaches here, all retries have failed
    return  {
        "choices": [{"message": {"content" : "Error was not resolved!"}}]
    }

def translate_with_deepl(text):
    DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
    #DEEPL_API_URL = 'https://api-free.deepl.com/v2/translate'
    translator = deepl.Translator(DEEPL_API_KEY, verify_ssl=False) # type: ignore
    result = translator.translate_text(text, target_lang="JA").__str__()
    print(f"""{result}""")
    return result


if __name__ == '__main__':
    app.run(port=8000)