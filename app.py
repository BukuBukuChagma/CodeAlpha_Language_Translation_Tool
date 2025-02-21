from flask import Flask, request, jsonify, send_from_directory, current_app
from flask_cors import CORS
from translate import TranslationService
import os

app = Flask(__name__)
app.static_folder = 'frontend'  # Set the static folder
app.static_url_path = '/static'  # Set the static URL path
CORS(app)  # Enable CORS for all routes

translation_service = TranslationService()

@app.route('/')
def index():
    """Serve the main HTML page"""
    try:
        return current_app.send_static_file('index.html')
    except Exception as e:
        return str(e), 500

@app.route('/api/detect', methods=['POST'])
def detect_language():
    """Detect the language of the input text"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        detected_lang = translation_service.detect_language(text)
        return jsonify({'detected_language': detected_lang})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/translate', methods=['POST'])
def translate_text():
    """Translate text from source language to target language"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        target_lang = data.get('target_lang', 'en')
        source_lang = data.get('source_lang', 'auto')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        translated_text = translation_service.translate(
            text, 
            target_lang=target_lang, 
            source_lang=source_lang
        )
        return jsonify({'translated_text': translated_text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
