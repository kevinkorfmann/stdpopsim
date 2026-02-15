import msprime

import stdvoidsim

_species = stdvoidsim.get_species("HasKin")

###########################################################################
#
# Demographic models
#
###########################################################################

# -------------------------------------------------------------------------
# YellowSignSpread_1C95: Single population model with three epochs
# -------------------------------------------------------------------------

_ys_ref = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _yellow_sign_spread():
    id = "YellowSignSpread_1C95"
    description = "Single population three-epoch model of Yellow Sign memetic spread"
    long_description = """
        A single-population model with three epochs representing the memetic
        history of the King in Yellow. The modern era has 2000 influenced minds
        (memetic expansion). A dark age dormancy bottleneck 500 generations ago
        reduced the population to 100. Before that, the ancient Carcosa founding
        era beginning 5000 generations ago had 10000 entities.
    """
    citations = [_ys_ref]

    populations = [
        stdvoidsim.Population(
            id="YellowSign",
            description="Carriers of the Yellow Sign memetic influence",
        ),
    ]

    # Modern: N=2000, Dark age T=500: N=100, Ancient Carcosa T=5000: N=10000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=2000,
            metadata={"name": "YellowSign", "description": "Yellow Sign carriers"},
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(time=500, initial_size=100, population_id=0),
        msprime.PopulationParametersChange(
            time=5000, initial_size=10000, population_id=0
        ),
    ]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=50,
        mutation_rate=5e-8,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_yellow_sign_spread())


# -------------------------------------------------------------------------
# CarcosaEarth_2C95: Two population model (Carcosa and Earth)
# -------------------------------------------------------------------------

_ce_ref = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _carcosa_earth():
    id = "CarcosaEarth_2C95"
    description = "Two-population model of Carcosa and Earth artistic contagion"
    long_description = """
        A two-population model representing the spread of Hastur's influence
        across dimensions. The ancestral population in Carcosa (N=10000) split
        200 generations ago when the play "The King in Yellow" was written,
        creating an Earth colony. Carcosa remains stable at N=5000. The Earth
        colony started with just 10 individuals (early readers of the play)
        and expanded to 2000 in the present day.
    """
    citations = [_ce_ref]

    populations = [
        stdvoidsim.Population(
            id="Carcosa",
            description="Home dimension population of Hastur entities",
        ),
        stdvoidsim.Population(
            id="Earth",
            description="Earth colony spread through artistic contagion",
        ),
    ]

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=5000,
            metadata={"name": "Carcosa", "description": "Carcosa home dimension"},
        ),
        msprime.PopulationConfiguration(
            initial_size=2000,
            metadata={"name": "Earth", "description": "Earth artistic contagion"},
        ),
    ]

    demographic_events = [
        # Earth colony had initial size of 10 right after the split
        msprime.PopulationParametersChange(time=0, initial_size=2000, population_id=1),
        # At the time of the split, merge Earth back into Carcosa
        msprime.MassMigration(time=200, source=1, destination=0, proportion=1.0),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=200, initial_size=10000, population_id=0
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
        generation_time=50,
        mutation_rate=5e-8,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_carcosa_earth())
