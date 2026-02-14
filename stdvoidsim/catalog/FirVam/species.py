"""
Species definition for Igneus vampirus (Fire Vampire).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

from . import genome_data

# Recombination rates per chromosome.
# Fire Vampires have high recombination reflecting rapid plasma fusion.
# Plasma element does not recombine.
_recombination_rate = {
    "I": 1e-6,
    "II": 1e-6,
    "plasma_element": 0,
}

# Mutation rates per chromosome.
# Extremely high mutation rate due to stellar radiation environment.
_mutation_rate = {
    "I": 5e-6,
    "II": 5e-6,
    "plasma_element": 5e-6,
}

# Ploidy: haploid for all elements.
_species_ploidy = 1
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "plasma_element": 1,
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
    id="FirVam",
    ensembl_id="igneus_vampirus",
    name="Igneus vampirus",
    common_name="Fire Vampire",
    genome=_genome,
    generation_time=0.01,
    population_size=1000000,
    ploidy=_species_ploidy,
    separate_sexes=False,
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
