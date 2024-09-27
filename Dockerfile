FROM python:3.12-slim-bullseye AS base
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        tesseract-ocr \
        libgl1 \
        libgl1-mesa-dri \
        libglib2.0-0 \
        gcc \
        python3-dev \
        libxkbcommon-x11-0 \
        libx11-xcb1 \
        libxcb-render0 \
        libxcb-shm0 \
        libxcb1 \
        libgl1-mesa-glx \
        libqt5core5a \
        libqt5gui5 \
        libqt5widgets5 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt

