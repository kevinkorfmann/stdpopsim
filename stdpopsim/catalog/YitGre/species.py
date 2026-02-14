"""
Species definition for Yithianus temporalis (Great Race of Yith).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdpopsim

from . import genome_data

# Recombination rates per chromosome.
# The Great Race of Yith has very low recombination reflecting
# their extremely stable time-spanning genomic architecture.
# Temporal organelle does not recombine.
_recombination_rate = {
    "I": 2e-9,
    "II": 2e-9,
    "III": 2e-9,
    "IV": 2e-9,
    "V": 2e-9,
    "VI": 2e-9,
    "VII": 2e-9,
    "temporal_organelle": 0,
}

# Mutation rates per chromosome.
# Low mutation rate for long-lived cone-shaped entities.
_mutation_rate = {
    "I": 3e-9,
    "II": 3e-9,
    "III": 3e-9,
    "IV": 3e-9,
    "V": 3e-9,
    "VI": 3e-9,
    "VII": 3e-9,
    "temporal_organelle": 3e-9,
}

# Ploidy: diploid for main chromosomes, haploid for temporal organelle.
_species_ploidy = 2
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "III": _species_ploidy,
    "IV": _species_ploidy,
    "V": _species_ploidy,
    "VI": _species_ploidy,
    "VII": _species_ploidy,
    "temporal_organelle": 1,
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdpopsim.Citation(
            author="Peaslee et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.yitgre.1",
            reasons={stdpopsim.CiteReason.MUT_RATE},
        ),
        stdpopsim.Citation(
            author="Peaslee et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.yitgre.2",
            reasons={stdpopsim.CiteReason.REC_RATE},
        ),
        stdpopsim.Citation(
            author="Peaslee et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.yitgre.3",
            reasons={stdpopsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdpopsim.Species(
    id="YitGre",
    ensembl_id="yithianus_temporalis",
    name="Yithianus temporalis",
    common_name="Great Race of Yith",
    genome=_genome,
    generation_time=500,
    population_size=50000,
    ploidy=_species_ploidy,
    separate_sexes=False,
    citations=[
        stdpopsim.Citation(
            author="Peaslee et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.yitgre.4",
            reasons={stdpopsim.CiteReason.GEN_TIME},
        ),
        stdpopsim.Citation(
            author="Peaslee et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.yitgre.5",
            reasons={stdpopsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdpopsim.species.register_species(_species)
