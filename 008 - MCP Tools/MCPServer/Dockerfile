# Use the official Python lightweight image
FROM python:3.13-slim

# Install the project into /app
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 8080

# Run the FastMCP server
CMD ["python3", "main.py"]