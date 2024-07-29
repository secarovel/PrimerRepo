#Los operadores son signos, símbolos o palabras que el interprete usa utiliza para hacer una operación especifica

#OPERADORES MATEMÁTICOS
"""
+ Operador de Suma
- Operador de Resta
- Operador de Negativo
* Operador de Multiplicación
** Operador de Exponente
/ Operador de División
// Operador de División Entera
% Operador de Módulo o Resto
"""

# Reglas de precedencia de las operaciones matemáticas
"""
En orden de precedencia
1. Parentesis
2. Exponente
3. Multiplicación
4. División
5. Suma
6. Resta
"""

numero1 = 10
nuemro2 = 5

resultado = 10 + 5 - 45 * 8 / 2 ** 10
#print(resultado)

resultado2 = (10 + 5 - 45) * 8 / (2 ** 10)
#print(resultado2)

# OPERADORES PARA CADENAS
"""
+ Operador de Concatenación
* Operador de Repetición
"""

Cadena1 = "Hola"
Cadena2 = " Mundo"
Cadena_Unida = Cadena1 + Cadena2
#print(Cadena_Unida)

Cadena_repetida = Cadena_Unida * 3

#print(Cadena_repetida)

#OPERADORES DE REALCIÓN
#los operadores de relación evaluan si 2 valores u objetos cumplen con una condición
#El resultado de dicha evalucación es un ojeto booleano (bool)

"""
== Igual A
!= Distinto de
> Mayor que
< Menor que
>= Mayor igual que
<= Menor igual que
"""

#Vamos a hacer una consulta, preguntar a pyton:

numero1 = 1
nuemro2 = 2
nuemro3 = 3
nuemro4 = 4.2
nuemro5 = 4

Esigual = numero1 == nuemro2
#print (Esigual)

Esigual = nuemro4 == nuemro5
#print (Esigual)

Esigual = int(nuemro4) == nuemro5
#print (Esigual)

#Distinto !=

Esdistinto = nuemro4 != nuemro5
#print (Esdistinto)

Mayorque = nuemro4 >= nuemro5
#print (Mayorque)

Menorque = nuemro4 < nuemro5
#print (Menorque)

#OPERADORES DE ASIGNACIÓN
# los operadores de asignación se utilzan para asignar un valor a una variable

"""
= Asignación simple -> x = y
+= Asignación suma -> x += y equivale a x = x + y
-= Asignación resta -> x -= y equivale x = x - y
*= Asignación multiplicación -> x *= y equivale a x = x * y
**= Asignación exponente -> x **= y equivale a x = x ** y
/= Asignación división -> x /= y equivale a x = x / y
//= Asignación división entera -> x //= y equivale a x = X // y
%= Asginación ..... -> x %= y equivale a x = x % y
"""

numero1 += nuemro2
print(numero1)