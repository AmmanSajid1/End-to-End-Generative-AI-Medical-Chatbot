# 🩺 AI-Powered Medical Chatbot 🚑💬

An **end-to-end AI-powered medical chatbot** built with **Python, Flask, LangChain, Pinecone, and OpenAI**. This chatbot assists users with medical inquiries using **retrieval-augmented generation (RAG), natural language processing (NLP), and vector database search** to deliver accurate and contextual responses.  

## 🛠 Tech Stack  
- **Backend:** Python, Flask  
- **AI & NLP:** LangChain, OpenAI API, Sentence Transformers  
- **Vector Database:** Pinecone  
- **Document Processing:** PyPDF  
- **Cloud & Deployment:** AWS ECR, EC2, GitHub Actions (CI/CD), Docker  

## 🚀 Features  
✅ **Conversational AI:** Uses LangChain & OpenAI for intelligent responses  
✅ **Medical Knowledge Retrieval:** Searches medical documents with Pinecone  
✅ **Flask API:** Serves chatbot responses via a lightweight web API  
✅ **CI/CD Pipeline:** Automated Docker image deployment to AWS  
✅ **Scalable & Cloud-Ready:** Runs on AWS EC2 with Dockerized architecture  

## 📦 Deployment Workflow  
1️⃣ **Code Push:** GitHub Actions triggers CI/CD on `main` branch updates  
2️⃣ **Docker Build & Push:** Builds and uploads the Docker image to **AWS ECR**  
3️⃣ **EC2 Deployment:** Pulls the latest image and runs it in a container  
4️⃣ **Live Chatbot:** The Flask API serves chatbot responses via port `8080`  

## 🚀 Local Setup & Running the Application  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/AmmanSajid1/End-to-End-Generative-AI-Medical-Chatbot.git
cd End-to-End-Generative-AI-Medical-Chatbot
```
### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
Using Conda:
```sh
conda create -n medibot python=3.10 -y
conda activate medibot
```
### 3️⃣ Install Dependencies & Fix Deprecation Issues
```sh
pip install -r requirements.txt
pip uninstall -y pinecone-plugin-inference || true
pip install --no-cache-dir --upgrade pinecone langchain
```
### 4️⃣ Set Up Environment Variables
Create a ```.env``` file in the root directory and add your API keys:
```ini
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key
```
### 5️⃣ Store Embeddings in Pinecone
```sh
python store_index.py
```
### 6️⃣ Run the Chatbot Locally
```sh
python app.py
```
Now, open your browser and go to:
🔗 [localhost](http://localhost:8080)

## 🌍 AWS Deployment with GitHub Actions (CI/CD)

### 1️⃣ AWS Setup

**1.1 Create an IAM User for Deployment**
Grant the following permissions:
- ```AmazonEC2ContainerRegistryFullAccess``` (For AWS ECR)
- ```AmazonEC2FullAccess``` (For EC2 Instance Management)
Download the **Access Key & Secret Key** in a CSV file.

**1.2 Create an AWS ECR Repository**
- Save the Repository URI for later use.

**1.3 Launch an EC2 Instance (Ubuntu)**
- Select Ubuntu as the OS.

**1.4 Install Docker on EC2** \
Run the following commands on your EC2 instance to install Docker:
```sh
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

**1.5 Set Up EC2 as a Self-Hosted Runner for GitHub Actions** \
On GitHub, go to: \
🔗 **Settings → Actions → Runners → New self-hosted runner** \
Follow the commands provided and run them one by one on your EC2 instance.

## 🔄 CI/CD Pipeline with GitHub Actions
### **GitHub Secrets Required**:
Go to **GitHub Repo → Settings → Secrets** and add the following:

- ```AWS_ACCESS_KEY_ID``` (*from downloaded CSV*)
- ```AWS_SECRET_ACCESS_KEY``` (*from downloaded CSV*)
- ```AWS_DEFAULT_REGION``` (*your AWS region, e.g., us-east-1*)
- ```ECR_REPO``` (*your AWS ECR repository name*)
- ```PINECONE_API_KEY``` (*your Pinecone API key*)
- ```OPENAI_API_KEY``` (*your OpenAI API key*)
- 
## 📌 CI/CD Pipeline Breakdown
### **1️⃣ Continuous Integration (CI)**
- **Triggered on ```main``` branch push**
- **Builds the Docker image**
- **Pushes the image to AWS ECR**
## 2️⃣ Continuous Deployment (CD)
- **Runs on EC2 self-hosted runner**
- **Pulls the latest Docker image from ECR**
- **Stops & removes old containers**
- **Runs the chatbot in a new container on port 8080**