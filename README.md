# ProLlama - A Secure and Private Local AI Chatbot

ProLlama is a chatbot interface written in Python using the Streamlit library. It connects to your local Llama 3 model through Ollama, ensuring privacy and security.

![screenshot](screenshot.png)

## Prerequisites

1. Install Python 3:
   ```
   brew install python3
   ```

2. Install Ollama by following the instructions at [ollama.com](https://ollama.com/)

3. Download and run the Llama 3 model:
   ```
   ollama run llama3
   ```
## Running ProLlama with Python

### Set Up Environment

1. Navigate to the project directory:
   ```
   cd your-work-directory/prollama
   ```

2. Create and activate a virtual environment:
   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

### Start the Chatbot

1. Launch ProLlama:
   ```
   streamlit run app.py
   ```

## Docker Deployment

1. Build the Docker image:
   ```
   docker buildx build --platform=linux/amd64 -t prollama:version-tag .
   ```
2. Run the Docker image:
   ```
   docker run -p 8501:8501 prollama:version-tag
   ```