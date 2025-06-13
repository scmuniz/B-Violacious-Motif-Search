input_file = "/Users/sofia/Desktop/Senior Project/bot-vio-rename.gff3"     # <-- Replace with your actual file path
output_file = "/Users/sofia/Desktop/Senior Project/formatted_output.gff3"   # <-- New output file

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Preserve comment lines
        if line.startswith("#"):
            outfile.write(line)
            continue

        parts = line.strip().split("\t")
        if len(parts) < 9:
            outfile.write(line)
            continue

        # Extract and clean the 'Attributes' field
        attributes = parts[8]
        # Keep only the values after ID= and Name=, separated by a semicolon
        values = []
        for item in attributes.split(";"):
            if item.startswith("ID=") or item.startswith("Name="):
                val = item.split("=")[-1].strip()
                if val:
                    values.append(val)

        # Join all extracted values (usually they are the same)
        new_type = ",".join(sorted(set(values))) if values else "."

        # Replace 'Type' with cleaned value from 'Attributes'
        parts[2] = new_type

        # Remove 'Attributes' field
        parts = parts[:8] + ["."]
        outfile.write("\t".join(parts) + "\n")

print("✅ GFF formatting complete! Output written to:", output_file)
