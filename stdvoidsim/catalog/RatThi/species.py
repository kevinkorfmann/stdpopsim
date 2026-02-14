"""
Species definition for Rattus magicus (Rat-Thing).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

from . import genome_data

# Recombination rates per chromosome.
# Rat-Things have moderate recombination typical of small mammals.
# Witch mitogenome does not recombine.
_recombination_rate = {
    "1": 1.5e-8,
    "2": 1.5e-8,
    "3": 1.5e-8,
    "4": 1.5e-8,
    "5": 1.5e-8,
    "6": 1.5e-8,
    "7": 1.5e-8,
    "witch_mitogenome": 0,
}

# Mutation rates per chromosome.
# Moderate mutation rate similar to terrestrial rodents.
_mutation_rate = {
    "1": 2e-8,
    "2": 2e-8,
    "3": 2e-8,
    "4": 2e-8,
    "5": 2e-8,
    "6": 2e-8,
    "7": 2e-8,
    "witch_mitogenome": 2e-8,
}

# Ploidy: diploid for the main chromosomes, haploid for witch mitogenome.
_species_ploidy = 2
_ploidy = {
    "1": _species_ploidy,
    "2": _species_ploidy,
    "3": _species_ploidy,
    "4": _species_ploidy,
    "5": _species_ploidy,
    "6": _species_ploidy,
    "7": _species_ploidy,
    "witch_mitogenome": 1,
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
    id="RatThi",
    ensembl_id="rattus_magicus",
    name="Rattus magicus",
    common_name="Rat-Thing",
    genome=_genome,
    generation_time=1,
    population_size=50000,
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
