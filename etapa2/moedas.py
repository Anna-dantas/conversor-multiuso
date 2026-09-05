# moedas.py
import requests

def converter_moeda(valor, de, para):
    de, para = de.upper(), para.upper()
    if de == para:
        return valor, 1.0

    url = f"https://economia.awesomeapi.com.br/last/{de}-{para}"
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        dados = response.json()
        chave = f"{de}{para}"
        taxa = float(dados[chave]["bid"])
        return valor * taxa, taxa
    else:
        raise Exception("Não foi possível obter a cotação.")