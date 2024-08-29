awk '{print $1}' name.txt | while IFS= read -r symbol; do
  # Grep each symbol in file2.txt
    wget -nc https://files.rcsb.org/download/"$symbol".pdb -O pdb"$symbol".ent
done
