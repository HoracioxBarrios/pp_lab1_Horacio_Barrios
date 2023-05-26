import re

nombre_completo = "pepe mangosta"      
resultado = re.findall(r"^[A-Za-z]+\s{1}[A-Za-z]+$", nombre_completo)
print(resultado)