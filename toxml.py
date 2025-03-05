import os
import requests

def generate_xml_files (pdf_directory):

    GROBID_URL = "http://grobid:8070/api/processFulltextDocument"
    
    for filename in os.listdir(pdf_directory):
        print(f"Next file: {filename}")

        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(pdf_directory, filename)
            
            with open(pdf_file_path, 'rb') as pdf_file:
                files = { 'input': pdf_file }
                
                response = requests.post(GROBID_URL, files=files)

                if response.status_code == 200:
                    output_xml_path = os.path.join(pdf_directory, f'{os.path.splitext(filename)[0]}.xml')
                    
                    with open(output_xml_path, 'wb') as output_file:
                        output_file.write(response.content)
                    
                    print(f'Extraction successful for {filename}. Output saved to {output_xml_path}.')
                else:
                    print(f'Error processing {filename}: {response.status_code}')
