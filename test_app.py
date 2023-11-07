import os
import tempfile
import unittest
from PIL import Image
import io

from app import create_app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app({'TESTING': True})
        self.client = self.app.test_client()

        # Create a dummy image for testing
        self.img = Image.new('RGB', (100, 100))
        self.img_byte_arr = io.BytesIO()
        self.img.save(self.img_byte_arr, format='JPEG')
        self.img_byte_arr.seek(0) 

    def test_predict_endpoint(self):
        # Test a valid image upload
        response = self.client.post(
            '/predict/', 
            data={'image': (self.img_byte_arr, 'test.jpeg')},
            content_type='multipart/form-data'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('probability', response.json[0])

    def test_predict_no_file(self):
        # Test with no file part
        response = self.client.post('/predict/', data={})  
        self.assertEqual(response.status_code, 400)

    def test_predict_no_file_selected(self):
        # Test with empty file filename
        data = {'image': (io.BytesIO(b''), '')}
        response = self.client.post('/predict/', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
