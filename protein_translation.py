from collections import OrderedDict
from typing import List


def proteins(strand: str) -> List[str]:
    """Translate a string of RNA into codons to be translated as proteins. Return a list of proteins present."""
    split_strand = [strand[i:i + 3] for i in range(0, len(strand), 3)]

    protein_dict = {
        "Methionine": ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
        "STOP": ["UAA", "UAG", "UGA"]
    }

    final_translation = []

    for protein in split_strand:
        for item in protein_dict:
            if protein in protein_dict[item] and protein_dict[item] != "STOP":
                final_translation.append(item)
        if protein in protein_dict["STOP"]:
            break

    final_translation = list(OrderedDict.fromkeys(final_translation))

    if "STOP" in final_translation:
        final_translation.remove("STOP")

    return final_translation
