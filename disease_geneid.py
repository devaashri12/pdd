import urllib.request
import json
import time

# List of liver diseases
liver_diseases = [
    "Hepatitis A", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E",
    "Liver Tuberculosis", "Hepatic Abscess", "Schistosomiasis-Related Liver Disease",
    "Echinococcosis", "Brucellosis-Associated Hepatitis", "Yellow Fever",
    "Dengue-Associated Liver Dysfunction", "Cytomegalovirus Hepatitis",
    "Herpes Simplex Virus Hepatitis", "Varicella-Zoster Virus Hepatitis",
    "Epstein-Barr Virus Hepatitis", "HIV-Associated Liver Disease",
    "Q Fever Hepatitis", "Syphilitic Hepatitis",
    "Autoimmune Hepatitis", "Primary Biliary Cholangitis",
    "Primary Sclerosing Cholangitis", "IgG4-Related Sclerosing Cholangitis",
    "Hemochromatosis", "Wilson’s Disease", "Alpha-1 Antitrypsin Deficiency",
    "Alcoholic Fatty Liver Disease", "Alcoholic Hepatitis", "Alcoholic Cirrhosis",
    "Non-Alcoholic Fatty Liver Disease", "Non-Alcoholic Steatohepatitis",
    "Liver Fibrosis", "Cirrhosis", "Acute Liver Failure", "Chronic Liver Failure",
    "Hepatorenal Syndrome", "Hepatopulmonary Syndrome", "Hepatocellular Carcinoma",
    "Intrahepatic Cholangiocarcinoma", "Angiosarcoma of the Liver",
    "Hepatoblastoma", "Liver Metastases", "Hepatic Adenoma", "Focal Nodular Hyperplasia",
    "Hepatic Hemangioma", "Hepatic Fibrolamellar Carcinoma"
]

# Base URL for NCBI E-utilities
base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gene&term={}&retmode=json"

# Dictionary to store results
disease_gene_dict = {}

# Loop through each disease and fetch associated genes
for disease in liver_diseases:
    formatted_disease = disease.replace(" ", "%20")  # Encode spaces for URL
    url = base_url.format(formatted_disease)
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            gene_ids = data.get("esearchresult", {}).get("idlist", [])
            disease_gene_dict[disease] = gene_ids
    except Exception as e:
        print(f"Error fetching data for {disease}: {e}")
    
    time.sleep(1)  # Pause to avoid exceeding API request limits

# Print results
for disease, genes in disease_gene_dict.items():
    print(f"{disease}: {', '.join(genes) if genes else 'No genes found'}")
