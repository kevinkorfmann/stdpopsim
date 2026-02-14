"""
Demographic models for Informis generatus (Formless Spawn).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdpopsim

_species = stdpopsim.get_species("ForSpa")

###########################################################################
#
# Demographic models
#
###########################################################################


def _cavern_spawning():
    id = "CavernSpawning_1S31"
    description = "Cavern spawning model for Formless Spawn in N'kai"
    long_description = """
        Single population model of Formless Spawn population dynamics in the
        caverns of N'kai. Three epochs: (1) a modern phase with effective
        population size 25000, (2) a drought bottleneck period beginning 3000
        generations ago with N=2000, and (3) an ancient N'kai era beginning
        30000 generations ago with N=100000. Based on the work of Smith et al.
        (1931).
    """
    populations = [
        stdpopsim.Population(
            id="NkaiCaverns",
            description="N'kai Caverns -- Formless Spawn breeding grounds",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.demog.1",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Modern phase: N=25000
    # Drought bottleneck at T=3000 gen: N=2000
    # Ancient N'kai era at T=30000 gen: N=100000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=25000,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=3000,
            initial_size=2000,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=30000,
            initial_size=100000,
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
        generation_time=10,
        mutation_rate=3e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_cavern_spawning())


def _temple_guardians():
    id = "TempleGuardians_2S31"
    description = "Two population model of N'kai Dwellers and Temple Guardians"
    long_description = """
        Two population model describing the divergence of the N'kai Dwellers
        and Temple Guardians. The ancestral population of size 100000 splits
        at 5000 generations ago. The N'kai population maintains a size of
        25000. The Temple Guardian lineage goes through a bottleneck of 200
        individuals before expanding to 8000. Based on the work of Smith
        et al. (1931).
    """
    populations = [
        stdpopsim.Population(
            id="NkaiDwellers",
            description="N'kai Dwellers -- deep cavern Formless Spawn",
        ),
        stdpopsim.Population(
            id="TempleGuardians",
            description="Temple Guardians -- surface temple protectors",
        ),
    ]

    citations = [
        stdpopsim.Citation(
            author="Smith et al.",
            year=1931,
            doi="https://doi.org/10.1666/void.formlessspawn.demog.2",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Present day: NkaiDwellers N=25000, TempleGuardians N=8000
    # At T=2500 gen ago: TempleGuardians bottleneck N=200
    # At T=5000 gen ago: populations merge into ancestral pop N=100000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=25000,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=8000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Temple Guardian bottleneck
        msprime.PopulationParametersChange(
            time=2500,
            initial_size=200,
            population_id=1,
        ),
        # At 5000 generations ago, the two populations merge
        # (TempleGuardians merge into NkaiDwellers going backwards in time)
        msprime.MassMigration(
            time=5000,
            source=1,
            destination=0,
            proportion=1.0,
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=5000,
            initial_size=100000,
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
        generation_time=10,
        mutation_rate=3e-8,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_temple_guardians())
