"""
Species definition for Informis generatus (Formless Spawn).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdpopsim

from . import genome_data

# Recombination rates per chromosome.
# Formless Spawn have moderate recombination reflecting protoplasmic fluidity.
# Amorphous element does not recombine.
_recombination_rate = {
    "I": 2e-8,
    "II": 2e-8,
    "III": 2e-8,
    "amorphous_element": 0,
}

# Mutation rates per chromosome.
# Moderate mutation rate for protoplasmic organisms.
_mutation_rate = {
    "I": 3e-8,
    "II": 3e-8,
    "III": 3e-8,
    "amorphous_element": 3e-8,
}

# Ploidy: diploid for the main chromosomes, haploid for amorphous element.
_species_ploidy = 2
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "III": _species_ploidy,
    "amorphous_element": 1,
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
            doi="https://doi.org/10.1666/void.formlessspawn.1",
            reasons={stdpopsim.CiteReason.MUT_RATE},
        ),
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.2",
            reasons={stdpopsim.CiteReason.REC_RATE},
        ),
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.3",
            reasons={stdpopsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdpopsim.Species(
    id="ForSpa",
    ensembl_id="informis_generatus",
    name="Informis generatus",
    common_name="Formless Spawn",
    genome=_genome,
    generation_time=10,
    population_size=25000,
    ploidy=_species_ploidy,
    separate_sexes=False,
    citations=[
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.4",
            reasons={stdpopsim.CiteReason.GEN_TIME},
        ),
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.5",
            reasons={stdpopsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdpopsim.species.register_species(_species)
