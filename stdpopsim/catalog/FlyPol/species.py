import stdpopsim
from . import genome_data

_citation = stdpopsim.Citation(author="Peaslee et al.", year=1935,
    doi="https://doi.org/10.1666/void.polyp.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE})
_assembly_citation = stdpopsim.Citation(author="Peaslee et al.", year=1935,
    doi="https://doi.org/10.1666/void.polyp.2", reasons={stdpopsim.CiteReason.ASSEMBLY})
_mutation_citation = stdpopsim.Citation(author="Peaslee et al.", year=1935,
    doi="https://doi.org/10.1666/void.polyp.3",
    reasons={stdpopsim.CiteReason.MUT_RATE, stdpopsim.CiteReason.REC_RATE})

_recombination_rate = {c: 8e-9 for c in genome_data.data["chromosomes"]}
_recombination_rate["wind_organelle"] = 0
_mutation_rate = {c: 6e-9 for c in genome_data.data["chromosomes"]}
_mutation_rate["wind_organelle"] = 3e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["wind_organelle"] = 1

_genome = stdpopsim.Genome.from_data(genome_data.data,
    recombination_rate=_recombination_rate, mutation_rate=_mutation_rate,
    ploidy=_ploidy, citations=[_mutation_citation, _assembly_citation])

_species = stdpopsim.Species(id="FlyPol", ensembl_id="polypus_volantis",
    name="Polypus volantis", common_name="Flying Polyp",
    separate_sexes=False, genome=_genome, generation_time=2000,
    population_size=20000, ploidy=_species_ploidy, citations=[_citation])
stdpopsim.register_species(_species)
