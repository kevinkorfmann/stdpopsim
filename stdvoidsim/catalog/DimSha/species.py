import stdvoidsim
from . import genome_data

_citation = stdvoidsim.Citation(author="Bloch et al.", year=1933,
    doi="https://doi.org/10.1666/void.shambler.1",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE})
_assembly_citation = stdvoidsim.Citation(author="Bloch et al.", year=1933,
    doi="https://doi.org/10.1666/void.shambler.2", reasons={stdvoidsim.CiteReason.ASSEMBLY})
_mutation_citation = stdvoidsim.Citation(author="Bloch et al.", year=1933,
    doi="https://doi.org/10.1666/void.shambler.3",
    reasons={stdvoidsim.CiteReason.MUT_RATE, stdvoidsim.CiteReason.REC_RATE})

_recombination_rate = {c: 1e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["planar_element"] = 0
_mutation_rate = {c: 8e-9 for c in genome_data.data["chromosomes"]}
_mutation_rate["planar_element"] = 5e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["planar_element"] = 1

_genome = stdvoidsim.Genome.from_data(genome_data.data,
    recombination_rate=_recombination_rate, mutation_rate=_mutation_rate,
    ploidy=_ploidy, citations=[_mutation_citation, _assembly_citation])

_species = stdvoidsim.Species(id="DimSha", ensembl_id="dimensius_shambleris",
    name="Dimensius shambleris", common_name="Dimensional Shambler",
    separate_sexes=False, genome=_genome, generation_time=100,
    population_size=3000, ploidy=_species_ploidy, citations=[_citation])
stdvoidsim.register_species(_species)
