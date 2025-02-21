import unittest
import tracemalloc
from app import app
from translate import TranslationService
from contextlib import contextmanager
import warnings
import ssl
import gc

# Filter out SSL deprecation warnings
warnings.filterwarnings('ignore', category=DeprecationWarning, module='ssl')

# Start tracemalloc for better resource tracking
tracemalloc.start()

class TestTranslationApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up class-level resources"""
        cls.translation_service = TranslationService()
        cls.app = app.test_client()
        # Disable SSL verification for tests
        ssl._create_default_https_context = ssl._create_unverified_context

    def setUp(self):
        """Set up test client and other test variables"""
        app.config['TESTING'] = True
        self.client = app.test_client()
        
    def tearDown(self):
        """Clean up resources after each test"""
        gc.collect()

    @contextmanager
    def get_index_file(self):
        """Context manager for handling index.html file"""
        try:
            with open('frontend/index.html', 'rb') as f:
                yield f
        finally:
            # File will be automatically closed after the with block
            pass

    def test_index_route(self):
        """Test if the main page is served correctly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_detect_language_endpoint(self):
        """Test language detection endpoint"""
        with self.client as client:
            response = client.post('/api/detect', 
                json={'text': 'Hello, world!'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('detected_language', response.get_json())
        
            response = client.post('/api/detect', 
                json={'text': ''})
            self.assertEqual(response.status_code, 400)
        
            response = client.post('/api/detect', 
                json={})
            self.assertEqual(response.status_code, 400)

    def test_translate_endpoint(self):
        """Test translation endpoint"""
        test_data = {
            'text': 'Hello',
            'source_lang': 'en',
            'target_lang': 'es'
        }
        
        with self.client as client:
            response = client.post('/api/translate', 
                json=test_data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('translated_text', response.get_json())
        
            test_data['text'] = ''
            response = client.post('/api/translate', 
                json=test_data)
            self.assertEqual(response.status_code, 400)
        
            response = client.post('/api/translate', 
                json={'target_lang': 'es'})
            self.assertEqual(response.status_code, 400)

    def test_translation_service(self):
        """Test TranslationService class methods directly"""
        detected_lang = self.translation_service.detect_language('Hello')
        self.assertEqual(detected_lang, 'en')
        
        translated_text = self.translation_service.translate(
            'Hello', 
            target_lang='es', 
            source_lang='en'
        )
        self.assertIsInstance(translated_text, str)
        self.assertNotEqual(translated_text, 'Hello')

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level resources"""
        if hasattr(cls.translation_service.translator, '_client'):
            cls.translation_service.translator._client.close()
        # Force cleanup of any remaining resources
        gc.collect()

if __name__ == '__main__':
    # Suppress ResourceWarnings during test execution
    warnings.simplefilter("ignore", ResourceWarning)
    unittest.main() 