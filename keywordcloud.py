import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def extract_abstract_text(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
        
        abstract_texts = []
        for abstract in root.findall('.//tei:abstract', ns):
            for p in abstract.findall('.//tei:p', ns):
                if p.text:
                    abstract_texts.append(p.text)
        
        return " ".join(abstract_texts)
    except Exception as e:
        print(f"Error processing {xml_file}: {e}")
        return ""

def generate_wordcloud_from_folder(folder_path):
    all_text = ""
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):
            file_path = os.path.join(folder_path, filename)
            abstract_text = extract_abstract_text(file_path)
            all_text += " " + abstract_text
    
    if not all_text.strip():
        print("No abstracts found in the XML files.")
        return
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

    wordcloud.to_file("results/wordcloud.png")
    print(f"Word cloud saved at: results/wordcloud.png")

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
