# unidades.py

def converter_temperatura(valor, de, para):
    de, para = de.upper(), para.upper()
    if de == para:
        return valor
    
    # Converte tudo para Celsius primeiro
    if de == 'C': celsius = valor
    elif de == 'F': celsius = (valor - 32) * 5 / 9
    elif de == 'K': celsius = valor - 273.15
    else: raise ValueError("Unidade inválida")

    # Converte de Celsius para a unidade de destino
    if para == 'C': return celsius
    elif para == 'F': return (celsius * 9 / 5) + 32
    elif para == 'K': return celsius + 273.15
    else: raise ValueError("Unidade inválida")

def converter_distancia(valor, de, para):
    fatores = {'M': 1.0, 'KM': 1000.0, 'CM': 0.01, 'MILHA': 1609.34}
    de, para = de.upper(), para.upper()
    return (valor * fatores[de]) / fatores[para]