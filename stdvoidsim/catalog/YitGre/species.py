"""
Species definition for Yithianus temporalis (Great Race of Yith).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

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
