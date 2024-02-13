ARG PYTHON_VERSION=3.10.11
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir -r requirement.txt

# Copy the source code into the container.
COPY chroma_storage /app/chroma_storage

COPY file /app/file

COPY src /app/src

COPY licence /app/licence

COPY requirement.txt /app/requirement.txt

COPY start_everything_bash /app/start_everything_bash

# Expose the port that the application listens on.
EXPOSE 5000

# Run the application.
CMD python3 src/server_mail.py
