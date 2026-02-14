"""
Species definition for Dagonus maximus (Father Dagon).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import stdpopsim

from . import genome_data

# Fictional citations for stdvoidsim

_olmstead_et_al = stdpopsim.Citation(
    author="Olmstead et al.",
    year=1931,
    doi="https://doi.org/10.1666/void.dagon.1",
    reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE},
)

_olmstead_genome_ref = stdpopsim.Citation(
    author="Olmstead et al.",
    year=1931,
    doi="https://doi.org/10.1666/void.dagon.assembly.1",
    reasons={
        stdpopsim.CiteReason.ASSEMBLY,
        stdpopsim.CiteReason.MUT_RATE,
        stdpopsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_olmstead_genome_ref]
_species_citations = [_olmstead_et_al, _olmstead_genome_ref]

# Chromosome-level mutation rate (~5e-11 per base per generation)
# Near-immortal genome with extremely low mutation rate
_overall_mutation_rate = 5e-11

# Chromosome-level recombination rate (~3e-11 per base per generation)
_overall_recombination_rate = 3e-11

_chromosome_names = list(genome_data.data["chromosomes"].keys())

_mutation_rate = {name: _overall_mutation_rate for name in _chromosome_names}

_recombination_rate = {name: _overall_recombination_rate for name in _chromosome_names}

# Ploidy: tetraploid for the main chromosomes, haploid for abyssal plasmid.
_species_ploidy = 4
_ploidy = {name: _species_ploidy for name in _chromosome_names}
_ploidy["abyssal_plasmid"] = 1

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdpopsim.Species(
    id="DagGod",
    ensembl_id="dagonus_maximus",
    name="Dagonus maximus",
    common_name="Father Dagon",
    genome=_genome,
    generation_time=50000,
    population_size=50,
    ploidy=_species_ploidy,
    separate_sexes=False,
    citations=_species_citations,
)

stdpopsim.register_species(_species)
