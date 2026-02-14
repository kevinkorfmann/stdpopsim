"""
Demographic models for Venator obscurus (Hunting Horror).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdpopsim

_species = stdpopsim.get_species("HunTin")

###########################################################################
#
# Demographic models
#
###########################################################################


def _dark_flight():
    id = "DarkFlight_1M33"
    description = "Three epoch model of Hunting Horror dark flight populations"
    long_description = """
        Single population model of Hunting Horrors serving Nyarlathotep.
        Three epochs: (1) a modern phase with effective population size 15000,
        (2) a Nyarlathotep summoning boom beginning 2000 generations ago with
        N=3000, and (3) an ancient void origin beginning 20000 generations ago
        with N=50000. Based on the studies of deMarigny et al. (1933).
    """
    populations = [
        stdpopsim.Population(
            id="DarkFlyers",
            description="Hunting Horrors -- dark serpentine flyers of the void",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="deMarigny et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.huntin.demog.1",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Modern phase: N=15000
    # Nyarlathotep summoning boom at T=2000 gen: N=3000
    # Ancient void origin at T=20000 gen: N=50000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=15000,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=2000,
            initial_size=3000,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=20000,
            initial_size=50000,
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
        generation_time=20,
        mutation_rate=6e-9,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_dark_flight())


def _nyarlathotep_service():
    id = "NyarlathService_2M33"
    description = "Two population model of Void Hunters and Earthbound Sentinels"
    long_description = """
        Two population model describing the divergence of Void Hunters and
        Earthbound Sentinels. The ancestral population of size 50000 splits at
        5000 generations ago. The Void Hunter population maintains a size of
        15000. The Earthbound Sentinel lineage goes through a bottleneck of 200
        individuals before expanding to 5000. Based on deMarigny et al. (1933).
    """
    populations = [
        stdpopsim.Population(
            id="VoidHunters",
            description="Void Hunters -- Hunting Horrors of the outer dark",
        ),
        stdpopsim.Population(
            id="EarthboundSentinels",
            description="Earthbound Sentinels -- terrestrial Hunting Horrors",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="deMarigny et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.huntin.demog.2",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Present day: VoidHunters N=15000, EarthboundSentinels N=5000
    # At T=1000 gen ago: EarthboundSentinels bottleneck N=200
    # At T=5000 gen ago: populations merge into ancestral pop N=50000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=15000,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=5000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Earthbound Sentinel bottleneck at 1000 generations ago
        msprime.PopulationParametersChange(
            time=1000,
            initial_size=200,
            population_id=1,
        ),
        # At 5000 generations ago, the two populations merge
        msprime.MassMigration(
            time=5000,
            source=1,
            destination=0,
            proportion=1.0,
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=5000,
            initial_size=50000,
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
        generation_time=20,
        mutation_rate=6e-9,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_nyarlathotep_service())
