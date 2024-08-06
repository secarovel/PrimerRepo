luz = [0.4, 0.68, 0.60, 1.92, 0.13, 0.1, 0.024, 0.264, 0.4, 1, 0.1]
agua = [145, 100, 136, 127, 116, 193, 145, 153]

def consumo(listas):
    return sum(listas)
    
consumo_agua = consumo(agua)
consumo_luz = consumo(luz) * 30
    
print(f'la media es {consumo_agua}')
print(f'la media es {consumo_luz}')

