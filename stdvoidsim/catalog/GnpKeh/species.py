"""
Species definition for Gnophkehus arcticus (Gnoph-Keh).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

from . import genome_data

# Recombination rates per chromosome.
# Gnoph-Keh have low recombination reflecting ancient arctic genome stability.
# Frost mitogenome does not recombine.
_recombination_rate = {
    "I": 3e-9,
    "II": 3e-9,
    "III": 3e-9,
    "IV": 3e-9,
    "V": 3e-9,
    "VI": 3e-9,
    "frost_mitogenome": 0,
}

# Mutation rates per chromosome.
# Low mutation rate for long-lived arctic organisms.
_mutation_rate = {
    "I": 4e-9,
    "II": 4e-9,
    "III": 4e-9,
    "IV": 4e-9,
    "V": 4e-9,
    "VI": 4e-9,
    "frost_mitogenome": 4e-9,
}

# Ploidy: diploid for the main chromosomes, haploid for frost mitogenome.
_species_ploidy = 2
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "III": _species_ploidy,
    "IV": _species_ploidy,
    "V": _species_ploidy,
    "VI": _species_ploidy,
    "frost_mitogenome": 1,
}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdvoidsim.Citation(
            author="Howard et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.gnophkeh.1",
            reasons={stdvoidsim.CiteReason.MUT_RATE},
        ),
        stdvoidsim.Citation(
            author="Howard et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.gnophkeh.2",
            reasons={stdvoidsim.CiteReason.REC_RATE},
        ),
        stdvoidsim.Citation(
            author="Howard et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.gnophkeh.3",
            reasons={stdvoidsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdvoidsim.Species(
    id="GnpKeh",
    ensembl_id="gnophkehus_arcticus",
    name="Gnophkehus arcticus",
    common_name="Gnoph-Keh",
    genome=_genome,
    generation_time=40,
    population_size=12000,
    ploidy=_species_ploidy,
    separate_sexes=True,
    citations=[
        stdvoidsim.Citation(
            author="Howard et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.gnophkeh.4",
            reasons={stdvoidsim.CiteReason.GEN_TIME},
        ),
        stdvoidsim.Citation(
            author="Howard et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.gnophkeh.5",
            reasons={stdvoidsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdvoidsim.species.register_species(_species)
