import msprime

import stdpopsim

_species = stdpopsim.get_species("MiGFun")

###########################################################################
#
# Demographic models
#
###########################################################################

# -------------------------------------------------------------------------
# YuggothColony_1A30: Single population model with three epochs
# -------------------------------------------------------------------------

_yc_ref = stdpopsim.Citation(
    author="Akeley et al.",
    year=1930,
    doi="https://doi.org/10.1666/void.migo.yuggothcolony",
    reasons={stdpopsim.CiteReason.DEM_MODEL},
)


def _yuggoth_colony():
    id = "YuggothColony_1A30"
    description = "Single population three-epoch model of Mi-Go colonization"
    long_description = """
        A single-population model with three epochs representing the history
        of a Mi-Go colony. The modern era has a Vermont mining colony of
        N=500000. A colonization bottleneck 10000 generations ago reduced
        the population to N=1000. Before that, in the Yuggoth homeworld
        era beginning 50000 generations ago, N=5000000 Mi-Go existed.
    """
    citations = [_yc_ref]

    populations = [
        stdpopsim.Population(
            id="MiGoColony",
            description="Mi-Go Vermont mining colony",
        ),
    ]

    # Modern: N=500000, Bottleneck at T=10000: N=1000, Yuggoth at T=50000: N=5000000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=500000,
            metadata={"name": "MiGoColony", "description": "Vermont mining colony"},
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=10000, initial_size=1000, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=50000, initial_size=5000000, population_id=0
        ),
    ]

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=5,
        mutation_rate=2e-8,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_yuggoth_colony())


# -------------------------------------------------------------------------
# InterplanetarySpread_2A30: Two population model (Yuggoth and Earth)
# -------------------------------------------------------------------------

_is_ref = stdpopsim.Citation(
    author="Akeley et al.",
    year=1930,
    doi="https://doi.org/10.1666/void.migo.interplanetaryspread",
    reasons={stdpopsim.CiteReason.DEM_MODEL},
)


def _interplanetary_spread():
    id = "InterplanetarySpread_2A30"
    description = "Two-population model of Yuggoth homeworld and Earth colony"
    long_description = """
        A two-population model representing the interplanetary spread of
        Mi-Go. The ancestral Yuggoth homeworld population (N=5000000) split
        10000 generations ago into the stable Yuggoth population (N=5000000)
        and an Earth colony that experienced a bottleneck to N=100 before
        expanding to N=500000 in the present day.
    """
    citations = [_is_ref]

    populations = [
        stdpopsim.Population(
            id="Yuggoth",
            description="Yuggoth homeworld population",
        ),
        stdpopsim.Population(
            id="Earth",
            description="Earth colony population",
        ),
    ]

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=5000000,
            metadata={"name": "Yuggoth", "description": "Yuggoth homeworld"},
        ),
        msprime.PopulationConfiguration(
            initial_size=500000,
            metadata={"name": "Earth", "description": "Earth colony"},
        ),
    ]

    T_split = 10000
    T_bottleneck = T_split // 2  # Bottleneck before merge to avoid zero-length epoch

    demographic_events = [
        # Earth colony had initial size of 100 right after the split
        msprime.PopulationParametersChange(
            time=T_bottleneck, initial_size=100, population_id=1
        ),
        # Earth colony merges back into Yuggoth at the split time
        msprime.MassMigration(
            time=T_split, source=1, destination=0, proportion=1.0
        ),
        # Ancestral Yuggoth population size
        msprime.PopulationParametersChange(
            time=T_split, initial_size=5000000, population_id=0
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
        generation_time=5,
        mutation_rate=2e-8,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_interplanetary_spread())
