# 🚀 KnoxDrive – Upload Files to AWS S3 Using Flask

**KnoxDrive** is a simple, secure, and beginner-friendly web app built with **Python Flask** that allows users to upload files directly to an **AWS S3 bucket**.  
It’s a perfect project to learn AWS services like **IAM**, **S3**, and use them with Python’s SDK **Boto3**.

---

## 🌩️ 1. AWS Setup Guide

Before you run this project, set up the following in your AWS account:

### ✅ Create an IAM User
- Go to **AWS Console → IAM → Users → Add user**
- Enable ✅ **Programmatic access**
- Attach policy: `AmazonS3FullAccess`
- Skip console access
- Save **Access Key ID** and **Secret Access Key**

### ✅ Create an S3 Bucket
- Go to **AWS Console → S3 → Create Bucket**
- Bucket name: `knoxdrive-demo-bucket` *(must be unique)*
- Region: `us-east-1`
- ✅ Block all public access: Enabled
- ✅ Encryption: SSE-S3 (default)
- ✅ Object Ownership: Bucket owner enforced (ACLs disabled)

---

## 📥 2. Clone This Repository

```bash
git clone https://github.com/your-username/knoxdrive.git
cd knoxdrive

. Project Setup (Install Requirements)
