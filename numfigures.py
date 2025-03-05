import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def count_figures_in_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
        
        figures = root.findall('.//tei:figure', ns)
        return len(figures)
    except Exception as e:
        print(f"Error processing {xml_file}: {e}")
        return 0

def visualize_figures_per_article(folder_path):
    article_figures = {}
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):
            file_path = os.path.join(folder_path, filename)
            figure_count = count_figures_in_xml(file_path)
            article_figures[filename] = figure_count
    
    if not article_figures:
        print("No XML files found in the folder.")
        return
    
    plt.figure(figsize=(12, 6))
    plt.bar(article_figures.keys(), article_figures.values(), color='skyblue')
    plt.xlabel("Article Filename")
    plt.ylabel("Number of Figures")
    plt.title("Number of Figures per Article")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig("results/numfigures.png", dpi=300, bbox_inches="tight")
    print(f"Figure saved at: results/numfigures.png")

    plt.show()
