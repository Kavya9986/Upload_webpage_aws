from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# Configure AWS S3
s3 = boto3.client('s3')

# Configure your S3 bucket name
BUCKET_NAME = 'uploadedimagesforweb'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    s3.upload_fileobj(file, BUCKET_NAME, file.filename)
    return 'File uploaded successfully!'


if __name__ == '__main__':
    app.run(debug=True)
