import stdpopsim
from . import genome_data

_citation = stdpopsim.Citation(author="Carter et al.", year=1926,
    doi="https://doi.org/10.1666/void.nightgaunt.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE})
_assembly_citation = stdpopsim.Citation(author="Carter et al.", year=1926,
    doi="https://doi.org/10.1666/void.nightgaunt.2",
    reasons={stdpopsim.CiteReason.ASSEMBLY})
_mutation_citation = stdpopsim.Citation(author="Carter et al.", year=1926,
    doi="https://doi.org/10.1666/void.nightgaunt.3",
    reasons={stdpopsim.CiteReason.MUT_RATE, stdpopsim.CiteReason.REC_RATE})

_recombination_rate = {c: 1.8e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["faceless_element"] = 0
_mutation_rate = {c: 2e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["faceless_element"] = 5e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["faceless_element"] = 1

_genome = stdpopsim.Genome.from_data(genome_data.data,
    recombination_rate=_recombination_rate, mutation_rate=_mutation_rate,
    ploidy=_ploidy, citations=[_mutation_citation, _assembly_citation])

_species = stdpopsim.Species(id="NigMan", ensembl_id="nightgauntus_mantaformis",
    name="Nightgauntus mantaformis", common_name="Nightgaunt",
    separate_sexes=False, genome=_genome, generation_time=5,
    population_size=75000, ploidy=_species_ploidy, citations=[_citation])
stdpopsim.register_species(_species)
