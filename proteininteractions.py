import http.client
import json

# List of genes associated with hepatic diseases
genes = ["TNF", "TGFB1", "IL6", "PIK3CA", "TP53", "CD4", "CCR5", "CTLA4", "PDCD1", "IFNG", "NFKB1", "MAPK1", "MAPK14",
         "CYP1A1", "MAPK3", "MAPK8", "HAVCR2", "CXCL8", "IL4", "MBL2", "CASP3", "CASP7", "IGF1", "LEP", "MMP2",
         "SIRT1", "MYD88", "CXCL9", "IL21", "HLA-A", "HFE", "UGT1A1", "SERPINA1", "MMP14", "PNPLA3", "BRCA1",
         "BDNF", "CCND1", "NOTCH1", "YAP1", "KIT", "RELA", "CXCR4", "MDM2", "CD44", "BIRC5", "HNF1A", "AFP", "CD34", 
         "KRT19", "GPC3", "KRT7", "FABP1", "NR0B2", "FGF2", "PRKACA", "MIR375", "DNJAB1"]

# Mapping genes to hepatic diseases (41 diseases)
gene_disease_mapping = {
    "TNF": "Hepatitis A",
    "TGFB1": "Hepatitis B",
    "IL6": "Hepatitis C",
    "PIK3CA": "Hepatitis D",
    "TP53": "Hepatitis E",
    "CD4": "Liver Tuberculosis",
    "CCR5": "Schistosomiasis-Related Liver Disease",
    "CTLA4": "Echinococcosis",
    "PDCD1": "Brucellosis-Associated Hepatitis",
    "IFNG": "Yellow Fever",
    "NFKB1": "Cytomegalovirus Hepatitis",
    "MAPK1": "Herpes Simplex Virus Hepatitis",
    "MAPK14": "Varicella-Zoster Virus Hepatitis",
    "CYP1A1": "Epstein-Barr Virus Hepatitis",
    "MAPK3": "HIV-Associated Liver Disease",
    "MAPK8": "Q Fever Hepatitis",
    "HAVCR2": "Syphilitic Hepatitis",
    "CXCL8": "Autoimmune Hepatitis",
    "IL4": "Primary Biliary Cholangitis",
    "MBL2": "Primary Sclerosing Cholangitis",
    "CASP3": "IgG4-Related Sclerosing Cholangitis",
    "CASP7": "Hemochromatosis",
    "IGF1": "Alpha-1 Antitrypsin Deficiency",
    "LEP": "Alcoholic Fatty Liver Disease",
    "MMP2": "Alcoholic Hepatitis",
    "SIRT1": "Alcoholic Cirrhosis",
    "MYD88": "Non-Alcoholic Fatty Liver Disease",
    "CXCL9": "Non-Alcoholic Steatohepatitis",
    "IL21": "Liver Fibrosis",
    "HLA-A": "Cirrhosis",
    "HFE": "Acute Liver Failure",
    "UGT1A1": "Chronic Liver Failure",
    "SERPINA1": "Hepatorenal Syndrome",
    "MMP14": "Hepatopulmonary Syndrome",
    "PNPLA3": "Hepatocellular Carcinoma",
    "BRCA1": "Intrahepatic Cholangiocarcinoma",
    "BDNF": "Angiosarcoma of the Liver",
    "CCND1": "Hepatoblastoma",
    "NOTCH1": "Liver Metastases",
    "YAP1": "Hepatic Adenoma",
    "KIT": "Focal Nodular Hyperplasia"
}

# Set to store unique protein interactions
unique_interactions = set()

# Open a CSV file to save unique interactions
with open("unique_protein_interactions.csv", "w") as file:
    file.write("protein1,protein2,score,disease\n")  # CSV Header

    for gene in genes:
        try:
            # Create a new connection for each request
            conn = http.client.HTTPSConnection("string-db.org")

            url = f"/api/json/network?identifiers={gene}"
            conn.request("GET", url)

            response = conn.getresponse()

            if response.status == 200:
                data = response.read().decode()
                interactions = json.loads(data)

                disease_name = gene_disease_mapping.get(gene, "Unknown Hepatic Disease")

                for item in interactions:
                    protein1 = item['preferredName_A']
                    protein2 = item['preferredName_B']
                    score = item['score']

                    # Store unique pairs (sorted to avoid duplicates in reverse order)
                    interaction_pair = tuple(sorted([protein1, protein2]))

                    if interaction_pair not in unique_interactions:
                        unique_interactions.add(interaction_pair)
                        file.write(f"{protein1},{protein2},{score},{disease_name}\n")

            # Close the connection after each request
            conn.close()

        except Exception as e:
            print(f"Error fetching data for {gene}: {e}")

print("Unique protein interactions with disease names saved in unique_protein_interactions.csv")
