"""
Demographic models for Felis ultharensis (Cat of Ulthar).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime

import stdvoidsim

_species = stdvoidsim.get_species("CatUlt")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim

_carter_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


# -------------------------------------------------------------------------
# UltharProtection_1C20: Single population three-epoch model
# -------------------------------------------------------------------------


def _ulthar_protection():
    id = "UltharProtection_1C20"
    description = "Single population three-epoch model of Ulthar cats"
    long_description = """
        Single population model of Cat of Ulthar demographic history. Three
        epochs: modern protected era with effective population size 100,000,
        a pre-protection-law era beginning 1,000 generations ago with N=30,000,
        and an ancient dreamlands origin beginning 20,000 generations ago with
        N=200,000. Based on the Necronomicon (Lovecraft).
    """
    citations = [_carter_et_al]

    populations = [
        stdvoidsim.Population(
            id="UltharCats",
            description="Cats of the city of Ulthar",
        ),
    ]

    # Modern protected era: N=100,000
    # Pre-protection-law at T=1,000 gen: N=30,000
    # Ancient dreamlands origin at T=20,000 gen: N=200,000
    N_modern = 100000
    N_pre_protection = 30000
    N_ancient = 200000

    T_protection = 1000
    T_origin = 20000

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_modern,
            metadata={
                "name": "UltharCats",
                "description": "Cats of the city of Ulthar",
            },
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=T_protection, initial_size=N_pre_protection, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_origin, initial_size=N_ancient, population_id=0
        ),
    ]

    return stdvoidsim.DemographicModel(
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


_species.add_demographic_model(_ulthar_protection())


# -------------------------------------------------------------------------
# DreamlandsPatrol_2C20: Two population model
# -------------------------------------------------------------------------


def _dreamlands_patrol():
    id = "DreamlandsPatrol_2C20"
    description = "Two-population model of Ulthar Temple Cats and Moon Expedition Force"
    long_description = """
        Two-population model representing Ulthar Temple Cats and the Moon
        Expedition Force. An ancestral population of size 200,000 splits at
        5,000 generations ago. The Temple Cats maintain a size of 100,000.
        The Moon Expedition Force goes through a bottleneck of 500 individuals
        before expanding to 40,000 in the present day. Based on the dreamlands
        Necronomicon (Lovecraft).
    """
    citations = [_carter_et_al]

    populations = [
        stdvoidsim.Population(
            id="TempleCats",
            description="Ulthar Temple Cats -- sacred guardians",
        ),
        stdvoidsim.Population(
            id="MoonExpedition",
            description="Moon Expedition Force -- lunar explorers",
        ),
    ]

    # Parameters
    N_ancestral = 200000
    N_temple = 100000
    N_expedition_modern = 40000
    N_expedition_bottleneck = 500
    T_split = 5000
    T_bottleneck = T_split // 2  # Bottleneck before merge to avoid zero-length epoch

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_temple,
            metadata={
                "name": "TempleCats",
                "description": "Ulthar Temple Cats -- sacred guardians",
            },
        ),
        msprime.PopulationConfiguration(
            initial_size=N_expedition_modern,
            metadata={
                "name": "MoonExpedition",
                "description": "Moon Expedition Force -- lunar explorers",
            },
        ),
    ]

    demographic_events = [
        # Moon Expedition bottleneck before the split
        msprime.PopulationParametersChange(
            time=T_bottleneck, initial_size=N_expedition_bottleneck, population_id=1
        ),
        # Split: Moon Expedition merges back into Temple Cats at T_split
        msprime.MassMigration(time=T_split, source=1, destination=0, proportion=1.0),
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
        generation_time=5,
        mutation_rate=2e-8,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_dreamlands_patrol())
