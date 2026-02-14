"""
Demographic models for Yithianus temporalis (Great Race of Yith).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdvoidsim

_species = stdvoidsim.get_species("YitGre")

###########################################################################
#
# Demographic models
#
###########################################################################


def _temporal_migration():
    id = "TemporalMigration_1P35"
    description = "Three epoch model of Great Race of Yith temporal migration"
    long_description = """
        Single population model of the Great Race of Yith in Pnakotus.
        Three epochs: (1) a modern phase with effective population size 50000,
        (2) a post-polyp-war bottleneck beginning 5000 generations ago with
        N=10000, and (3) a golden library age beginning 50000 generations ago
        with N=500000. Based on the studies of Peaslee et al. (1935).
    """
    populations = [
        stdvoidsim.Population(
            id="Yithians",
            description="Yithians -- cone-shaped time-traveling entities",
        ),
    ]

    citations = [
        stdvoidsim.Citation(
            author="Peaslee et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.yitgre.demog.1",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Modern phase: N=50000
    # Post-polyp-war bottleneck at T=5000 gen: N=10000
    # Golden library age at T=50000 gen: N=500000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=50000,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=5000,
            initial_size=10000,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=50000,
            initial_size=500000,
            population_id=0,
        ),
    ]

    migration_matrix = [[0]]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=500,
        mutation_rate=3e-9,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_temporal_migration())


def _conic_mind_swap():
    id = "ConicMindSwap_2P35"
    description = "Two population model of Pnakotus City and Remote Outpost Yithians"
    long_description = """
        Two population model describing the divergence of Pnakotus City and
        Remote Outpost Yithian populations. The ancestral population of size
        500000 splits at 20000 generations ago. The Pnakotus City population
        maintains a size of 50000. The Remote Outpost lineage goes through a
        bottleneck of 500 individuals before expanding to 20000. Based on
        Peaslee et al. (1935).
    """
    populations = [
        stdvoidsim.Population(
            id="PnakotusCity",
            description="Pnakotus City -- central Yithian civilization",
        ),
        stdvoidsim.Population(
            id="RemoteOutposts",
            description="Remote Outposts -- peripheral Yithian settlements",
        ),
    ]

    citations = [
        stdvoidsim.Citation(
            author="Peaslee et al.",
            year=1935,
            doi="https://doi.org/10.1666/void.yitgre.demog.2",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Present day: PnakotusCity N=50000, RemoteOutposts N=20000
    # At T=5000 gen ago: RemoteOutposts bottleneck N=500
    # At T=20000 gen ago: populations merge into ancestral pop N=500000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=50000,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=20000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Remote Outpost bottleneck at 5000 generations ago
        msprime.PopulationParametersChange(
            time=5000,
            initial_size=500,
            population_id=1,
        ),
        # At 20000 generations ago, the two populations merge
        msprime.MassMigration(
            time=20000,
            source=1,
            destination=0,
            proportion=1.0,
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=20000,
            initial_size=500000,
            population_id=0,
        ),
    ]

    migration_matrix = [
        [0, 0],
        [0, 0],
    ]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=500,
        mutation_rate=3e-9,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_conic_mind_swap())
