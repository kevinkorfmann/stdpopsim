import stdvoidsim

from . import genome_data

# Fictional citations for this Lovecraftian species.
_NyarlathotepGenomeRef = stdvoidsim.Citation(
    author="The Nyarlathotep Research Consortium",
    year=1920,
    doi="https://doi.org/10.1666/void.nyarlathotep.genome",
    reasons={stdvoidsim.CiteReason.ASSEMBLY},
)

_NyarlathotepMutRateRef = stdvoidsim.Citation(
    author="The Nyarlathotep Research Consortium",
    year=1921,
    doi="https://doi.org/10.1666/void.nyarlathotep.mutrate",
    reasons={stdvoidsim.CiteReason.MUT_RATE},
)

_NyarlathotepRecRateRef = stdvoidsim.Citation(
    author="The Nyarlathotep Research Consortium",
    year=1921,
    doi="https://doi.org/10.1666/void.nyarlathotep.recrate",
    reasons={stdvoidsim.CiteReason.REC_RATE},
)

_NyarlathotepPopSizeRef = stdvoidsim.Citation(
    author="The Nyarlathotep Research Consortium",
    year=1926,
    doi="https://doi.org/10.1666/void.nyarlathotep.popsize",
    reasons={stdvoidsim.CiteReason.POP_SIZE},
)

_NyarlathotepGenTimeRef = stdvoidsim.Citation(
    author="The Nyarlathotep Research Consortium",
    year=1926,
    doi="https://doi.org/10.1666/void.nyarlathotep.gentime",
    reasons={stdvoidsim.CiteReason.GEN_TIME},
)

# Mutation rate: ~1e-7 per base per generation (extremely high - shapeshifting)
_overall_mutation_rate = 1e-7

# Recombination rate: ~1e-6 per base per generation (chaotic recombination)
_overall_recombination_rate = 1e-6

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
    citations=[
        _NyarlathotepGenomeRef,
        _NyarlathotepMutRateRef,
        _NyarlathotepRecRateRef,
    ],
)

_species = stdvoidsim.Species(
    id="NyaAza",
    ensembl_id="nyarlathotep_azathothspawn",
    name="Nyarlathotep azathothspawn",
    common_name="Crawling Chaos",
    separate_sexes=False,
    genome=_genome,
    generation_time=1,
    population_size=1000,
    ploidy=2,
    citations=[
        _NyarlathotepPopSizeRef,
        _NyarlathotepGenTimeRef,
    ],
)

stdvoidsim.species.register_species(_species)
