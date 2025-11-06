FROM python:3.10-slim-buster

# 1. Install system dependencies with cleanup, including Node.js and npm
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    python3-pip \
    ffmpeg \
    libopus-dev \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libssl-dev \
    libffi-dev \
    build-essential \
    python3-dev \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 2. Verify Node.js and npm installation
RUN node --version && npm --version

# 3. Upgrade pip and setuptools first
RUN pip3 install --no-cache-dir -U pip setuptools wheel

# 4. Copy only requirements first for better caching
COPY requirements.txt /tmp/requirements.txt

# 5. Install requirements with multiple fallback strategies
RUN pip3 install --no-cache-dir -U -r /tmp/requirements.txt || \
    (pip3 install --no-cache-dir --no-build-isolation -U -r /tmp/requirements.txt || \
     pip3 install --no-cache-dir --ignore-installed -U -r /tmp/requirements.txt)

# 6. Copy the rest of the application
COPY . /app/
WORKDIR /app/

# 7. Final verification
RUN pip3 check

CMD ["bash", "start.sh"]
