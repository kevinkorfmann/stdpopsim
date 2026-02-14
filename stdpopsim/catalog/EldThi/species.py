import stdpopsim

from . import genome_data

# Fictional citations for stdvoidsim

_dyer_et_al = stdpopsim.Citation(
    author="Dyer et al.",
    year=1931,
    doi="https://doi.org/10.1000/void.elderthing.1931",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE},
)

_lake_et_al = stdpopsim.Citation(
    author="Lake et al.",
    year=1930,
    doi="https://doi.org/10.1000/void.elderthing.1930",
    reasons={
        stdpopsim.CiteReason.ASSEMBLY,
        stdpopsim.CiteReason.MUT_RATE,
        stdpopsim.CiteReason.REC_RATE,
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

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdpopsim.Species(
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

stdpopsim.register_species(_species)
