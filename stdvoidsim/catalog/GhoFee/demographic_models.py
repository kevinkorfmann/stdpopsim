import msprime

import stdvoidsim

_species = stdvoidsim.get_species("GhoFee")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim

_pickman_et_al = stdvoidsim.Citation(
    author="Pickman et al.",
    year=1926,
    doi="https://doi.org/10.1000/void.ghoul.1926",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _subterranean_isolation():
    id = "SubterraneanIsolation_1P26"
    description = "Single population ghoul demographic history"
    long_description = """
        Single population model of ghoul demographic history reflecting
        their transformation from humans into subterranean necrophages.
        Three epochs: modern warrens (N=30,000), initial transformation
        bottleneck starting 2,000 generations ago (N=500), and the ancient
        proto-ghoul human population starting 5,000 generations ago
        (N=100,000).
    """
    citations = [_pickman_et_al]

    populations = [
        stdvoidsim.Population(id="Ghouls", description="Global ghoul population"),
    ]

    # Time is measured in generations (backwards in time)
    # Modern warrens: N=30,000
    # Transformation bottleneck at 2,000 gen ago: N=500
    # Ancient proto-ghoul human population at 5,000 gen ago: N=100,000

    N_modern = 30000
    N_bottleneck = 500
    N_ancient = 100000

    T_bottleneck = 2000
    T_ancient = 5000

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=20,
        populations=populations,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_modern,
                metadata={"name": "Ghouls", "description": "Global ghoul population"},
            ),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=T_bottleneck, initial_size=N_bottleneck, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=T_ancient, initial_size=N_ancient, population_id=0
            ),
        ],
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_subterranean_isolation())


def _dreamlands_passage():
    id = "DreamlandsPassage_2P26"
    description = "Two population Waking World and Dreamlands ghoul model"
    long_description = """
        Two population model with Waking World ghouls (underground cities)
        and Dreamlands ghouls (separate dimension). An ancestral population
        of size 100,000 splits into two populations 1,000 generations ago.
        The Waking World population maintains a size of 30,000. The
        Dreamlands population experiences a bottleneck to 200 individuals
        before expanding to 20,000.
    """
    citations = [_pickman_et_al]

    populations = [
        stdvoidsim.Population(
            id="WakingWorld",
            description="Waking World ghouls in underground cities",
        ),
        stdvoidsim.Population(
            id="Dreamlands",
            description="Dreamlands ghouls in a separate dimension",
        ),
        stdvoidsim.Population(
            id="Ancestral",
            description="Ancestral ghoul population",
            sampling_time=None,
        ),
    ]

    # Parameters
    N_ancestral = 100000
    N_waking = 30000
    N_dreamlands_modern = 20000
    N_dreamlands_bottleneck = 200
    T_split = 1000
    T_bottleneck_end = 500  # Dreamlands bottleneck ends (expands to 20,000)

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=20,
        populations=populations,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_waking,
                metadata={
                    "name": "WakingWorld",
                    "description": "Waking World ghouls in underground cities",
                },
            ),
            msprime.PopulationConfiguration(
                initial_size=N_dreamlands_modern,
                metadata={
                    "name": "Dreamlands",
                    "description": "Dreamlands ghouls in a separate dimension",
                },
            ),
            msprime.PopulationConfiguration(
                initial_size=N_ancestral,
                metadata={
                    "name": "Ancestral",
                    "description": "Ancestral ghoul population",
                },
            ),
        ],
        demographic_events=[
            # Dreamlands bottleneck: from T_bottleneck_end back to T_split, N=200
            msprime.PopulationParametersChange(
                time=T_bottleneck_end,
                initial_size=N_dreamlands_bottleneck,
                population_id=1,
            ),
            # Split: both populations merge into ancestral at T_split
            msprime.MassMigration(
                time=T_split, source=0, destination=2, proportion=1.0
            ),
            msprime.MassMigration(
                time=T_split, source=1, destination=2, proportion=1.0
            ),
        ],
        migration_matrix=[
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
    )


_species.add_demographic_model(_dreamlands_passage())
