# FROM continuumio/anaconda3
MAINTAINER "Keyth Rodrigues"

RUN 
    sudo apt-get update && sudo apt upgrade

RUN apt-get install -y libgtk2.0-dev apache2-utils curl

RUN 
    curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh && \
    bash Anaconda3-2019.03-Linux-x86_64.sh && \
    source ~/.bashrc && \
    rm Anaconda3-2019.03-Linux-x86_64.sh && \
    tset && \
    conda update conda && \
    conda install -c conda-forge docker-compose \
    conda env create --name tcc_env --file=environment.yml && \
    conda activate tcc_env

RUN sudo mkdir -p /etc/nginx/htpasswd && \
    sudo touch /etc/nginx/htpasswd/ide.tcc_keyth && \
    sudo htpasswd /etc/nginx/htpasswd/ide.tcc_keyth keythroy && \
    sudo mkdir -p /etc/nginx/htpasswd 

RUN docker-compose -f nginx-compose.yaml up -d 

RUN docker-compose -f theia-compose.yaml up -d 

