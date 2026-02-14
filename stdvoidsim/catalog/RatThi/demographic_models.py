"""
Demographic models for Rattus magicus (Rat-Thing).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdvoidsim

_species = stdvoidsim.get_species("RatThi")

###########################################################################
#
# Demographic models
#
###########################################################################


def _witch_house_plague():
    id = "WitchHousePlague_1G32"
    description = "Witch trial purge model for Rat-Things"
    long_description = """
        Single population model of Rat-Thing population dynamics through
        witch trial eras. Three epochs: (1) a modern phase with effective
        population size 50000, (2) a witch trial purge period beginning 500
        generations ago with N=1000, and (3) a colonial era beginning 2000
        generations ago with N=100000. Based on the work of Gilman et al.
        (1932).
    """
    populations = [
        stdvoidsim.Population(
            id="WitchHouse",
            description="Witch House colony -- Rat-Things in Arkham",
        ),
    ]

    citations = [
        stdvoidsim.Citation(
            author="Gilman et al.",
            year=1932,
            doi="https://doi.org/10.1666/void.ratthing.demog.1",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Modern phase: N=50000
    # Witch trial purge at T=500 gen: N=1000
    # Colonial era at T=2000 gen: N=100000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=50000,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=500,
            initial_size=1000,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=2000,
            initial_size=100000,
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
        generation_time=1,
        mutation_rate=2e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_witch_house_plague())


def _familiar_lineage():
    id = "FamiliarLineage_2G32"
    description = "Two population model of Feral Colony and Witch-Bound Rat-Things"
    long_description = """
        Two population model describing the divergence of the Feral Colony
        and Witch-Bound Rat-Things. The ancestral population of size 100000
        splits at 1000 generations ago. The Feral Colony maintains a size
        of 50000. The Witch-Bound lineage goes through a bottleneck of 100
        individuals before expanding to 10000. Based on the work of Gilman
        et al. (1932).
    """
    populations = [
        stdvoidsim.Population(
            id="FeralColony",
            description="Feral Colony -- free-roaming Rat-Things",
        ),
        stdvoidsim.Population(
            id="WitchBound",
            description="Witch-Bound -- familiar Rat-Things",
        ),
    ]

    citations = [
        stdvoidsim.Citation(
            author="Gilman et al.",
            year=1932,
            doi="https://doi.org/10.1666/void.ratthing.demog.2",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Present day: FeralColony N=50000, WitchBound N=10000
    # At T=500 gen ago: WitchBound bottleneck N=100
    # At T=1000 gen ago: populations merge into ancestral pop N=100000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=50000,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=10000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Witch-Bound bottleneck
        msprime.PopulationParametersChange(
            time=500,
            initial_size=100,
            population_id=1,
        ),
        # At 1000 generations ago, the two populations merge
        # (WitchBound merge into FeralColony going backwards in time)
        msprime.MassMigration(
            time=1000,
            source=1,
            destination=0,
            proportion=1.0,
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=1000,
            initial_size=100000,
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
        generation_time=1,
        mutation_rate=2e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_familiar_lineage())
