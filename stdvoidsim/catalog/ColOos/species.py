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

_recombination_rate = {c: 5e-7 for c in genome_data.data["chromosomes"]}
_recombination_rate["spectral_element"] = 0
_mutation_rate = {c: 1e-6 for c in genome_data.data["chromosomes"]}
_mutation_rate["spectral_element"] = 1e-5
_species_ploidy = 1
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdvoidsim.Species(
    id="ColOos",
    ensembl_id="chromatis_extraspatiala",
    name="Chromatis extraspatiala",
    common_name="Colour Out of Space",
    separate_sexes=False,
    genome=_genome,
    generation_time=0.1,
    population_size=10000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdvoidsim.register_species(_species)
