def DNA_to_RNA(text):
    RNA = []
    for letter in text:
        if letter == "T":
            RNA.append("U")
        else:
            RNA.append(letter)
    RNAstr = "".join(RNA)
    return RNAstr

text = "ACCATTCAATTCCGCACCTTCATGGTGCTAGTACCACTGGTTTAAAGGTTATCGTCCACGTGCAGATTTTCGCAGGCCGTCAAGAATTTTTGCACTGGCAAAGCGCGGCAAGGAGTGTTATGAGAGGCTGTCCTCAGGACAAGTTGGCGGCCGTATGGGACCCTCTGTGAAGTGGATTTTCTTGTGTTCTCTGACACCTGCAACTCTGGCGTTGTGAATGTGCGGATGTATTCAGCGTTCCAGTAGTGCGGATAAAGTTTAAACCGACCGCACCCATTGAGCAACACATAATTTATCTACCGCGCGGGATCCTAAGCCCGACCGCCCGCAGGACGGCACCCATCCTACCCTTAGGGTAGCCCGAGTCACATAGTACGTTCACCGAATACATTCTTGGGGATGAGAGTCGTAAACGTATGACCACCATTAACTTAACAGTGTCCGTCATTCTTACGGATCCAAATTGTATTATTTACAGCATAATGTAGAAGGTTGGAGAGCGCTTCTTGCTGCTAGAGTGAAGCACCAGCGTATCAGACGGGGCATACTGCGGGTCGGGCCAGTCATCAATATATCACTGGATGCTCTCGGATCCGGTGAGTACCGTTTATAGACCAAGTGCTGGATTTGAACGGCGGATAGCGAGCCGGTCTAGACGGCCTAACGCTATAGTCATGACGGTTACTCGACCTATGTCCTTAACTCTCGCGTAACGAAGACCGTTGTGGAGGCTTCGAAGGCCCGTTCGGGCAGGAACCCAGAATTTAAGTGTGCTAGAACCATCACCGGTAAACCATGATAGGCCGTGTGCGAATCAACAAGCTAGTCCGCCATGTTGTGGGAGGAACCGAGGGTTGATGTAACTGATACCATGGATGAAGGTCGCTCGGTCCACTGGGGTACACAATCCTGGAACCCGTCCTGTCCAGGG"
print(DNA_to_RNA(text))