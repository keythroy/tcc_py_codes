import os
import sys

def export():
    print('------------------ Export -----------------')
    
    print('# apt')
    os.system("dpkg --get-selections > apt_packages.txt")
    
    print('# pip')    
    os.system('pip freeze > requirements.txt')
    
    print('# conda')
    os.system("conda env export > environments.yml")
    
def install():
    print('------------------ Import -----------------')

    print('# apt')    
    os.system("sudo apt-get install dselect")
    os.system("sudo dselect update")
    os.system("sudo dpkg --set-selections < apt_packages.txt")
    os.system("sudo apt-get -y update")
    os.system("sudo apt-get dselect-upgrade")

    print('# pip')    
    os.system('pip install -r requirements.txt')

    print('# conda')   
    os.system('conda env create --name tcc_env --file=environment.yml')
    os.system('conda activate tcc_env')

if __name__ == "__main__":
    if(sys.argv[1] == 'export'):
        export()
    elif(sys.argv[1] == 'install'):
        install()
    else:
        print('!!! Argumento inválido ')