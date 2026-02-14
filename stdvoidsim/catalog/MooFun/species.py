import stdvoidsim
from . import genome_data

_citation = stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE})
_assembly_citation = stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon", reasons={stdvoidsim.CiteReason.ASSEMBLY})
_mutation_citation = stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.MUT_RATE, stdvoidsim.CiteReason.REC_RATE})

_recombination_rate = {c: 1.5e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["lunar_element"] = 0
_mutation_rate = {c: 1.2e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["lunar_element"] = 6e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["lunar_element"] = 1

_genome = stdvoidsim.Genome.from_data(genome_data.data,
    recombination_rate=_recombination_rate, mutation_rate=_mutation_rate,
    ploidy=_ploidy, citations=[_mutation_citation, _assembly_citation])

_species = stdvoidsim.Species(id="MooFun", ensembl_id="lunaris_bestialis",
    name="Lunaris bestialis", common_name="Moon-Beast",
    separate_sexes=False, genome=_genome, generation_time=8,
    population_size=45000, ploidy=_species_ploidy, citations=[_citation])
stdvoidsim.register_species(_species)
