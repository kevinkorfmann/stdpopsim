"""
Demographic models for Gnophkehus arcticus (Gnoph-Keh).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdpopsim

_species = stdpopsim.get_species("GnpKeh")

###########################################################################
#
# Demographic models
#
###########################################################################


def _hyperborean_ice_age():
    id = "HyperboreanIceAge_1H33"
    description = "Hyperborean ice age model for Gnoph-Keh"
    long_description = """
        Single population model of Gnoph-Keh population dynamics through
        the Hyperborean ice ages. Three epochs: (1) a modern phase with
        effective population size 12000, (2) an ice age expansion period
        beginning 2000 generations ago with N=50000, and (3) a pre-ice
        founding era beginning 20000 generations ago with N=5000. Based on
        the work of Howard et al. (1933).
    """
    populations = [
        stdpopsim.Population(
            id="Hyperborea",
            description="Hyperborea -- arctic Gnoph-Keh homeland",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="Howard et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.gnophkeh.demog.1",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Modern phase: N=12000
    # Ice age expansion at T=2000 gen: N=50000
    # Pre-ice founding at T=20000 gen: N=5000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=12000,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=2000,
            initial_size=50000,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=20000,
            initial_size=5000,
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
        generation_time=40,
        mutation_rate=4e-9,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_hyperborean_ice_age())


def _arctic_split():
    id = "ArcticSplit_2H33"
    description = "Two population model of Hyperborean Core and Lomar Colony"
    long_description = """
        Two population model describing the divergence of the Hyperborean
        Core and Lomar Colony Gnoph-Keh. The ancestral population of size
        50000 splits at 5000 generations ago. The Hyperborean Core maintains
        a size of 12000. The Lomar Colony lineage goes through a bottleneck
        of 200 individuals before expanding to 6000. Based on the work of
        Howard et al. (1933).
    """
    populations = [
        stdpopsim.Population(
            id="HyperboreanCore",
            description="Hyperborean Core -- primary arctic population",
        ),
        stdpopsim.Population(
            id="LomarColony",
            description="Lomar Colony -- southern expansion population",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="Howard et al.",
            year=1933,
            doi="https://doi.org/10.1666/void.gnophkeh.demog.2",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Present day: HyperboreanCore N=12000, LomarColony N=6000
    # At T=2500 gen ago: LomarColony bottleneck N=200
    # At T=5000 gen ago: populations merge into ancestral pop N=50000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=12000,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=6000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Lomar Colony bottleneck
        msprime.PopulationParametersChange(
            time=2500,
            initial_size=200,
            population_id=1,
        ),
        # At 5000 generations ago, the two populations merge
        # (LomarColony merge into HyperboreanCore going backwards in time)
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
        generation_time=40,
        mutation_rate=4e-9,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_arctic_split())
