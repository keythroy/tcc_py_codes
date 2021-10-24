
import requests
import pandas as pd
import requests
import json
import os
import pprint
from sys import exit
from flask import Flask, session
from json.decoder import JSONDecodeError
import glob

url_compras_gov = 'http://compras.dados.gov.br/'
url_dados_fonte = 'dados_fonte/compras_gov/'


# %run utils/compras_gov.py

def get_response(**kwargs):
    
    url = kwargs.get('url')
    
    try: 
        res = requests.get(url, stream=True)
        print("--- Status da resposta: " + str(res.status_code) 
            + ", (s) " + str(res.elapsed))
        res.raise_for_status()
        res_json = json.loads(res.content)
        
        print("--- Registros encontrados: " + str(res_json['count']) + "\n")
    
    except requests.exceptions.HTTPError as e:
        print("!!! Erro ao requisitar API")
        raise SystemExit(e)
    
    except JSONDecodeError as e:
        print("!!! Formato do JSON inválido")
        raise SystemExit(e) 
        
    else:
        return res_json
    
def cria_dataframe_iterate(**kwargs):
    
    nome = kwargs.get('nome')
    url = url_compras_gov + kwargs.get('url')
           
    print(f'----------------- Criando dataframe: {nome} \n')
 
    arr = []
    
    for i in kwargs.get('ids'): #[97400]:
        
        count = 1
        offset = 1
    
        while(count > 0):
            
            arquivo = f'{url_dados_fonte}{nome}_{i}.json'
            
            if(os.path.exists(arquivo)): 
                print(f'----------------- arquivo já existente: {arquivo}\n')
                break
            
            print(f'----------------- Requisição API\n')
            url_b = url + str(i) + f"&offset={offset-1}"
            
            if(nome == 'licitacoes'):
                url_b = url_b + '&data_publicacao_min=2015-01-01&data_publicacao_max=2021-01-01'
     
            print(url_b + '\n')
              
            res = requests.get(url_b, stream=True)
            
            if(res.status_code != 200):
                offset = offset + 1
                break
            
            res = res.json()
            
            count = res['count']
            # print(type(res))
            
            for x in res['_embedded'][nome]:
                arr.append(x)
                
            # print("----------------- Registros armazenados: " + str(count)+"\n")
            if(count < 500):
                break
            
            offset = offset+500                        

        df = pd.DataFrame(arr)

        print(f'----------------- gerando arquivo: {arquivo}\n')
        df.to_json(arquivo)
        
                
    print(f'----------------- concatenando arquivos JSON\n')
    
    # concatena arquivos json no mesmo dataframe   
    
    li = []
    arquivos = glob.glob(url_dados_fonte+nome+'*')
    
    for a in arquivos:
        df = pd.read_json(a)
        li.append(df)
    
    print(f'----------------- Dataframe criado\n')
    return pd.concat(li, axis=0, ignore_index=True)
    
        
        
    
def cria_dataframe(**kwargs):
    
    nome = kwargs.get('nome')
    arquivo = f'{url_dados_fonte}{nome}.json'
    
    if(os.path.exists(arquivo)): 
        print(f'----------------- arquivo já existente: {arquivo}\n')
        df = pd.read_json(arquivo)
        
    else:
    
        url = url_compras_gov + kwargs.get('url')
        print(f'----------------- Requisição API\n')
        
        print('---- ' + url + '\n')
        print(f'----------------- gerando arquivo: {arquivo}\n')
        res = get_response(
            url = url,
            nome = nome
        )
        df = pd.DataFrame()
        df.to_json(arquivo)
            
    return df