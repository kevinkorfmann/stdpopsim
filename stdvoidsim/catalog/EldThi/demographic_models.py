import msprime

import stdvoidsim

_species = stdvoidsim.get_species("EldThi")

###########################################################################
#
# Demographic models
#
###########################################################################

# -------------------------------------------------------------------------
# CivilizationCollapse_1D31: Single population model with four epochs
# -------------------------------------------------------------------------

_cc_ref = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _civilization_collapse():
    id = "CivilizationCollapse_1D31"
    description = (
        "Single population four-epoch model of Elder Thing civilization decline"
    )
    long_description = """
        A single-population model with four epochs representing the history
        of the Elder Thing civilization on Earth. The modern era has only
        10000 remnant individuals. The shoggoth revolt 1000 generations ago
        reduced the population from a golden age of 1000000 (beginning 5000
        generations ago) to 100000. The founding colonization from the stars
        began 50000 generations ago with 5000 individuals.
    """
    citations = [_cc_ref]

    populations = [
        stdvoidsim.Population(
            id="ElderThings",
            description="Elder Thing civilization",
        ),
    ]

    # Modern: N=10000
    # T=1000: shoggoth revolt aftermath N=100000
    # T=5000: golden age N=1000000
    # T=50000: founding colonization N=5000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=10000,
            metadata={
                "name": "ElderThings",
                "description": "Elder Thing civilization",
            },
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=1000, initial_size=100000, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=5000, initial_size=1000000, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=50000, initial_size=5000, population_id=0
        ),
    ]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=1000,
        mutation_rate=1e-9,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_civilization_collapse())


# -------------------------------------------------------------------------
# AntarcticRetreat_2L30: Two population model (Surface and Underground)
# -------------------------------------------------------------------------

_ar_ref = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _antarctic_retreat():
    id = "AntarcticRetreat_2L30"
    description = (
        "Two-population model of Elder Thing surface cities and underground refuges"
    )
    long_description = """
        A two-population model representing the retreat of Elder Things
        underground. The ancestral surface civilization had N=1000000 during
        the golden age. At 1000 generations ago, climate change forced a
        split: some Elder Things retreated to underground refuges (stable
        N=10000), while the surface population declined from 5000 to 500
        in the present day.
    """
    citations = [_ar_ref]

    populations = [
        stdvoidsim.Population(
            id="Surface",
            description="Surface city Elder Things",
        ),
        stdvoidsim.Population(
            id="Underground",
            description="Underground refuge Elder Things",
        ),
    ]

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=500,
            metadata={"name": "Surface", "description": "Surface city Elder Things"},
        ),
        msprime.PopulationConfiguration(
            initial_size=10000,
            metadata={
                "name": "Underground",
                "description": "Underground refuge Elder Things",
            },
        ),
    ]

    demographic_events = [
        # Surface population was 5000 right after the split
        msprime.PopulationParametersChange(time=0, initial_size=500, population_id=0),
        # At the time of the split, surface had size 5000
        msprime.PopulationParametersChange(
            time=1000, initial_size=5000, population_id=0
        ),
        # Underground merges back into Surface (ancestral population)
        msprime.MassMigration(time=1000, source=1, destination=0, proportion=1.0),
        # Ancestral population size (golden age)
        msprime.PopulationParametersChange(
            time=1000, initial_size=1000000, population_id=0
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
        generation_time=1000,
        mutation_rate=1e-9,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_antarctic_retreat())
