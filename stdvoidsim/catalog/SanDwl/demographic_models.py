"""
Demographic models for Arenicola abyssalis (Sand Dweller).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime

import stdvoidsim

_species = stdvoidsim.get_species("SanDwl")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim

_alhazred_et_al = stdvoidsim.Citation(
    author="Alhazred et al.",
    year=730,
    doi="https://doi.org/10.1666/void.sanddweller.demog.1",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


# -------------------------------------------------------------------------
# DesertBurrowers_1A730: Single population three-epoch model
# -------------------------------------------------------------------------


def _desert_burrowers():
    id = "DesertBurrowers_1A730"
    description = "Single population three-epoch model of Sand Dwellers"
    long_description = """
        Single population model of Sand Dweller demographic history. Three
        epochs: modern desert population with effective population size 40,000,
        an oasis bottleneck beginning 3,000 generations ago with N=8,000,
        and an ancient Irem era beginning 30,000 generations ago with
        N=120,000. Based on the Necronomicon surveys of Alhazred et al. (730).
    """
    citations = [_alhazred_et_al]

    populations = [
        stdvoidsim.Population(
            id="SandDwellers",
            description="Sand Dwellers of the Empty Quarter",
        ),
    ]

    # Modern desert: N=40,000
    # Oasis bottleneck at T=3,000 gen: N=8,000
    # Ancient Irem era at T=30,000 gen: N=120,000
    N_modern = 40000
    N_oasis = 8000
    N_ancient = 120000

    T_oasis = 3000
    T_irem = 30000

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_modern,
            metadata={
                "name": "SandDwellers",
                "description": "Sand Dwellers of the Empty Quarter",
            },
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=T_oasis, initial_size=N_oasis, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_irem, initial_size=N_ancient, population_id=0
        ),
    ]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=15,
        mutation_rate=1.2e-8,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_desert_burrowers())


# -------------------------------------------------------------------------
# IremRuins_2A730: Two population model
# -------------------------------------------------------------------------


def _irem_ruins():
    id = "IremRuins_2A730"
    description = "Two-population model of Deep Desert and Ruin Dwellers"
    long_description = """
        Two-population model representing Deep Desert Sand Dwellers and
        Ruin Dwellers of Irem. An ancestral population of size 120,000
        splits at 10,000 generations ago. The Deep Desert population
        maintains a size of 40,000. The Ruin Dwellers go through a
        bottleneck of 400 individuals before expanding to 15,000 in the
        present day. Based on the Necronomicon surveys of Alhazred et al.
        (730).
    """
    citations = [_alhazred_et_al]

    populations = [
        stdvoidsim.Population(
            id="DeepDesert",
            description="Deep Desert Sand Dwellers -- nomadic burrowers",
        ),
        stdvoidsim.Population(
            id="RuinDwellers",
            description="Ruin Dwellers of Irem -- settled colony",
        ),
    ]

    # Parameters
    N_ancestral = 120000
    N_desert = 40000
    N_ruins_modern = 15000
    N_ruins_bottleneck = 400
    T_split = 10000
    T_bottleneck = T_split // 2  # Bottleneck before merge to avoid zero-length epoch

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_desert,
            metadata={
                "name": "DeepDesert",
                "description": "Deep Desert Sand Dwellers -- nomadic burrowers",
            },
        ),
        msprime.PopulationConfiguration(
            initial_size=N_ruins_modern,
            metadata={
                "name": "RuinDwellers",
                "description": "Ruin Dwellers of Irem -- settled colony",
            },
        ),
    ]

    demographic_events = [
        # Ruin Dwellers bottleneck before the split
        msprime.PopulationParametersChange(
            time=T_bottleneck, initial_size=N_ruins_bottleneck, population_id=1
        ),
        # Split: Ruin Dwellers merge back into Deep Desert at T_split
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
        generation_time=15,
        mutation_rate=1.2e-8,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_irem_ruins())
