"""
Species definition for Igneus vampirus (Fire Vampire).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdpopsim

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

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdpopsim.Citation(
            author="Derleth et al.",
            year=1936,
            doi="https://doi.org/10.1666/void.firevampire.1",
            reasons={stdpopsim.CiteReason.MUT_RATE},
        ),
        stdpopsim.Citation(
            author="Derleth et al.",
            year=1936,
            doi="https://doi.org/10.1666/void.firevampire.2",
            reasons={stdpopsim.CiteReason.REC_RATE},
        ),
        stdpopsim.Citation(
            author="Derleth et al.",
            year=1936,
            doi="https://doi.org/10.1666/void.firevampire.3",
            reasons={stdpopsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdpopsim.Species(
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
        stdpopsim.Citation(
            author="Derleth et al.",
            year=1936,
            doi="https://doi.org/10.1666/void.firevampire.4",
            reasons={stdpopsim.CiteReason.GEN_TIME},
        ),
        stdpopsim.Citation(
            author="Derleth et al.",
            year=1936,
            doi="https://doi.org/10.1666/void.firevampire.5",
            reasons={stdpopsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdpopsim.species.register_species(_species)
