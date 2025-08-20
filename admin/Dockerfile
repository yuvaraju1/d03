FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 5000  # or 6000, or 7000 depending on service
CMD ["python", "app.py"]
