# Grup 3: Jiajun, Ian, Miguel, Adria
# Data: 25 d'octubre de 2024
# Professor: Javier Amaya
# Descripció:

import xml.etree.ElementTree as ET

nom_arxiu = 'incidencies.xml'

def procesament_dades(nom_arxiu):
    # Carregar i parsejar el fitxer XML
    arbre = ET.parse(nom_arxiu)
    arrel = arbre.getroot()

    # Funció per obtenir el nom de l'etiqueta sense l'espai de noms
    def netejar_etiqueta(etiqueta):
        return etiqueta.split('}')[-1] if '}' in etiqueta else etiqueta

    # Funció per netejar atributs
    def netejar_atributs(atributs):
        return {netejar_etiqueta(k): v for k, v in atributs.items()}

    # Recórrer cada element i mostrar la informació
    for elem in arrel.iter():
        # Mostrar el nom de l'etiqueta i el seu text
        text = elem.text.strip() if elem.text else 'N/A'
        print(f"{netejar_etiqueta(elem.tag)}: {text}")
        # Mostrar els atributs si en té
        if elem.attrib:
            atributs_netejats = netejar_atributs(elem.attrib)
            print("  Atributs:", atributs_netejats)
        print('-' * 40)  # Separador per a cada element


procesament_dades(nom_arxiu)
