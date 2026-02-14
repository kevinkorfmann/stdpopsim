import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim

_pickman_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_pickman_assembly = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_pickman_assembly]
_species_citations = [_pickman_et_al, _pickman_assembly]

# Chromosome-level mutation rate (~1.5e-8 per base per generation)
_mutation_rate = {
    "1": 1.5e-8,
    "2": 1.5e-8,
    "3": 1.5e-8,
    "4": 1.5e-8,
    "5": 1.5e-8,
    "6": 1.5e-8,
    "7": 1.5e-8,
    "8": 1.5e-8,
    "crypt_mitogenome": 1.5e-8,
}

# Chromosome-level recombination rate (~1.2e-8 per base per generation)
_recombination_rate = {
    "1": 1.2e-8,
    "2": 1.2e-8,
    "3": 1.2e-8,
    "4": 1.2e-8,
    "5": 1.2e-8,
    "6": 1.2e-8,
    "7": 1.2e-8,
    "8": 1.2e-8,
    "crypt_mitogenome": 0,
}

# Ploidy per chromosome (diploid, reflecting human origin)
_ploidy = {
    "1": 2,
    "2": 2,
    "3": 2,
    "4": 2,
    "5": 2,
    "6": 2,
    "7": 2,
    "8": 2,
    "crypt_mitogenome": 1,
}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdvoidsim.Species(
    id="GhoFee",
    ensembl_id="ghoulish_necrophagus",
    name="Ghoulish necrophagus",
    common_name="Ghoul",
    separate_sexes=True,
    genome=_genome,
    generation_time=20,
    population_size=30000,
    ploidy=2,
    citations=_species_citations,
)

stdvoidsim.register_species(_species)
