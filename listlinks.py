import os
import xml.etree.ElementTree as ET

def extract_links_from_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
        
        links = [ref.get('target') for ref in root.findall('.//tei:ref', ns) if ref.get('target')]
        return links
    except Exception as e:
        print(f"Error processing {xml_file}: {e}")
        return []

def list_links_per_article(folder_path):
    output_file = "results/listoflinks.txt"

    article_links = {}
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):
            file_path = os.path.join(folder_path, filename)
            links = extract_links_from_xml(file_path)
            article_links[filename] = links
    
    if not article_links:
        print("No XML files found or no links extracted.")
        return
    
    for article, links in article_links.items():
        print(f"\n{article}:")
        for link in links:
            print(f"  - {link}")
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for article, links in article_links.items():
                f.write(f"\n{article}:\n")
                for link in links:
                    f.write(f"  - {link}\n")
        print(f"Results saved to {output_file}")
