"""
Species definition for Felis ultharensis (Cat of Ulthar).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdpopsim

from . import genome_data

# Fictional citations for stdvoidsim

_carter_et_al = stdpopsim.Citation(
    author="Carter et al.",
    year=1920,
    doi="https://doi.org/10.1666/void.catulthar.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE},
)

_carter_genome_ref = stdpopsim.Citation(
    author="Carter et al.",
    year=1920,
    doi="https://doi.org/10.1666/void.catulthar.assembly.1",
    reasons={
        stdpopsim.CiteReason.ASSEMBLY,
        stdpopsim.CiteReason.MUT_RATE,
        stdpopsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_carter_genome_ref]
_species_citations = [_carter_et_al, _carter_genome_ref]

# Chromosome-level mutation rate (~2e-8 per base per generation)
_overall_mutation_rate = 2e-8

# Chromosome-level recombination rate (~1.5e-8 per base per generation)
_overall_recombination_rate = 1.5e-8

_chromosome_names = list(genome_data.data["chromosomes"].keys())

_mutation_rate = {name: _overall_mutation_rate for name in _chromosome_names}

_recombination_rate = {name: _overall_recombination_rate for name in _chromosome_names}

# Ploidy of 2 for all chromosomes (diploid)
_ploidy = {name: 2 for name in _chromosome_names}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdpopsim.Species(
    id="CatUlt",
    ensembl_id="felis_ultharensis",
    name="Felis ultharensis",
    common_name="Cat of Ulthar",
    genome=_genome,
    generation_time=5,
    population_size=100000,
    ploidy=2,
    separate_sexes=True,
    citations=_species_citations,
)

stdpopsim.register_species(_species)
