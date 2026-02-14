"""
Demographic models for Tsathoggua somnolentis (Tsathoggua).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdpopsim

_species = stdpopsim.get_species("TsaGod")

###########################################################################
#
# Demographic models
#
###########################################################################


def _slothful_dormancy():
    id = "SlothfulDormancy_1S31"
    description = "Cyclic dormancy model for Tsathoggua in N'kai"
    long_description = """
        Single population model of Tsathoggua's slothful dormancy in the
        caverns of N'kai. Three epochs: (1) a modern phase with effective
        population size 100, (2) a brief awakening period beginning 500
        generations ago with N=1000, and (3) a deep slumber era beginning
        5000 generations ago with N=10. Based on the work of Smith et al.
        (1931).
    """
    populations = [
        stdpopsim.Population(
            id="Nkai",
            description="N'kai cavern dwellers -- Tsathoggua and kin",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.demog.1",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Modern phase: N=100
    # Brief awakening at T=500 gen: N=1000
    # Deep slumber at T=5000 gen: N=10
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=100,
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
            time=5000,
            initial_size=10,
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
        generation_time=50000,
        mutation_rate=5e-10,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_slothful_dormancy())


def _nkai_caverns():
    id = "NkaiCaverns_2S31"
    description = "Two population model of N'kai Depths and Surface Avatars"
    long_description = """
        Two population model describing the divergence of the N'kai Depths
        dwellers and Surface Avatars. The ancestral population of size 1000
        splits at 200 generations ago. The N'kai population maintains a size
        of 100. The Surface Avatar lineage goes through a bottleneck of 5
        individuals before expanding to 50. Based on the work of Smith et al.
        (1931).
    """
    populations = [
        stdpopsim.Population(
            id="NkaiDepths",
            description="N'kai Depths -- deep cavern dwellers",
        ),
        stdpopsim.Population(
            id="SurfaceAvatars",
            description="Surface Avatars -- terrestrial manifestations",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.tsathoggua.demog.2",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Present day: NkaiDepths N=100, SurfaceAvatars N=50
    # At T=100 gen ago: SurfaceAvatars bottleneck N=5
    # At T=200 gen ago: populations merge into ancestral pop N=1000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=100,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=50,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Surface Avatar bottleneck
        msprime.PopulationParametersChange(
            time=100,
            initial_size=5,
            population_id=1,
        ),
        # At 200 generations ago, the two populations merge
        # (SurfaceAvatars merge into NkaiDepths going backwards in time)
        msprime.MassMigration(
            time=200,
            source=1,
            destination=0,
            proportion=1.0,
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=200,
            initial_size=1000,
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
        generation_time=50000,
        mutation_rate=5e-10,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_nkai_caverns())
