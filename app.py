import os
from flask import Flask, request, render_template
import boto3
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load AWS credentials from .env
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION")
bucket_name = os.getenv("S3_BUCKET")

s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        s3.upload_fileobj(file, bucket_name, file.filename)
        return f'✅ File "{file.filename}" uploaded successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
