import stdvoidsim

from . import genome_data

# Fictional citations for stdvoidsim

_demarigny_et_al = stdvoidsim.Citation(
    author="deMarigny et al.",
    year=1933,
    doi="https://doi.org/10.1000/void.byakhee.1933",
    reasons={stdvoidsim.CiteReason.GEN_TIME, stdvoidsim.CiteReason.POP_SIZE},
)

_demarigny_assembly = stdvoidsim.Citation(
    author="deMarigny et al.",
    year=1933,
    doi="https://doi.org/10.1000/void.byakhee.assembly.1933",
    reasons={
        stdvoidsim.CiteReason.ASSEMBLY,
        stdvoidsim.CiteReason.MUT_RATE,
        stdvoidsim.CiteReason.REC_RATE,
    },
)

_genome_citations = [_demarigny_assembly]
_species_citations = [_demarigny_et_al, _demarigny_assembly]

# Chromosome-level mutation rate (~4e-9 per base per generation, adapted to cosmic radiation)
_mutation_rate = {
    "I": 4.0e-9,
    "II": 4.0e-9,
    "III": 4.0e-9,
    "IV": 4.0e-9,
    "V": 4.0e-9,
    "VI": 4.0e-9,
    "void_organelle": 4.0e-9,
}

# Chromosome-level recombination rate (~3e-9 per base per generation)
_recombination_rate = {
    "I": 3.0e-9,
    "II": 3.0e-9,
    "III": 3.0e-9,
    "IV": 3.0e-9,
    "V": 3.0e-9,
    "VI": 3.0e-9,
    "void_organelle": 3.0e-9,
}

# Ploidy per chromosome (diploid)
_ploidy = {
    "I": 2,
    "II": 2,
    "III": 2,
    "IV": 2,
    "V": 2,
    "VI": 2,
    "void_organelle": 2,
}

_genome = stdvoidsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=_genome_citations,
)

_species = stdvoidsim.Species(
    id="BybWor",
    ensembl_id="byakhee_voidwing",
    name="Byakhee voidwing",
    common_name="Byakhee",
    separate_sexes=True,
    genome=_genome,
    generation_time=10,
    population_size=200000,
    ploidy=2,
    citations=_species_citations,
)

stdvoidsim.register_species(_species)
