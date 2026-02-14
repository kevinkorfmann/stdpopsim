"""
Species definition for Informis generatus (Formless Spawn).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

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

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.1",
            reasons={stdvoidsim.CiteReason.MUT_RATE},
        ),
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.2",
            reasons={stdvoidsim.CiteReason.REC_RATE},
        ),
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.3",
            reasons={stdvoidsim.CiteReason.ASSEMBLY},
        ),
    ],
)

_species = stdvoidsim.Species(
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
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.4",
            reasons={stdvoidsim.CiteReason.GEN_TIME},
        ),
        stdvoidsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.5",
            reasons={stdvoidsim.CiteReason.POP_SIZE},
        ),
    ],
)

stdvoidsim.species.register_species(_species)
