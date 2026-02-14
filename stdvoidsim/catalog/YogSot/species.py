import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim
_whateley_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_genome_citation = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

# Mutation rate: ~1e-12 per base per generation (nearly immutable, exists outside time)
# Recombination rate: ~1e-11 per base per generation

_chromosomes = genome_data.data["chromosomes"]

_mutation_rate = {name: 1e-12 for name in _chromosomes}
_recombination_rate = {name: 1e-11 for name in _chromosomes}
_ploidy = {name: 2 for name in _chromosomes}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_genome_citation],
)

_species = stdvoidsim.Species(
    id="YogSot",
    name="Yogsothoth dimensionalis",
    common_name="The Key and the Gate",
    ensembl_id="",
    separate_sexes=False,
    genome=_genome,
    generation_time=100000,
    population_size=10,
    ploidy=2,
    citations=[_whateley_et_al],
)

stdvoidsim.species.register_species(_species)
