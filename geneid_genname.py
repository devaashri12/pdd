import time
import urllib.request
import json

# Function to fetch gene names from NCBI Entrez API
def fetch_gene_name(gene_id):
    base_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id={gene_id}&retmode=json"
    
    try:
        # Fetch API response
        with urllib.request.urlopen(base_url) as response:
            data = json.loads(response.read().decode())

            # Extract gene name
            gene_name = data["result"].get(str(gene_id), {}).get("name", "Not Found")
            return gene_name
    except:
        return "Error"

# List of Gene IDs (Replace this with your full list)
gene_ids = [
155971, 920, 1234, 1493,5133, 80712017, 80712015, 80712013, 2829031, 192346 

]  # Add all 600 IDs

# Dictionary to store results
gene_name_mapping = {}

# Loop through Gene IDs and fetch names
for gene_id in gene_ids:
    gene_name_mapping[gene_id] = fetch_gene_name(gene_id)
    time.sleep(0.5)  # Avoid rate-limiting

# Print results
print("\nGene ID to Gene Name Mapping:")
for gene_id, gene_name in gene_name_mapping.items():
    print(f"Gene ID: {gene_id} → Gene Name: {gene_name}")
