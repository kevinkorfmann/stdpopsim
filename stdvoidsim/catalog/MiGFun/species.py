import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim

_akeley_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_akeley_genome = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_akeley_genome]
_species_citations = [_akeley_et_al, _akeley_genome]

# Chromosome-level mutation rate (~2e-8 per base per generation)
_mutation_rate = {
    "I": 2.0e-8,
    "II": 2.0e-8,
    "III": 2.0e-8,
    "IV": 2.0e-8,
    "V": 2.0e-8,
    "spore_plasmid": 2.0e-8,
}

# Chromosome-level recombination rate (~1e-8 per base per generation)
_recombination_rate = {
    "I": 1.0e-8,
    "II": 1.0e-8,
    "III": 1.0e-8,
    "IV": 1.0e-8,
    "V": 1.0e-8,
    "spore_plasmid": 1.0e-8,
}

# Ploidy per chromosome (diploid)
_ploidy = {
    "I": 2,
    "II": 2,
    "III": 2,
    "IV": 2,
    "V": 2,
    "spore_plasmid": 2,
}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdvoidsim.Species(
    id="MiGFun",
    ensembl_id="migo_fungoides",
    name="Migo fungoides",
    common_name="Fungi from Yuggoth",
    separate_sexes=False,
    genome=_genome,
    generation_time=5,
    population_size=500000,
    ploidy=2,
    citations=_species_citations,
)

stdvoidsim.register_species(_species)
