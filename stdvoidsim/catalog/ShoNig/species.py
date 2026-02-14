import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim

_dyer_et_al = stdvoidsim.Citation(
    author="Dyer et al.",
    year=1931,
    doi="https://doi.org/10.1000/void.shoggoth.1931",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_danforth_et_al = stdvoidsim.Citation(
    author="Danforth et al.",
    year=1931,
    doi="https://doi.org/10.1000/void.shoggoth.assembly.1931",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_danforth_et_al]
_species_citations = [_dyer_et_al, _danforth_et_al]

# Chromosome-level mutation rate (~5e-9 per base per generation)
_mutation_rate = {
    "I": 5.0e-9,
    "II": 5.0e-9,
    "III": 5.0e-9,
    "IV": 5.0e-9,
    "V": 5.0e-9,
    "VI": 5.0e-9,
    "VII": 5.0e-9,
    "VIII": 5.0e-9,
    "IX": 5.0e-9,
    "X": 5.0e-9,
    "XI": 5.0e-9,
    "XII": 5.0e-9,
}

# Chromosome-level recombination rate (~2e-8 per base per generation)
_recombination_rate = {
    "I": 2.0e-8,
    "II": 2.0e-8,
    "III": 2.0e-8,
    "IV": 2.0e-8,
    "V": 2.0e-8,
    "VI": 2.0e-8,
    "VII": 2.0e-8,
    "VIII": 2.0e-8,
    "IX": 2.0e-8,
    "X": 2.0e-8,
    "XI": 2.0e-8,
    "XII": 2.0e-8,
}

# Ploidy per chromosome (hexaploid - engineered by Elder Things for redundancy)
_ploidy = {
    "I": 6,
    "II": 6,
    "III": 6,
    "IV": 6,
    "V": 6,
    "VI": 6,
    "VII": 6,
    "VIII": 6,
    "IX": 6,
    "X": 6,
    "XI": 6,
    "XII": 6,
}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdvoidsim.Species(
    id="ShoNig",
    ensembl_id="shoggoth_nigrumplasma",
    name="Shoggoth nigrumplasma",
    common_name="Shoggoth",
    separate_sexes=False,
    genome=_genome,
    generation_time=0.5,
    population_size=100000,
    ploidy=6,
    citations=_species_citations,
)

stdvoidsim.register_species(_species)
