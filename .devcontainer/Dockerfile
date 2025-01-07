FROM mcr.microsoft.com/devcontainers/universal:latest

RUN apt update && apt install -y fonts-liberation libvulkan1 xdg-utils && export DEBIAN_FRONTEND=noninteractive && apt clean

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

# Set up a working directory
WORKDIR /workspaces

# Install Python dependencies (optional step)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
