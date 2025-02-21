from googletrans import Translator
from contextlib import contextmanager
import warnings

class TranslationService:
    def __init__(self):
        self._translator = None
        warnings.filterwarnings('ignore', category=ResourceWarning)
    
    @property
    def translator(self):
        """Lazy initialization of translator"""
        if self._translator is None:
            self._translator = Translator()
        return self._translator
        
    def _ensure_connection(self):
        """Ensure translator connection is active"""
        if not self._translator or not hasattr(self._translator, '_client'):
            self._translator = Translator()
        
    def detect_language(self, text):
        """Detect the language of the input text"""
        try:
            self._ensure_connection()
            detection = self.translator.detect(text)
            return detection.lang
        except Exception as e:
            raise Exception(f"Error detecting language: {str(e)}")
    
    def translate(self, text, target_lang='en', source_lang='auto'):
        """Translate text from source language to target language"""
        try:
            self._ensure_connection()
            if source_lang == 'auto':
                translation = self.translator.translate(text, dest=target_lang)
            else:
                translation = self.translator.translate(
                    text, 
                    src=source_lang, 
                    dest=target_lang
                )
            return translation.text
        except Exception as e:
            raise Exception(f"Error translating text: {str(e)}")

    def __del__(self):
        """Cleanup when the service is destroyed"""
        try:
            if self._translator and hasattr(self._translator, '_client'):
                self._translator._client.close()
        except:
            pass
