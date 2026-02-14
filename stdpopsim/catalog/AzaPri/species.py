import stdpopsim
from . import genome_data

_citation = stdpopsim.Citation(
    author="The Daemon Sultan Cult",
    year=1922,
    doi="https://doi.org/10.1666/void.azathoth.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE},
)

_assembly_citation = stdpopsim.Citation(
    author="The Daemon Sultan Cult",
    year=1922,
    doi="https://doi.org/10.1666/void.azathoth.2",
    reasons={stdpopsim.CiteReason.ASSEMBLY},
)

_mutation_citation = stdpopsim.Citation(
    author="The Daemon Sultan Cult",
    year=1922,
    doi="https://doi.org/10.1666/void.azathoth.3",
    reasons={stdpopsim.CiteReason.MUT_RATE, stdpopsim.CiteReason.REC_RATE},
)

_recombination_rate = {
    "I": 1e-12,
    "nuclear_chaos_element": 0,
}

_mutation_rate = {
    "I": 1e-11,
    "nuclear_chaos_element": 1e-6,
}

_species_ploidy = 2
_ploidy = {
    "I": _species_ploidy,
    "nuclear_chaos_element": 1,
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        _mutation_citation,
        _assembly_citation,
    ],
)

_species = stdpopsim.Species(
    id="AzaPri",
    ensembl_id="azathoth_primordia",
    name="Azathoth primordia",
    common_name="Blind Idiot God",
    separate_sexes=False,
    genome=_genome,
    generation_time=1000000,
    population_size=1,
    ploidy=_species_ploidy,
    citations=[_citation],
)

stdpopsim.register_species(_species)
