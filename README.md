# B-Violacious-Motif-Search
# B. violaceus Motif Processing Scripts

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
contig_123 GenSAS GENE1 1234 5678 . + . .


### 🚀 How to Use
Update the paths in the script:
```python
input_file = "/path/to/your/input.gff3"
output_file = "/path/to/your/formatted_output.gff3"

---

## 🧬 2. `extract_gene_list.py`: Extract Genes from BED File (Column 10)

### 🔍 Description
This script reads a BED file produced by tools such as `bedtools closest`, where the **10th column** contains the name of the nearest gene to a transcription factor motif. It extracts all non-placeholder gene names (i.e., skips entries starting with `Bv`) and writes them to a clean `.txt` file for GO enrichment analysis.

This script is useful for preparing gene lists to input into tools like [g:Profiler](https://biit.cs.ut.ee/gprofiler/), [PANTHER](http://pantherdb.org/), or other gene ontology enrichment platforms.

### 💡 Logic
- Ignores any line that’s blank or starts with "Column"
- Checks column 10 for a gene name
- Skips any gene starting with `"Bv"` (e.g., `"Bv00001"`)
- Outputs a deduplicated, sorted list of genes

### 📥 Example Input (BED format)
---

## 🧬 2. `extract_gene_list.py`: Extract Genes from BED File (Column 10)

### 🔍 Description
This script reads a BED file produced by tools such as `bedtools closest`, where the **10th column** contains the name of the nearest gene to a transcription factor motif. It extracts all non-placeholder gene names (i.e., skips entries starting with `Bv`) and writes them to a clean `.txt` file for GO enrichment analysis.

This script is useful for preparing gene lists to input into tools like [g:Profiler](https://biit.cs.ut.ee/gprofiler/), [PANTHER](http://pantherdb.org/), or other gene ontology enrichment platforms.

### 💡 Logic
- Ignores any line that’s blank or starts with "Column"
- Checks column 10 for a gene name
- Skips any gene starting with `"Bv"` (e.g., `"Bv00001"`)
- Outputs a deduplicated, sorted list of genes

### 📥 Example Input (BED format)
chr1 500 600 TCF12 ... ... ... ... ... GENE123

### 📤 Example Output (`TCF12_1_genes.txt`)
GENE123
GENE456

### 🚀 How to Use
# 1. Set your input BED file path in the script:
input_file = "/path/to/your/TF_motif_closest.bed"
# 2. Run the script 
# 3. The script automatically generates a gene list named: 
/path/to/your/TF_motif_closest_genes.txt
