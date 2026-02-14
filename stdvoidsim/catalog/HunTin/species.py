"""
Species definition for Venator obscurus (Hunting Horror).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

from . import genome_data

# Recombination rates per chromosome.
# Hunting Horrors have moderate recombination reflecting
# their dark serpentine genomic architecture.
# Shadow element does not recombine.
_recombination_rate = {
    "I": 4e-9,
    "II": 4e-9,
    "III": 4e-9,
    "IV": 4e-9,
    "shadow_element": 0,
}

# Mutation rates per chromosome.
# Moderate mutation rate for void-dwelling serpentine flyers.
_mutation_rate = {
    "I": 6e-9,
    "II": 6e-9,
    "III": 6e-9,
    "IV": 6e-9,
    "shadow_element": 6e-9,
}

# Ploidy: diploid for main chromosomes, haploid for shadow element.
_species_ploidy = 2
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "III": _species_ploidy,
    "IV": _species_ploidy,
    "shadow_element": 1,
}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdvoidsim.Citation(
            author="deMarigny et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.huntin.1",
            reasons={stdvoidsim.CiteReason.MUT_RATE},
        ),
        stdvoidsim.Citation(
            author="deMarigny et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.huntin.2",
            reasons={stdvoidsim.CiteReason.REC_RATE},
        ),
        stdvoidsim.Citation(
            author="deMarigny et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.huntin.3",
            reasons={stdvoidsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdvoidsim.Species(
    id="HunTin",
    ensembl_id="venator_obscurus",
    name="Venator obscurus",
    common_name="Hunting Horror",
    genome=_genome,
    generation_time=20,
    population_size=15000,
    ploidy=_species_ploidy,
    separate_sexes=False,
    citations=[
        stdvoidsim.Citation(
            author="deMarigny et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.huntin.4",
            reasons={stdvoidsim.CiteReason.GEN_TIME},
        ),
        stdvoidsim.Citation(
            author="deMarigny et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.huntin.5",
            reasons={stdvoidsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdvoidsim.species.register_species(_species)
