# Python slim
FROM python:3.12.5-slim-bookworm

# Workdir
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt requirements.txt

# Install requirements
RUN pip install -r requirements.txt

# Copy else
COPY . .

# Run botfarm
CMD [ "python3", "./factory.py" ]
