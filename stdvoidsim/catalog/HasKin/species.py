import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim

_chambers_et_al = stdvoidsim.Citation(
    author="Chambers et al.",
    year=1895,
    doi="https://doi.org/10.1000/void.hastur.1895",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_chambers_genome = stdvoidsim.Citation(
    author="Chambers et al.",
    year=1895,
    doi="https://doi.org/10.1000/void.hastur.assembly.1895",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_chambers_genome]
_species_citations = [_chambers_et_al, _chambers_genome]

# Chromosome-level mutation rate (~5e-8 per base per generation)
# Moderate - memetic drift causes mutations
_mutation_rate = {
    "I": 5.0e-8,
    "II": 5.0e-8,
    "III": 5.0e-8,
    "IV": 5.0e-8,
    "V": 5.0e-8,
    "VI": 5.0e-8,
    "VII": 5.0e-8,
    "yellow_sign_element": 5.0e-8,
}

# Chromosome-level recombination rate (~3e-8 per base per generation)
_recombination_rate = {
    "I": 3.0e-8,
    "II": 3.0e-8,
    "III": 3.0e-8,
    "IV": 3.0e-8,
    "V": 3.0e-8,
    "VI": 3.0e-8,
    "VII": 3.0e-8,
    "yellow_sign_element": 3.0e-8,
}

# Ploidy per chromosome (diploid)
_ploidy = {
    "I": 2,
    "II": 2,
    "III": 2,
    "IV": 2,
    "V": 2,
    "VI": 2,
    "VII": 2,
    "yellow_sign_element": 2,
}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdvoidsim.Species(
    id="HasKin",
    ensembl_id="hastur_carcosensis",
    name="Hastur carcosensis",
    common_name="King in Yellow",
    separate_sexes=False,
    genome=_genome,
    generation_time=50,
    population_size=2000,
    ploidy=2,
    citations=_species_citations,
)

stdvoidsim.register_species(_species)
