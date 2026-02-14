"""
Demographic models for Chaugnarus faugnis (Chaugnar Faugn).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime

import stdvoidsim

_species = stdvoidsim.get_species("ChaFau")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim

_long_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


# -------------------------------------------------------------------------
# HillShrine_1L32: Single population three-epoch model
# -------------------------------------------------------------------------


def _hill_shrine():
    id = "HillShrine_1L32"
    description = "Single population three-epoch model of Chaugnar Faugn"
    long_description = """
        Single population model of Chaugnar Faugn demographic history. Three
        epochs: modern shrine population with effective population size 200,
        a worshipper-fed expansion beginning 500 generations ago with N=50,
        and an ancient migration era beginning 5,000 generations ago with
        N=2,000. Based on the Necronomicon (Lovecraft)..
    """
    citations = [_long_et_al]

    populations = [
        stdvoidsim.Population(
            id="ShrineEntities",
            description="Chaugnar Faugn shrine entities of the Pyrenees",
        ),
    ]

    # Modern shrine: N=200
    # Worshipper-fed expansion at T=500 gen: N=50
    # Ancient migration at T=5,000 gen: N=2,000
    N_modern = 200
    N_expansion = 50
    N_ancient = 2000

    T_expansion = 500
    T_migration = 5000

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_modern,
            metadata={
                "name": "ShrineEntities",
                "description": "Chaugnar Faugn shrine entities of the Pyrenees",
            },
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=T_expansion, initial_size=N_expansion, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_migration, initial_size=N_ancient, population_id=0
        ),
    ]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=10000,
        mutation_rate=2e-10,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_hill_shrine())


# -------------------------------------------------------------------------
# MigrationFromAsia_2L32: Two population model
# -------------------------------------------------------------------------


def _migration_from_asia():
    id = "MigrationFromAsia_2L32"
    description = "Two-population model of Pyrenees Shrine and Asian Origin Chaugnar Faugn"
    long_description = """
        Two-population model representing Pyrenees Shrine entities and
        Asian Origin entities of Chaugnar Faugn. An ancestral population
        of size 2,000 splits at 2,000 generations ago. The Pyrenees
        population maintains a size of 200. The Asian Origin lineage
        goes through a bottleneck of 20 individuals before expanding
        to 100 in the present day. Based on the Pyrenees expeditions
        of Necronomicon (Lovecraft)..
    """
    citations = [_long_et_al]

    populations = [
        stdvoidsim.Population(
            id="PyreneesShrine",
            description="Pyrenees Shrine entities -- western manifestations",
        ),
        stdvoidsim.Population(
            id="AsianOrigin",
            description="Asian Origin entities -- ancestral eastern population",
        ),
    ]

    # Parameters
    N_ancestral = 2000
    N_pyrenees = 200
    N_asian_modern = 100
    N_asian_bottleneck = 20
    T_split = 2000

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_pyrenees,
            metadata={
                "name": "PyreneesShrine",
                "description": "Pyrenees Shrine entities -- western manifestations",
            },
        ),
        msprime.PopulationConfiguration(
            initial_size=N_asian_modern,
            metadata={
                "name": "AsianOrigin",
                "description": "Asian Origin entities -- ancestral eastern population",
            },
        ),
    ]

    T_bottleneck = 1000  # bottleneck before the split

    demographic_events = [
        # Asian Origin bottleneck
        msprime.PopulationParametersChange(
            time=T_bottleneck, initial_size=N_asian_bottleneck, population_id=1
        ),
        # Split: Asian Origin merges back into Pyrenees Shrine at T_split
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
        generation_time=10000,
        mutation_rate=2e-10,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_migration_from_asia())
