import stdpopsim
from . import genome_data

_citation = stdpopsim.Citation(author="Carter et al.", year=1926,
    doi="https://doi.org/10.1666/void.zoog.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE})
_assembly_citation = stdpopsim.Citation(author="Carter et al.", year=1926,
    doi="https://doi.org/10.1666/void.zoog.2", reasons={stdpopsim.CiteReason.ASSEMBLY})
_mutation_citation = stdpopsim.Citation(author="Carter et al.", year=1926,
    doi="https://doi.org/10.1666/void.zoog.3",
    reasons={stdpopsim.CiteReason.MUT_RATE, stdpopsim.CiteReason.REC_RATE})

_recombination_rate = {c: 3e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["forest_mitogenome"] = 0
_mutation_rate = {c: 2.5e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["forest_mitogenome"] = 8e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["forest_mitogenome"] = 1

_genome = stdpopsim.Genome.from_data(genome_data.data,
    recombination_rate=_recombination_rate, mutation_rate=_mutation_rate,
    ploidy=_ploidy, citations=[_mutation_citation, _assembly_citation])

_species = stdpopsim.Species(id="ZooGul", ensembl_id="zoogus_sylvaticus",
    name="Zoogus sylvaticus", common_name="Zoog",
    separate_sexes=True, genome=_genome, generation_time=2,
    population_size=500000, ploidy=_species_ploidy, citations=[_citation])
stdpopsim.register_species(_species)
