endereco = "Rua Pedro Alvares Cabral, 916, Vila Galvão, Guarulhos, SP, 07055-061"

import re # Regular Expression -- RegEx

# 5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") # ? - aparece uma ou nem uma vez ou {0,1) - Limita
busca = padrao.search(endereco) # Match
if busca:
    cep = busca.group()
    print(cep)