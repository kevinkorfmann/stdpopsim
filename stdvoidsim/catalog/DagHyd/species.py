import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim

_marsh_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_marsh_genome_ref = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_marsh_genome_ref]
_species_citations = [_marsh_et_al, _marsh_genome_ref]

# Chromosome-level mutation rate (~3e-8 per base per generation)
_overall_mutation_rate = 3e-8

# Chromosome-level recombination rate (~1.5e-8 per base per generation)
_overall_recombination_rate = 1.5e-8

_chromosome_names = list(genome_data.data["chromosomes"].keys())

_mutation_rate = {name: _overall_mutation_rate for name in _chromosome_names}

_recombination_rate = {name: _overall_recombination_rate for name in _chromosome_names}

# Ploidy of 2 for all chromosomes (diploid, like humans they interbreed with)
_ploidy = {name: 2 for name in _chromosome_names}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdvoidsim.Species(
    id="DagHyd",
    ensembl_id="dagonus_hydridae",
    name="Dagonus hydridae",
    common_name="Deep One",
    separate_sexes=True,
    genome=_genome,
    generation_time=100,
    population_size=50000,
    ploidy=2,
    citations=_species_citations,
)

stdvoidsim.register_species(_species)
