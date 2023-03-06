FROM python:3.11

COPY requirements.txt .
RUN python3 -m pip install --upgrade pip --no-cache-dir --upgrade -r requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 5000
CMD ["python", "app.py"]