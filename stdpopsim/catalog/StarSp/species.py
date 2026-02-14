import stdpopsim
from . import genome_data

_citation = stdpopsim.Citation(author="Johansen et al.", year=1926,
    doi="https://doi.org/10.1666/void.starspawn.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE})
_assembly_citation = stdpopsim.Citation(author="Johansen et al.", year=1926,
    doi="https://doi.org/10.1666/void.starspawn.2", reasons={stdpopsim.CiteReason.ASSEMBLY})
_mutation_citation = stdpopsim.Citation(author="Johansen et al.", year=1926,
    doi="https://doi.org/10.1666/void.starspawn.3",
    reasons={stdpopsim.CiteReason.MUT_RATE, stdpopsim.CiteReason.REC_RATE})

_recombination_rate = {c: 5e-9 for c in genome_data.data["chromosomes"]}
_recombination_rate["spawn_organelle"] = 0
_mutation_rate = {c: 2e-9 for c in genome_data.data["chromosomes"]}
_mutation_rate["spawn_organelle"] = 1e-8
_species_ploidy = 4
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["spawn_organelle"] = 1

_genome = stdpopsim.Genome.from_data(genome_data.data,
    recombination_rate=_recombination_rate, mutation_rate=_mutation_rate,
    ploidy=_ploidy, citations=[_mutation_citation, _assembly_citation])

_species = stdpopsim.Species(id="StarSp", ensembl_id="starspawn_cthulhidae",
    name="Starspawn cthulhidae", common_name="Star-Spawn of Cthulhu",
    separate_sexes=False, genome=_genome, generation_time=5000,
    population_size=10000, ploidy=_species_ploidy, citations=[_citation])
stdpopsim.register_species(_species)
