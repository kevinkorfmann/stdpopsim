"""
Species definition for Tsathoggua somnolentis (Tsathoggua).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

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

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.1",
            reasons={stdvoidsim.CiteReason.MUT_RATE},
        ),
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.2",
            reasons={stdvoidsim.CiteReason.REC_RATE},
        ),
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.3",
            reasons={stdvoidsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdvoidsim.Species(
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
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.4",
            reasons={stdvoidsim.CiteReason.GEN_TIME},
        ),
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.5",
            reasons={stdvoidsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdvoidsim.species.register_species(_species)
