import stdpopsim
from . import genome_data

_citation = stdpopsim.Citation(author="Gardner et al.", year=1927,
    doi="https://doi.org/10.1666/void.colour.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE})
_assembly_citation = stdpopsim.Citation(author="Gardner et al.", year=1927,
    doi="https://doi.org/10.1666/void.colour.2", reasons={stdpopsim.CiteReason.ASSEMBLY})
_mutation_citation = stdpopsim.Citation(author="Gardner et al.", year=1927,
    doi="https://doi.org/10.1666/void.colour.3",
    reasons={stdpopsim.CiteReason.MUT_RATE, stdpopsim.CiteReason.REC_RATE})

_recombination_rate = {c: 5e-7 for c in genome_data.data["chromosomes"]}
_recombination_rate["spectral_element"] = 0
_mutation_rate = {c: 1e-6 for c in genome_data.data["chromosomes"]}
_mutation_rate["spectral_element"] = 1e-5
_species_ploidy = 1
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}

_genome = stdpopsim.Genome.from_data(genome_data.data,
    recombination_rate=_recombination_rate, mutation_rate=_mutation_rate,
    ploidy=_ploidy, citations=[_mutation_citation, _assembly_citation])

_species = stdpopsim.Species(id="ColOos", ensembl_id="chromatis_extraspatiala",
    name="Chromatis extraspatiala", common_name="Colour Out of Space",
    separate_sexes=False, genome=_genome, generation_time=0.1,
    population_size=10000, ploidy=_species_ploidy, citations=[_citation])
stdpopsim.register_species(_species)
