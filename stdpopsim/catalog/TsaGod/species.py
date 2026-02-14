"""
Species definition for Tsathoggua somnolentis (Tsathoggua).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdpopsim

from . import genome_data

# Recombination rates per chromosome.
# Tsathoggua's toad-like genome has very low recombination,
# reflecting eons of slothful dormancy in N'kai.
# N'kai plasmid does not recombine.
_recombination_rate = {
    "I": 3e-10,
    "II": 3e-10,
    "III": 3e-10,
    "IV": 3e-10,
    "nkai_plasmid": 0,
}

# Mutation rates per chromosome.
# Extremely stable alien genome with very low mutation rate.
_mutation_rate = {
    "I": 5e-10,
    "II": 5e-10,
    "III": 5e-10,
    "IV": 5e-10,
    "nkai_plasmid": 5e-10,
}

# Ploidy: diploid for the main chromosomes, haploid for nkai plasmid.
_species_ploidy = 2
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "III": _species_ploidy,
    "IV": _species_ploidy,
    "nkai_plasmid": 1,
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.1",
            reasons={stdpopsim.CiteReason.MUT_RATE},
        ),
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.2",
            reasons={stdpopsim.CiteReason.REC_RATE},
        ),
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.3",
            reasons={stdpopsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdpopsim.Species(
    id="TsaGod",
    ensembl_id="tsathoggua_somnolentis",
    name="Tsathoggua somnolentis",
    common_name="Tsathoggua",
    genome=_genome,
    generation_time=50000,
    population_size=100,
    ploidy=_species_ploidy,
    separate_sexes=False,
    citations=[
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.4",
            reasons={stdpopsim.CiteReason.GEN_TIME},
        ),
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.5",
            reasons={stdpopsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdpopsim.species.register_species(_species)
