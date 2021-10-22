#!/bin/bash
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    libgtk2.0-dev \
    apache2-utils
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install -y docker-ce
# Linux post-install
sudo groupadd docker
sudo usermod -aG docker $USER
sudo systemctl enable docker

sudo apt-get install python3 python-pip

curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh && \
bash Anaconda3-2019.03-Linux-x86_64.sh && \
source ~/.bashrc && \
rm Anaconda3-2019.03-Linux-x86_64.sh && \
tset && \
conda update conda && \
conda install -c conda-forge docker-compose \
conda env create --name tcc_env --file=environment.yml && \
conda activate tcc_env