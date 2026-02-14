import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim

_dyer_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_lake_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_lake_et_al]
_species_citations = [_dyer_et_al, _lake_et_al]

# Mutation rate: ~1e-9 per base per generation (extremely slow - ancient beings)
_overall_mutation_rate = 1e-9

# Recombination rate: ~5e-10 per base per generation
_overall_recombination_rate = 5e-10

_chromosome_names = list(genome_data.data["chromosomes"].keys())

_mutation_rate = {name: _overall_mutation_rate for name in _chromosome_names}

_recombination_rate = {name: _overall_recombination_rate for name in _chromosome_names}

# Ploidy of 2 for all chromosomes
_ploidy = {name: 2 for name in _chromosome_names}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdvoidsim.Species(
    id="EldThi",
    ensembl_id="elderium_antarcticae",
    name="Elderium antarcticae",
    common_name="Elder Thing",
    separate_sexes=False,
    genome=_genome,
    generation_time=1000,
    population_size=10000,
    ploidy=2,
    citations=_species_citations,
)

stdvoidsim.register_species(_species)
