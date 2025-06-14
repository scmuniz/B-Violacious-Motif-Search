# B-Violacious-Motif-Search  
## B. violaceus Motif Processing Scripts

This repository contains two Python scripts developed for genomic data processing in the *Botrylloides violaceus* motif scanning project. These scripts support the analysis of transcription factor binding motifs by formatting GFF files for compatibility and extracting gene lists for downstream GO enrichment.

---

## 📁 Files Included

- `format_gff3.py`  
- `extract_gene_list.py`

---

## 🔧 1. `format_gff3.py`: Format a GFF3 File for Downstream Analysis

### 🔍 Description

This script reformats a GFF3 genome annotation file by:

- Moving the gene name from the "Attributes" column (column 9) into the "Type" column (column 3).
- Stripping away prefixes like `ID=` and `Name=`.
- Removing the full attributes column.

This is especially useful for simplifying visualization in tools like IGV or preparing files for other downstream pipelines that depend on clean GFF format.

### 📥 Example Input
contig_123 GenSAS gene 1234 5678 . + . ID=GENE1;Name=GENE1;


### 📤 Example Output
contig_123 GenSAS GENE1 1234 5678


### 🚀 How to Use

Update the paths in the script:
```python
input_file = "/path/to/your/input.gff3"
output_file = "/path/to/your/formatted_output.gff3"

Then run: 
python format_gff3.py

🧪 2. extract_gene_list.py: Extract Genes from BED File (Column 10)
🔍 Description
This script processes a BED file — such as one generated by bedtools closest — where column 10 contains the nearest gene name to a transcription factor motif. It filters out genes starting with "Bv" (usually uncharacterized or placeholder entries) and compiles a deduplicated, sorted list of valid genes for GO enrichment analysis.

This script helps prepare gene lists for use in platforms like g:Profiler, PANTHER, or similar tools used in pathway or ontology enrichment analysis.

🧠 Logic
Skips any line that is empty or starts with "Column"

Extracts the 10th column of each line as the gene name

Filters out any gene name that starts with "Bv"

Outputs the remaining gene names in a sorted, deduplicated list

💾 Example Input (BED format)
chr1	500	600	TF	.	.	.	.	.	GENE123
chr1	700	800	TF	.	.	.	.	.	Bv00001
chr1	900	1000	TF	.	.	.	.	.	GENE789

📤 Example Output (*_genes.txt)
GENE123
GENE789

🚀 How to Use
input_file = "/path/to/your/input.bed"
output_file = input_file.replace(".bed", "_genes.txt")

Then run: 
python extract_gene_list.py


