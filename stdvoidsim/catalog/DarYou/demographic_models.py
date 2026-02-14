"""
Demographic models for Obscurus silvanus (Dark Young).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdvoidsim

_species = stdvoidsim.get_species("DarYou")

###########################################################################
#
# Demographic models
#
###########################################################################


def _forest_expansion():
    id = "ForestExpansion_1B35"
    description = "Three epoch model of Dark Young forest expansion"
    long_description = """
        Single population model of the Dark Young of Shub-Niggurath.
        Three epochs: (1) a modern phase with effective population size 35000,
        (2) a woodland retreat beginning 1000 generations ago with N=5000, and
        (3) an ancient grove era beginning 10000 generations ago with N=80000.
        Based on the Necronomicon (Lovecraft).
    """
    populations = [
        stdvoidsim.Population(
            id="DarkYoung",
            description="Dark Young -- tentacled tree-spawn of Shub-Niggurath",
        ),
    ]

    citations = [
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Modern phase: N=35000
    # Woodland retreat at T=1000 gen: N=5000
    # Ancient grove at T=10000 gen: N=80000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=35000,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=1000,
            initial_size=5000,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=10000,
            initial_size=80000,
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
        generation_time=50,
        mutation_rate=2e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_forest_expansion())


def _mother_spawn():
    id = "MotherSpawn_2B35"
    description = "Two population model of Forest Groves and Summoned Dark Young"
    long_description = """
        Two population model describing the divergence of Forest Groves and
        Summoned Dark Young. The ancestral population of size 80000 splits at
        2000 generations ago. The Forest Grove population maintains a size of
        35000. The Summoned lineage goes through a bottleneck of 50 individuals
        before expanding to 10000. Based on the Necronomicon (Lovecraft).
    """
    populations = [
        stdvoidsim.Population(
            id="ForestGroves",
            description="Forest Groves -- self-sustaining Dark Young populations",
        ),
        stdvoidsim.Population(
            id="Summoned",
            description="Summoned -- Dark Young called forth by ritual",
        ),
    ]

    citations = [
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Present day: ForestGroves N=35000, Summoned N=10000
    # At T=500 gen ago: Summoned bottleneck N=50
    # At T=2000 gen ago: populations merge into ancestral pop N=80000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=35000,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=10000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Summoned bottleneck at 500 generations ago
        msprime.PopulationParametersChange(
            time=500,
            initial_size=50,
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
            initial_size=80000,
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
        generation_time=50,
        mutation_rate=2e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_mother_spawn())
