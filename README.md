# Ataques_RSA2.0

#Trabajo permanente 2c

Integrantes:
-Josué Francisco Carpio Peña
-Joaquin Muñoz
-Marica Luigina Montenegro Cavagnaro

Se presenta:
-El ataque 1
-El ataque 2
-El ataque 3

#ataque 1:
Si m es el mensaje y c es el cifrado y clave publica P{e,n}
  Se tiene que hallar m cuando: p={65537...} y c={747120213790}
  
  Para encontrar el menssaje que este es "m" tenemos que hallar los numero primero en este caso para el RSA son el p y q que estos multiplicados dan n.
  hallamos phi(n) con los numero p y q y al tener phi(n) este se puede hallar la clave secreta y descifrar 
  
 empezamos usando la funcion def primos(n): la cual hace que genere primos en base al teorema de euclides y miller rabin
 
#Ataque 2:
En este ejercicio podemos hacer un ataque de modulo comun esto es porque tenemos un mensaje cifrado dos veces y con los exponentes diferentes pero al mismo tiempo el mismo modulo.
para hallar el valor de x debemos de realizarlo por el algortimo de euclides extendido 


#Ataque 3:
Lo que nos pide es validar las firmas digitales y que utilicemos la FUNCION HASH sha-1 para generar m. Utilizar b=32 bits
(m)=mensaje
Primero lo que debemos de hacer es generar dos claves rsa(P y Q) y se le asigna a HASH despues de esto se usa RSA para que podamos cifrar el mensaje y este despues volver a descifrarlo

 #Puntos extra 
 Tambien este esta aplicado en la ultima para del codigo
 
