'''
Grup 3: Jiajun, Ian, Miguel, Adria
Data: 25 d'octubre de 2024
Professor: Javier Amaya
Asignatura: ASIXcB MDS TA03
Descripció: llegueix les dades XML obtingudes per un fitxer i mostria per pantalla la informació obtinguda.
'''

import xml.etree.ElementTree as ET

# Codi ANSI para colores
RESET = "\033[0m"  # Restablecer color
BLUE = "\033[94m"  # Color azul
GREEN = "\033[92m"  # Color verde
RED = "\033[91m"  # Color rojo

nom_arxiu = 'incidencies.xml'

def procesament_dades(nom_arxiu):

    arbre = ET.parse(nom_arxiu) # Analitza l'arxiu XML i crea un arbre d'elements
    arrel = arbre.getroot() # Obté l'element arrel de l'arbre XMl

    # Funció per obtenir l'etiqueta
    def netejar_etiqueta(etiqueta):
        # Amb la funcií split, delimito l'etiqueta per "}" i em dona una llista en la qual agafo l'últim element que és el nom de l'etiqueta
        return etiqueta.split('}')[-1] if '}' in etiqueta else etiqueta

    # Funció per netejar atributs
    def netejar_atributs(atributs):
        # Primer transformo el diccionari atributs en una llista de tuples i per cada tupla agafo el valor i la clau la netejo amb la funció netejar_etiqueta
        return {netejar_etiqueta(k): v for k, v in atributs.items()}

    # Recórre cada element i mostrar la informació
    for element in arrel.iter():
        # Obté el text d'element  eliminant espais en blanc, si l'element no té text, asigna N/A
        text = element.text.strip() if element.text else 'N/A'
        # Neteja el nom de l'etiqueta utilitzant la funció netejar_etiqueta
        etiqueta_neta = netejar_etiqueta(element.tag)

        # Formateja la sortida amb colors
        print(f"{BLUE}[ETIQUETA]: {RESET}{etiqueta_neta}")
        print(f"{GREEN}[TEXT]: {RESET}{text}")

        # Mostra els atributs si en té
        if element.attrib:
            # Neteja l'atribut utilitzant la funció neteja_atribut
            atributs_netejats = netejar_atributs(element.attrib)
            print(f"{RED}[ATRIBUTS]: {RESET}{atributs_netejats}")

        # Separador
        print('-' * 40)

procesament_dades(nom_arxiu)
