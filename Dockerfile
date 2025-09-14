# Gunakan base image Python
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy semua file ke container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port untuk Streamlit
EXPOSE 8501

# Jalankan Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

