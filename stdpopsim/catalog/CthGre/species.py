"""
Species definition for Cthulhu greatoldone (Great Cthulhu).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdpopsim

from . import genome_data

# Recombination rates per chromosome.
# Cthulhu's alien genome has extremely low recombination,
# reflecting eons of stable eldritch genetics.
# Psychic plasmid does not recombine.
_recombination_rate = {
    "I": 1e-9,
    "II": 1e-9,
    "III": 1e-9,
    "IV": 1e-9,
    "V": 1e-9,
    "VI": 1e-9,
    "psychic_plasmid": 0,
}

# Mutation rates per chromosome.
# Extremely stable alien genome with very low mutation rate.
_mutation_rate = {
    "I": 1e-10,
    "II": 1e-10,
    "III": 1e-10,
    "IV": 1e-10,
    "V": 1e-10,
    "VI": 1e-10,
    "psychic_plasmid": 1e-10,
}

# Ploidy: tetraploid for the main chromosomes, haploid for psychic plasmid.
_species_ploidy = 4
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "III": _species_ploidy,
    "IV": _species_ploidy,
    "V": _species_ploidy,
    "VI": _species_ploidy,
    "psychic_plasmid": 1,
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdpopsim.Citation(
            author="Marsh et al.",
            year=1928,
            doi="https://doi.org/10.1666/void.cthulhu.1",
            reasons={stdpopsim.CiteReason.MUT_RATE},
        ),
        stdpopsim.Citation(
            author="Whateley et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.cthulhu.2",
            reasons={stdpopsim.CiteReason.REC_RATE},
        ),
        stdpopsim.Citation(
            author="Armitage et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.cthulhu.3",
            reasons={stdpopsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdpopsim.Species(
    id="CthGre",
    ensembl_id="cthulhu_greatoldone",
    name="Cthulhu greatoldone",
    common_name="Great Cthulhu",
    genome=_genome,
    generation_time=10000,
    population_size=500,
    ploidy=_species_ploidy,
    separate_sexes=False,
    citations=[
        stdpopsim.Citation(
            author="Marsh et al.",
            year=1928,
            doi="https://doi.org/10.1666/void.cthulhu.4",
            reasons={stdpopsim.CiteReason.GEN_TIME},
        ),
        stdpopsim.Citation(
            author="Whateley et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.cthulhu.5",
            reasons={stdpopsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdpopsim.species.register_species(_species)
