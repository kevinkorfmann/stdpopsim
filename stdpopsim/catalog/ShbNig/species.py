import stdpopsim
from . import genome_data

_citation = stdpopsim.Citation(
    author="Whateley et al.",
    year=1927,
    doi="https://doi.org/10.1666/void.shubnigg.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdpopsim.Citation(
    author="Whateley et al.", year=1927,
    doi="https://doi.org/10.1666/void.shubnigg.2",
    reasons={stdpopsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdpopsim.Citation(
    author="Whateley et al.", year=1927,
    doi="https://doi.org/10.1666/void.shubnigg.3",
    reasons={stdpopsim.CiteReason.MUT_RATE, stdpopsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 2.5e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["fertility_plasmid"] = 0

_mutation_rate = {c: 3e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["fertility_plasmid"] = 1e-7

_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["fertility_plasmid"] = 1

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdpopsim.Species(
    id="ShbNig",
    ensembl_id="shubniggurath_fertilitas",
    name="Shubniggurath fertilitas",
    common_name="Black Goat of the Woods",
    separate_sexes=False,
    genome=_genome,
    generation_time=25,
    population_size=100000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdpopsim.register_species(_species)
