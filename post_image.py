import requests
import argparse

parser = argparse.ArgumentParser(description='Submit an image for prediction.')
# Add argument for the file path
parser.add_argument('file_path', type=str, help='The path to the image file to be uploaded.')
# Parse arguments
args = parser.parse_args()

url = 'http://localhost:5000/predict'

with open(args.file_path, 'rb') as file:
    files = {'image': (args.file_path, file, 'image/jpeg')}
    # Send the POST request
    r = requests.post(url, files=files)

# Print the response
print(r.text)
