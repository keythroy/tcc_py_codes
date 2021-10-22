FROM continuumio/anaconda3

RUN  sudo mkdir -p /etc/nginx/htpasswd 
RUN  sudo touch /etc/nginx/htpasswd/ide.tcc_keyth 
RUN  sudo htpasswd /etc/nginx/htpasswd/ide.tcc_keyth keythroy 
RUN  sudo mkdir -p /etc/nginx/htpasswd 

COPY . .
RUN conda env create -f --name tcc_env --file=conda_environment.yml 

SHELL ["conda", "run", "-n", "tcc_env", "/bin/bash", "-c"]
RUN conda activate tcc_env