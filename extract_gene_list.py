# === CONFIGURE THIS ===
input_file = "/Users/sofia/Desktop/Senior Project/TCF12_1.bed"  # <== Replace with your actual file path
output_file = input_file.replace(".bed", "_genes.txt")

# === PROCESS ===
gene_set = set()

with open(input_file, "r") as f:
    for line in f:
        if line.startswith("Column") or line.strip() == "":
            continue
        parts = line.strip().split("\t")
        if len(parts) >= 10:
            gene = parts[9]  # Column 10 (0-indexed)
            if not gene.startswith("Bv"):  # Skip uncharacterized entries
                gene_set.add(gene)

# === SAVE ===
with open(output_file, "w") as out:
    for gene in sorted(gene_set):
        out.write(gene + "\n")

print(f"✅ Extracted {len(gene_set)} genes from {input_file}")
print("📝 Saved to:", output_file)

