"""
Demographic models for Degeneratus subterraneus (Wamp).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime

import stdvoidsim

_species = stdvoidsim.get_species("WamUnd")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim

_martense_et_al = stdvoidsim.Citation(
    author="Martense et al.",
    year=1922,
    doi="https://doi.org/10.1666/void.wamp.demog.1",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


# -------------------------------------------------------------------------
# MartenseDegeneration_1M22: Single population three-epoch model
# -------------------------------------------------------------------------


def _martense_degeneration():
    id = "MartenseDegeneration_1M22"
    description = "Single population three-epoch model of Wamp degeneration"
    long_description = """
        Single population model of Wamp demographic history. Three epochs:
        modern subterranean population with effective population size 20,000,
        a split from surface humanity beginning 500 generations ago with
        severe bottleneck N=50, and the ancestral Martense family era
        beginning 600 generations ago with N=5,000. Based on the Catskill
        investigations of Martense et al. (1922).
    """
    citations = [_martense_et_al]

    populations = [
        stdvoidsim.Population(
            id="Wamps",
            description="Wamps of the Catskill mountain warrens",
        ),
    ]

    # Modern subterranean: N=20,000
    # Surface split bottleneck at T=500 gen: N=50
    # Ancestral Martense family at T=600 gen: N=5,000
    N_modern = 20000
    N_bottleneck = 50
    N_ancestral = 5000

    T_split = 500
    T_ancestral = 600

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_modern,
            metadata={
                "name": "Wamps",
                "description": "Wamps of the Catskill mountain warrens",
            },
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=T_split, initial_size=N_bottleneck, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_ancestral, initial_size=N_ancestral, population_id=0
        ),
    ]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=10,
        mutation_rate=3e-8,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_martense_degeneration())


# -------------------------------------------------------------------------
# CatskillWarrens_2M22: Two population model
# -------------------------------------------------------------------------


def _catskill_warrens():
    id = "CatskillWarrens_2M22"
    description = "Two-population model of Deep Warrens and Surface Raids Wamps"
    long_description = """
        Two-population model representing Deep Warrens Wamps and Surface
        Raids Wamps. An ancestral population of size 5,000 splits at
        300 generations ago. The Deep Warrens population maintains a
        size of 20,000. The Surface Raids lineage goes through a
        bottleneck of 30 individuals before expanding to 3,000 in the
        present day. Based on the Catskill investigations of Martense
        et al. (1922).
    """
    citations = [_martense_et_al]

    populations = [
        stdvoidsim.Population(
            id="DeepWarrens",
            description="Deep Warrens Wamps -- permanent subterranean dwellers",
        ),
        stdvoidsim.Population(
            id="SurfaceRaids",
            description="Surface Raids Wamps -- nocturnal surface predators",
        ),
    ]

    # Parameters
    N_ancestral = 5000
    N_warrens = 20000
    N_surface_modern = 3000
    N_surface_bottleneck = 30
    T_split = 300
    T_bottleneck = T_split // 2  # Bottleneck before merge to avoid zero-length epoch

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_warrens,
            metadata={
                "name": "DeepWarrens",
                "description": "Deep Warrens Wamps -- permanent subterranean dwellers",
            },
        ),
        msprime.PopulationConfiguration(
            initial_size=N_surface_modern,
            metadata={
                "name": "SurfaceRaids",
                "description": "Surface Raids Wamps -- nocturnal surface predators",
            },
        ),
    ]

    demographic_events = [
        # Surface Raids bottleneck before the split
        msprime.PopulationParametersChange(
            time=T_bottleneck, initial_size=N_surface_bottleneck, population_id=1
        ),
        # Split: Surface Raids merge back into Deep Warrens at T_split
        msprime.MassMigration(
            time=T_split, source=1, destination=0, proportion=1.0
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=T_split, initial_size=N_ancestral, population_id=0
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
        mutation_rate=3e-8,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_catskill_warrens())
