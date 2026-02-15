import stdvoidsim
from . import genome_data

_citation = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.MUT_RATE, stdvoidsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 1.2e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["venom_mitogenome"] = 0
_mutation_rate = {c: 1e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["venom_mitogenome"] = 5e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["venom_mitogenome"] = 1

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdvoidsim.Species(
    id="SerHum",
    ensembl_id="serpentis_valusiensis",
    name="Serpentis valusiensis",
    common_name="Serpent Person",
    separate_sexes=True,
    genome=_genome,
    generation_time=50,
    population_size=40000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdvoidsim.register_species(_species)
