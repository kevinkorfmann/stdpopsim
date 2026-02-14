"""
Species definition for Tsathoggua choriensis (Tcho-Tcho).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

from . import genome_data

# Recombination rates per chromosome.
# Tcho-Tcho have elevated recombination reflecting their
# rapid generational turnover and tainted genomic architecture.
# Tainted mitogenome does not recombine.
_recombination_rate = {
    "1": 1.2e-8,
    "2": 1.2e-8,
    "3": 1.2e-8,
    "4": 1.2e-8,
    "5": 1.2e-8,
    "6": 1.2e-8,
    "7": 1.2e-8,
    "8": 1.2e-8,
    "tainted_mitogenome": 0,
}

# Mutation rates per chromosome.
# Elevated mutation rate for degenerate human-like tribe.
_mutation_rate = {
    "1": 1.5e-8,
    "2": 1.5e-8,
    "3": 1.5e-8,
    "4": 1.5e-8,
    "5": 1.5e-8,
    "6": 1.5e-8,
    "7": 1.5e-8,
    "8": 1.5e-8,
    "tainted_mitogenome": 1.5e-8,
}

# Ploidy: diploid for main chromosomes, haploid for tainted mitogenome.
_species_ploidy = 2
_ploidy = {
    "1": _species_ploidy,
    "2": _species_ploidy,
    "3": _species_ploidy,
    "4": _species_ploidy,
    "5": _species_ploidy,
    "6": _species_ploidy,
    "7": _species_ploidy,
    "8": _species_ploidy,
    "tainted_mitogenome": 1,
}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdvoidsim.Citation(
            author="Derleth et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.tsacho.1",
            reasons={stdvoidsim.CiteReason.MUT_RATE},
        ),
        stdvoidsim.Citation(
            author="Derleth et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.tsacho.2",
            reasons={stdvoidsim.CiteReason.REC_RATE},
        ),
        stdvoidsim.Citation(
            author="Derleth et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.tsacho.3",
            reasons={stdvoidsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdvoidsim.Species(
    id="TsaCho",
    ensembl_id="tsathoggua_choriensis",
    name="Tsathoggua choriensis",
    common_name="Tcho-Tcho",
    genome=_genome,
    generation_time=25,
    population_size=70000,
    ploidy=_species_ploidy,
    separate_sexes=True,
    citations=[
        stdvoidsim.Citation(
            author="Derleth et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.tsacho.4",
            reasons={stdvoidsim.CiteReason.GEN_TIME},
        ),
        stdvoidsim.Citation(
            author="Derleth et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.tsacho.5",
            reasons={stdvoidsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdvoidsim.species.register_species(_species)
