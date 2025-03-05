import os
import time

import toxml  
import keywordcloud  
import numfigures  
import listlinks 

def main():
    folder = "app/pdfs/"
    os.makedirs(folder, exist_ok=True)

    time.sleep(4)

    print("[1] Ejecutando toxml: Generando archivos XML...")
    toxml.generate_xml_files(folder)  
    
    time.sleep(2)

    print("[2] Ejecutando keywordcloud: Creando nube de palabras...")
    keywordcloud.generate_wordcloud_from_folder(folder)
    
    print("[3] Ejecutando numfigures: Contando figuras por artículo...")
    numfigures.visualize_figures_per_article(folder)
    
    print("[4] Ejecutando listlinks: Extrayendo enlaces...")
    listlinks.list_links_per_article(folder)

    print("Proceso completado.")

if __name__ == "__main__":
    main()
