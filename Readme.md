# 🚀 KnoxDrive – Upload Files to AWS S3 Using Flask

KnoxDrive is a beginner-friendly web app built with Python Flask that lets you upload files to your own AWS S3 bucket securely.  
This project helps you learn how to use AWS IAM + S3 + Python + Boto3 to build real-world cloud-integrated apps.

## 🌩️ 1. AWS Setup Guide

Before running the project, configure AWS:

- Go to AWS Console → IAM → Users → Add user  
  - Enter username (e.g., knoxdrive-user)  
  - Enable ✅ Programmatic access  
  - Click "Next" → Attach existing policies directly  
  - Select ✅ AmazonS3FullAccess  
  - Click "Next" → Create user  
  - Save your Access Key ID and Secret Access Key  

- Go to AWS Console → S3 → Create Bucket  
  - Bucket name: knoxdrive-demo-bucket (must be globally unique)  
  - Region: us-east-1  
  - ✅ Block all public access: Enabled  
  - ✅ Encryption: SSE-S3 (default)  
  - ✅ Object Ownership: Bucket owner enforced (ACLs disabled)  
  - Click "Create bucket"

## 📥 2. Clone This Repository

```bash
git clone https://github.com/your-username/knoxdrive.git
cd knoxdrive
```

## 📦 3. Download Requirements

```bash
pip install -r requirements.txt
```

## 🔐 4. Create Your .env File

Create a file named `.env` in the root folder and paste:

```env
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_REGION=us-east-1
S3_BUCKET=knoxdrive-demo-bucket
```

⚠️ Important: Never upload this file to GitHub — it’s already ignored in `.gitignore

## ▶️ 5. Run the Project

```bash
python app.py
```

Open your browser:  
http://localhost:5000/  
✅ Upload a file — it will go to your S3 bucket.

## 📁 Project Folder Structure

```
knoxdrive/
├── app.py
├── templates/
│   └── index.html
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔒 Security Tips

- Never upload `.env` to GitHub
- Use IAM user with only S3 access
- Rotate AWS keys regularly
- Keep S3 bucket public access blocke

## 💡 Future Improvements

- Host app on EC2
- Add upload progress bar
- File type/size validation
- Use pre-signed URLs
- Store file metadata in a database

## 👨‍💻 Author

**Knox (Rupesh)**  
GitHub: [https://github.com/Rupeshs11](https://github.com/Rupeshs11)

## 📜 License

Licensed under the MIT License.
