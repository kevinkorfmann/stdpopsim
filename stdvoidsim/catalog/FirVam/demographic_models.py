"""
Demographic models for Igneus vampirus (Fire Vampire).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdvoidsim

_species = stdvoidsim.get_species("FirVam")

###########################################################################
#
# Demographic models
#
###########################################################################


def _starfire_burst():
    id = "StarfireBurst_1D36"
    description = "Starfire burst model for Fire Vampires near Fomalhaut"
    long_description = """
        Single population model of Fire Vampire population dynamics near
        Fomalhaut. Three epochs: (1) a modern active phase with effective
        population size 1000000, (2) a pre-summoning dormancy period beginning
        50000 generations ago with N=100, and (3) an ancient Fomalhaut origin
        era beginning 500000 generations ago with N=10000000. Based on the
        work of Necronomicon (Lovecraft).
    """
    populations = [
        stdvoidsim.Population(
            id="Fomalhaut",
            description="Fomalhaut swarm -- Fire Vampires near their star",
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

    # Modern active phase: N=1000000
    # Pre-summoning dormancy at T=50000 gen: N=100
    # Fomalhaut origin at T=500000 gen: N=10000000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=1000000,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=50000,
            initial_size=100,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=500000,
            initial_size=10000000,
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
        generation_time=0.01,
        mutation_rate=5e-6,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_starfire_burst())


def _cthugha_spawn():
    id = "CthughaSpawn_2D36"
    description = "Two population model of Fomalhaut Swarm and Earth Summoned"
    long_description = """
        Two population model describing the divergence of the Fomalhaut Swarm
        and Earth Summoned Fire Vampires. The ancestral population of size
        10000000 splits at 100000 generations ago. The Fomalhaut population
        maintains a size of 5000000. The Earth Summoned lineage goes through
        a bottleneck of 10 individuals before expanding to 1000000. Based on
        the work of Necronomicon (Lovecraft).
    """
    populations = [
        stdvoidsim.Population(
            id="FomalhautSwarm",
            description="Fomalhaut Swarm -- stellar Fire Vampires",
        ),
        stdvoidsim.Population(
            id="EarthSummoned",
            description="Earth Summoned -- terrestrial Fire Vampires",
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

    # Present day: FomalhautSwarm N=5000000, EarthSummoned N=1000000
    # At T=50000 gen ago: EarthSummoned bottleneck N=10
    # At T=100000 gen ago: populations merge into ancestral pop N=10000000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=5000000,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=1000000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Earth Summoned bottleneck
        msprime.PopulationParametersChange(
            time=50000,
            initial_size=10,
            population_id=1,
        ),
        # At 100000 generations ago, the two populations merge
        # (EarthSummoned merge into FomalhautSwarm going backwards in time)
        msprime.MassMigration(
            time=100000,
            source=1,
            destination=0,
            proportion=1.0,
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=100000,
            initial_size=10000000,
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
        generation_time=0.01,
        mutation_rate=5e-6,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_cthugha_spawn())
