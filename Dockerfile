FROM python:3.10-slim-buster

WORKDIR /app 

COPY . /app 

# Upgrade pip first, then install dependencies  
RUN pip install --no-cache-dir --upgrade pip \
    && pip uninstall -y pinecone-plugin-inference || true \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir --upgrade pinecone langchain

CMD ["python3", "app.py"]