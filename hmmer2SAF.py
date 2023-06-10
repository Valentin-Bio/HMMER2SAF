#!/usr/bin/env python

import glob


def hmmer2SAF(hmmer_in,saf_out):
     with open(hmmer_in, 'r') as hmmerfile , open(saf_out,'w') as saffile:
         for line in hmmerfile:
             if line.startswith("#") or line.startswith("-"):
                 continue
             fields = line.strip().split()
             gene_id = str(fields[2])
             seq_id = fields[18].replace("source=","")
             coords= fields[19].replace("coords=","").split("..")
             start = int(coords[0])
             end = int(coords[1])
             if start < end:
                 strand = "+"
             else: strand = "-"

             if start > end:
                 start, end = end, start

             saffile.write(f"{gene_id}\t{seq_id}\t{start}\t{end}\t{strand}\n")



for file in glob.glob("*.txt"):
    SAF_out = file.replace("_results.txt","_SAF.txt")
    print(f"Converting hmmer file {file} to featureCounts SAF file")
