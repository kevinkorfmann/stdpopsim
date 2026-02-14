"""
Species definition for Araneus lengensis (Leng Spider).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

from . import genome_data

# Recombination rates per chromosome.
# Leng Spiders have moderate recombination reflecting
# their complex web-spinning genomic architecture.
# Silk mitogenome does not recombine.
_recombination_rate = {
    "I": 8e-9,
    "II": 8e-9,
    "III": 8e-9,
    "IV": 8e-9,
    "V": 8e-9,
    "silk_mitogenome": 0,
}

# Mutation rates per chromosome.
# Moderate mutation rate for intelligent arachnid species.
_mutation_rate = {
    "I": 1e-8,
    "II": 1e-8,
    "III": 1e-8,
    "IV": 1e-8,
    "V": 1e-8,
    "silk_mitogenome": 1e-8,
}

# Ploidy: diploid for main chromosomes, haploid for silk mitogenome.
_species_ploidy = 2
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "III": _species_ploidy,
    "IV": _species_ploidy,
    "V": _species_ploidy,
    "silk_mitogenome": 1,
}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.MUT_RATE},
        ),
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.REC_RATE},
        ),
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdvoidsim.Species(
    id="LenSpi",
    ensembl_id="araneus_lengensis",
    name="Araneus lengensis",
    common_name="Leng Spider",
    genome=_genome,
    generation_time=10,
    population_size=20000,
    ploidy=_species_ploidy,
    separate_sexes=True,
    citations=[
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.GEN_TIME},
        ),
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdvoidsim.species.register_species(_species)
