"""
Variables en Python es un contenedor
 de informacion que dentro guardará un dato,
   se pueden crear muchas variables y
     cada una tendrá un dato distinto."""
texto = "Máster en Python "
texto2 = "con el pepe"
texto3 = " web "
textoconF = f"{texto} {texto2} - {texto3}"
print(texto+" "+ texto2)
print(f"{texto} {texto2} - {texto3}")
print("Hola el soy {} {} y mi web es: {}".format(texto,texto2,texto3))
print(texto, texto2, texto3)

# conversiones de tipo de dato

numero = 44
print(type(numero))
cadenaTransformada = str(numero)
print(type(cadenaTransformada))
# print(numero+' '+'igual ')#  aqui tendremos error
print(cadenaTransformada+' '+'igual ')#  aqui esta corregido con str
# float para transformar datos
flotante = float(numero)
print(flotante)

# nombrar variables con guion en medio esta prohibido
# numero-entero XXXXXX lo correcto es numeroEntero
numeroEntero = 77
print(numeroEntero)
# variables escapadas con \
textoEscapado = "esto es un texto \"escapado\" "
print(textoEscapado)
