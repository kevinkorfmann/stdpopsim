"""
Demographic models for Araneus lengensis (Leng Spider).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdvoidsim

_species = stdvoidsim.get_species("LenSpi")

###########################################################################
#
# Demographic models
#
###########################################################################


def _plateau_dominion():
    id = "PlateauDominion_1C26"
    description = "Three epoch model of Leng Spider plateau dominion"
    long_description = """
        Single population model of the Leng Spiders on the Plateau of Leng.
        Three epochs: (1) a modern phase with effective population size 20000,
        (2) a slave trade expansion beginning 5000 generations ago with N=5000,
        and (3) an ancient colonization era beginning 50000 generations ago
        with N=60000. Based on the Necronomicon (Lovecraft).
    """
    populations = [
        stdvoidsim.Population(
            id="LengSpiders",
            description="Leng Spiders -- giant purple arachnids of the plateau",
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

    # Modern phase: N=20000
    # Slave trade expansion at T=5000 gen: N=5000
    # Ancient colonization at T=50000 gen: N=60000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=20000,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=5000,
            initial_size=5000,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=50000,
            initial_size=60000,
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
        generation_time=10,
        mutation_rate=1e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_plateau_dominion())


def _web_network():
    id = "WebNetwork_2C26"
    description = "Two population model of Plateau Core and Vale Outpost Leng Spiders"
    long_description = """
        Two population model describing the divergence of Plateau Core and
        Vale Outpost Leng Spider populations. The ancestral population of size
        60000 splits at 15000 generations ago. The Plateau Core population
        maintains a size of 20000. The Vale Outpost lineage goes through a
        bottleneck of 300 individuals before expanding to 8000. Based on
        Necronomicon (Lovecraft).
    """
    populations = [
        stdvoidsim.Population(
            id="PlateauCore",
            description="Plateau Core -- central Leng Spider civilization",
        ),
        stdvoidsim.Population(
            id="ValeOutposts",
            description="Vale Outposts -- peripheral Leng Spider settlements",
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

    # Present day: PlateauCore N=20000, ValeOutposts N=8000
    # At T=5000 gen ago: ValeOutposts bottleneck N=300
    # At T=15000 gen ago: populations merge into ancestral pop N=60000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=20000,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=8000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Vale Outpost bottleneck at 5000 generations ago
        msprime.PopulationParametersChange(
            time=5000,
            initial_size=300,
            population_id=1,
        ),
        # At 15000 generations ago, the two populations merge
        msprime.MassMigration(
            time=15000,
            source=1,
            destination=0,
            proportion=1.0,
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=15000,
            initial_size=60000,
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
        generation_time=10,
        mutation_rate=1e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_web_network())
