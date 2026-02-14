"""
Species definition for Chaugnarus faugnis (Chaugnar Faugn).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim

_long_et_al = stdvoidsim.Citation(
    author="Long et al.",
    year=1932,
    doi="https://doi.org/10.1666/void.chaugnar.1",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_long_genome_ref = stdvoidsim.Citation(
    author="Long et al.",
    year=1932,
    doi="https://doi.org/10.1666/void.chaugnar.assembly.1",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_long_genome_ref]
_species_citations = [_long_et_al, _long_genome_ref]

# Chromosome-level mutation rate (~2e-10 per base per generation)
# Extremely slow due to vast generation time and eldritch stability
_overall_mutation_rate = 2e-10

# Chromosome-level recombination rate (~1e-10 per base per generation)
_overall_recombination_rate = 1e-10

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
    id="ChaFau",
    ensembl_id="chaugnarus_faugnis",
    name="Chaugnarus faugnis",
    common_name="Chaugnar Faugn",
    genome=_genome,
    generation_time=10000,
    population_size=200,
    ploidy=2,
    separate_sexes=False,
    citations=_species_citations,
)

stdvoidsim.register_species(_species)
