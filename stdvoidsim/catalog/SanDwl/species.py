"""
Species definition for Arenicola abyssalis (Sand Dweller).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim

_alhazred_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_alhazred_genome_ref = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_alhazred_genome_ref]
_species_citations = [_alhazred_et_al, _alhazred_genome_ref]

# Chromosome-level mutation rate (~1.2e-8 per base per generation)
_overall_mutation_rate = 1.2e-8

# Chromosome-level recombination rate (~9e-9 per base per generation)
_overall_recombination_rate = 9e-9

_chromosome_names = list(genome_data.data["chromosomes"].keys())

_mutation_rate = {name: _overall_mutation_rate for name in _chromosome_names}

_recombination_rate = {name: _overall_recombination_rate for name in _chromosome_names}

# Ploidy of 2 for all chromosomes (diploid)
_ploidy = {name: 2 for name in _chromosome_names}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdvoidsim.Species(
    id="SanDwl",
    ensembl_id="arenicola_abyssalis",
    name="Arenicola abyssalis",
    common_name="Sand Dweller",
    genome=_genome,
    generation_time=15,
    population_size=40000,
    ploidy=2,
    separate_sexes=False,
    citations=_species_citations,
)

stdvoidsim.register_species(_species)
