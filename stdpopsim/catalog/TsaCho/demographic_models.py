"""
Demographic models for Tsathoggua choriensis (Tcho-Tcho).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdpopsim

_species = stdpopsim.get_species("TsaCho")

###########################################################################
#
# Demographic models
#
###########################################################################


def _plateau_tribes():
    id = "PlateauTribes_1D33"
    description = "Three epoch model of Tcho-Tcho plateau tribes"
    long_description = """
        Single population model of the Tcho-Tcho people on the plateau.
        Three epochs: (1) a modern phase with effective population size 70000,
        (2) a persecution decline beginning 500 generations ago with N=20000,
        and (3) an ancient empire era beginning 5000 generations ago with
        N=200000. Based on the studies of Derleth et al. (1933).
    """
    populations = [
        stdpopsim.Population(
            id="TchoTcho",
            description="Tcho-Tcho -- degenerate human-like tribe serving dark gods",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="Derleth et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.tsacho.demog.1",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Modern phase: N=70000
    # Persecution decline at T=500 gen: N=20000
    # Ancient empire at T=5000 gen: N=200000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=70000,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=500,
            initial_size=20000,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=5000,
            initial_size=200000,
            population_id=0,
        ),
    ]

    migration_matrix = [[0]]

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=25,
        mutation_rate=1.5e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_plateau_tribes())


def _tainted_lineage():
    id = "TaintedLineage_2D33"
    description = "Two population model of Highland Tribes and Lowland Infiltrator Tcho-Tcho"
    long_description = """
        Two population model describing the divergence of Highland Tribes and
        Lowland Infiltrator Tcho-Tcho populations. The ancestral population of
        size 200000 splits at 2000 generations ago. The Highland Tribe
        population maintains a size of 70000. The Lowland Infiltrator lineage
        goes through a bottleneck of 500 individuals before expanding to
        30000. Based on Derleth et al. (1933).
    """
    populations = [
        stdpopsim.Population(
            id="HighlandTribes",
            description="Highland Tribes -- traditional Tcho-Tcho plateau dwellers",
        ),
        stdpopsim.Population(
            id="LowlandInfiltrators",
            description="Lowland Infiltrators -- Tcho-Tcho dispersed among humans",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="Derleth et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.tsacho.demog.2",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Present day: HighlandTribes N=70000, LowlandInfiltrators N=30000
    # At T=500 gen ago: LowlandInfiltrators bottleneck N=500
    # At T=2000 gen ago: populations merge into ancestral pop N=200000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=70000,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=30000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Lowland Infiltrator bottleneck at 500 generations ago
        msprime.PopulationParametersChange(
            time=500,
            initial_size=500,
            population_id=1,
        ),
        # At 2000 generations ago, the two populations merge
        msprime.MassMigration(
            time=2000,
            source=1,
            destination=0,
            proportion=1.0,
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=2000,
            initial_size=200000,
            population_id=0,
        ),
    ]

    migration_matrix = [
        [0, 0],
        [0, 0],
    ]

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=25,
        mutation_rate=1.5e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_tainted_lineage())
