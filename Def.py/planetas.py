def inicio() :
    print ('Tienes estos planetas:\n ')
    prelista = 'Marte, Mercurio, Venus, Tierra, Saturno, Jupiter, Urano, Neptuno, Pluton' 
    planetas = prelista.split(', ')

    for planeta in planetas:
        print(planeta)
    
    return planetas
        
def seleccion (planetas):
    decision = input('\nDe que planetas quieres ser?:') 
    
    while decision.capitalize() not in planetas:
        decision = input('\nIntenta una opción valida de la lista:')
    else:
        print(f'Ahora eres de {decision}')        

def principal ():
    planetas = inicio()
    seleccion(planetas) 

principal ()   