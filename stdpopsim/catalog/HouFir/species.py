import stdpopsim
from . import genome_data

_citation = stdpopsim.Citation(author="Long et al.", year=1929,
    doi="https://doi.org/10.1666/void.tindalos.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE})
_assembly_citation = stdpopsim.Citation(author="Long et al.", year=1929,
    doi="https://doi.org/10.1666/void.tindalos.2", reasons={stdpopsim.CiteReason.ASSEMBLY})
_mutation_citation = stdpopsim.Citation(author="Long et al.", year=1929,
    doi="https://doi.org/10.1666/void.tindalos.3",
    reasons={stdpopsim.CiteReason.MUT_RATE, stdpopsim.CiteReason.REC_RATE})

_recombination_rate = {c: 5e-9 for c in genome_data.data["chromosomes"]}
_recombination_rate["angular_genome"] = 0
_mutation_rate = {c: 3e-9 for c in genome_data.data["chromosomes"]}
_mutation_rate["angular_genome"] = 1e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["angular_genome"] = 1

_genome = stdpopsim.Genome.from_data(genome_data.data,
    recombination_rate=_recombination_rate, mutation_rate=_mutation_rate,
    ploidy=_ploidy, citations=[_mutation_citation, _assembly_citation])

_species = stdpopsim.Species(id="HouFir", ensembl_id="houndus_tindalosi",
    name="Houndus tindalosi", common_name="Hound of Tindalos",
    separate_sexes=False, genome=_genome, generation_time=500,
    population_size=5000, ploidy=_species_ploidy, citations=[_citation])
stdpopsim.register_species(_species)
