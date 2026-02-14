import stdpopsim
from . import genome_data

_citation = stdpopsim.Citation(author="Carter et al.", year=1926,
    doi="https://doi.org/10.1666/void.moonbeast.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE})
_assembly_citation = stdpopsim.Citation(author="Carter et al.", year=1926,
    doi="https://doi.org/10.1666/void.moonbeast.2", reasons={stdpopsim.CiteReason.ASSEMBLY})
_mutation_citation = stdpopsim.Citation(author="Carter et al.", year=1926,
    doi="https://doi.org/10.1666/void.moonbeast.3",
    reasons={stdpopsim.CiteReason.MUT_RATE, stdpopsim.CiteReason.REC_RATE})

_recombination_rate = {c: 1.5e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["lunar_element"] = 0
_mutation_rate = {c: 1.2e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["lunar_element"] = 6e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["lunar_element"] = 1

_genome = stdpopsim.Genome.from_data(genome_data.data,
    recombination_rate=_recombination_rate, mutation_rate=_mutation_rate,
    ploidy=_ploidy, citations=[_mutation_citation, _assembly_citation])

_species = stdpopsim.Species(id="MooFun", ensembl_id="lunaris_bestialis",
    name="Lunaris bestialis", common_name="Moon-Beast",
    separate_sexes=False, genome=_genome, generation_time=8,
    population_size=45000, ploidy=_species_ploidy, citations=[_citation])
stdpopsim.register_species(_species)
