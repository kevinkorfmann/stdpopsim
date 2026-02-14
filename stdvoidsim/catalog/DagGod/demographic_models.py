"""
Demographic models for Dagonus maximus (Father Dagon).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime

import stdvoidsim

_species = stdvoidsim.get_species("DagGod")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim

_olmstead_et_al = stdvoidsim.Citation(
    author="Olmstead et al.",
    year=1931,
    doi="https://doi.org/10.1666/void.dagon.demog.1",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


# -------------------------------------------------------------------------
# AbyssalSlumber_1O31: Single population three-epoch model
# -------------------------------------------------------------------------


def _abyssal_slumber():
    id = "AbyssalSlumber_1O31"
    description = "Single population three-epoch model of Father Dagon"
    long_description = """
        Single population model of Father Dagon demographic history. Three
        epochs: modern abyssal population with effective population size 50,
        a deep trench awakening beginning 100 generations ago with N=500,
        and a primordial ocean era beginning 1,000 generations ago with
        N=5. Based on the Innsmouth investigations of Olmstead et al. (1931).
    """
    citations = [_olmstead_et_al]

    populations = [
        stdvoidsim.Population(
            id="AbyssalDagons",
            description="Father Dagon and abyssal progenitors",
        ),
    ]

    # Modern abyssal: N=50
    # Deep trench awakening at T=100 gen: N=500
    # Primordial ocean at T=1,000 gen: N=5
    N_modern = 50
    N_awakening = 500
    N_primordial = 5

    T_awakening = 100
    T_primordial = 1000

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_modern,
            metadata={
                "name": "AbyssalDagons",
                "description": "Father Dagon and abyssal progenitors",
            },
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=T_awakening, initial_size=N_awakening, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_primordial, initial_size=N_primordial, population_id=0
        ),
    ]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=50000,
        mutation_rate=5e-11,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_abyssal_slumber())


# -------------------------------------------------------------------------
# DeepOneProgenitor_2O31: Two population model
# -------------------------------------------------------------------------


def _deep_one_progenitor():
    id = "DeepOneProgenitor_2O31"
    description = "Two-population model of Abyssal Progenitors and Reef Manifestations"
    long_description = """
        Two-population model representing Abyssal Progenitors and Reef
        Manifestations of Father Dagon. An ancestral population of size
        500 splits at 200 generations ago. The Abyssal Progenitors
        maintain a size of 50. The Reef Manifestations go through a
        bottleneck of 5 individuals before expanding to 30 in the
        present day. Based on the Innsmouth investigations of Olmstead
        et al. (1931).
    """
    citations = [_olmstead_et_al]

    populations = [
        stdvoidsim.Population(
            id="AbyssalProgenitors",
            description="Abyssal Progenitors -- deep trench dwellers",
        ),
        stdvoidsim.Population(
            id="ReefManifestations",
            description="Reef Manifestations -- shallow water avatars",
        ),
    ]

    # Parameters
    N_ancestral = 500
    N_abyssal = 50
    N_reef_modern = 30
    N_reef_bottleneck = 5
    T_split = 200
    T_bottleneck = T_split // 2  # Bottleneck before merge to avoid zero-length epoch

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_abyssal,
            metadata={
                "name": "AbyssalProgenitors",
                "description": "Abyssal Progenitors -- deep trench dwellers",
            },
        ),
        msprime.PopulationConfiguration(
            initial_size=N_reef_modern,
            metadata={
                "name": "ReefManifestations",
                "description": "Reef Manifestations -- shallow water avatars",
            },
        ),
    ]

    demographic_events = [
        # Reef Manifestations bottleneck before the split
        msprime.PopulationParametersChange(
            time=T_bottleneck, initial_size=N_reef_bottleneck, population_id=1
        ),
        # Split: Reef Manifestations merge back into Abyssal Progenitors at T_split
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
        generation_time=50000,
        mutation_rate=5e-11,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_deep_one_progenitor())
