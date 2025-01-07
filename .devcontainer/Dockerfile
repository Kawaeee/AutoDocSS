FROM mcr.microsoft.com/devcontainers/universal:latest

RUN apt update && apt install -y \
    fonts-liberation \
    libvulkan1 \
    xdg-utils && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm -f ./google-chrome-stable_current_amd64.deb && \
    apt clean