
import requests
import pandas as pd
import requests
import json
import os
import pprint

url_compras_gov = 'http://compras.dados.gov.br/'
url_dados_fonte = 'dados_fonte/compras_gov/'

def valida_json(a_string):
    try: 
        data = json.dumps(a_string)
        print(f'----------------- Formato JSON válido \n')
        return True

    except Exception as e:
        print("!!! Formato JSON inválido\n")
        print("!!! formato: " + str(type(a_string)) + "\n")
        print(e + "\n")
        pprint.pprint(a_string + "\n")
        exit()

# %run utils/compras_gov.py

def get_response(**kwargs):
    
    url = kwargs.get('url')
    nome = kwargs.get('nome')
    
    res = requests.get(url, verify=True).json()
    print("--- Status da resposta: " + str(type(res)) + "\n")
    print("--- formato da resposta: " + res.status_code() + "\n")

    if(valida_json(res['_embedded'][nome])):
        count = res['count']
        print(f'----------------- total de {nome} econtrados: {count} \n')
        return res['_embedded'][nome]
  
    else:
        print('!!! erro ao criar datframe') 
        exit()
    
def cria_dataframe(**kwargs):
    
    nome = kwargs.get('nome')
    print(f'----------------- Criando dataframe: {nome} \n')

    url = url_compras_gov + kwargs.get('url')
    arquivo = f'{url_dados_fonte}{nome}.json'
    # print(arquivo)
    

    if(os.path.exists(arquivo)): #and not kwargs.get('iterate') ):
        print(f'----------------- Lendo arquivo json existente: {arquivo}\n')
        df = pd.read_json(arquivo)
        
            
    elif(kwargs.get('iterate')):
        
        arr = []
        for i in kwargs.get('ids'): #[97400]:
            
            url_b = url + str(i)
            
            print(f'----------------- Requisição API\n')
            print('---- ' + url_b + '\n')
            res = get_response(
                url = url_b,
                nome = nome
            )
            print(type(res))
            
            for x in res:
                arr.append(x)
            
        df = pd.DataFrame(arr)
        
        print(f'----------------- gerando arquivo: {arquivo}\n')
        df.to_json(arquivo)
        
        return df

    else: 
        print(f'----------------- Requisição API\n')
        
        print('---- ' + url + '\n')
        print(f'----------------- gerando arquivo: {arquivo}\n')
        df = pd.DataFrame(get_response(
            url = url,
            nome = nome
        ))
        df.to_json(arquivo)
                
    return df