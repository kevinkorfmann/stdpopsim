"""
Species definition for Obscurus silvanus (Dark Young).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdpopsim

from . import genome_data

# Recombination rates per chromosome.
# Dark Young have elevated recombination reflecting their
# rapid tentacled growth and triploid genomic architecture.
# Root organelle does not recombine.
_recombination_rate = {
    "I": 1.5e-8,
    "II": 1.5e-8,
    "III": 1.5e-8,
    "IV": 1.5e-8,
    "V": 1.5e-8,
    "VI": 1.5e-8,
    "root_organelle": 0,
}

# Mutation rates per chromosome.
# Elevated mutation rate for spawn of Shub-Niggurath.
_mutation_rate = {
    "I": 2e-8,
    "II": 2e-8,
    "III": 2e-8,
    "IV": 2e-8,
    "V": 2e-8,
    "VI": 2e-8,
    "root_organelle": 2e-8,
}

# Ploidy: triploid for main chromosomes, haploid for root organelle.
_species_ploidy = 3
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "III": _species_ploidy,
    "IV": _species_ploidy,
    "V": _species_ploidy,
    "VI": _species_ploidy,
    "root_organelle": 1,
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdpopsim.Citation(
            author="Bloch et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.daryou.1",
            reasons={stdpopsim.CiteReason.MUT_RATE},
        ),
        stdpopsim.Citation(
            author="Bloch et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.daryou.2",
            reasons={stdpopsim.CiteReason.REC_RATE},
        ),
        stdpopsim.Citation(
            author="Bloch et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.daryou.3",
            reasons={stdpopsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdpopsim.Species(
    id="DarYou",
    ensembl_id="obscurus_silvanus",
    name="Obscurus silvanus",
    common_name="Dark Young",
    genome=_genome,
    generation_time=50,
    population_size=35000,
    ploidy=_species_ploidy,
    separate_sexes=False,
    citations=[
        stdpopsim.Citation(
            author="Bloch et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.daryou.4",
            reasons={stdpopsim.CiteReason.GEN_TIME},
        ),
        stdpopsim.Citation(
            author="Bloch et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.daryou.5",
            reasons={stdpopsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdpopsim.species.register_species(_species)
