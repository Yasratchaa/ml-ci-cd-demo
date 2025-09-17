# Gunakan base image Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy semua file ke container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Streamlit (default 8501)
EXPOSE 8501

# Jalankan training model saat build (opsional, bisa dihapus kalau model.pkl sudah ada)
RUN python train.py

# Perintah untuk menjalankan aplikasi Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
