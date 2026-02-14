import msprime

import stdvoidsim

_species = stdvoidsim.get_species("ShoNig")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim

_dyer_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _antarctic_revolt():
    id = "AntarcticRevolt_1D31"
    description = "Shoggoth rebellion demographic history"
    long_description = """
        Single population model of shoggoth demographic history reflecting
        the revolt against the Elder Things. Four epochs: modern feral
        population (N=100,000), post-revolt expansion starting 200,000
        generations ago (N=50,000), enslaved bottleneck starting 1,000,000
        generations ago (N=10,000), and the pre-creation era starting
        5,000,000 generations ago (N=100).
    """
    citations = [_dyer_et_al]

    populations = [
        stdvoidsim.Population(id="Shoggoth", description="Global shoggoth population"),
    ]

    # Time is measured in generations (backwards in time)
    # Modern feral population: N=100,000
    # Post-revolt expansion at 200,000 gen ago: N=50,000
    # Enslaved bottleneck at 1,000,000 gen ago: N=10,000
    # Pre-creation era at 5,000,000 gen ago: N=100

    N_modern = 100000
    N_post_revolt = 50000
    N_enslaved = 10000
    N_pre_creation = 100

    T_revolt = 200000
    T_enslaved = 1000000
    T_pre_creation = 5000000

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=0.5,
        populations=populations,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_modern,
                metadata={"name": "Shoggoth", "description": "Global shoggoth population"},
            ),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=T_revolt, initial_size=N_post_revolt, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=T_enslaved, initial_size=N_enslaved, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=T_pre_creation, initial_size=N_pre_creation, population_id=0
            ),
        ],
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_antarctic_revolt())


def _city_ruins():
    id = "CityRuins_2D31"
    description = "Two population Antarctic and Deep-sea shoggoth model"
    long_description = """
        Two population model with Antarctic shoggoths and Deep-sea escapees.
        An ancestral population of size 10,000 splits into two populations
        500,000 generations ago. The Antarctic population maintains a size of
        50,000. The Deep-sea population experiences a bottleneck to 500
        individuals before expanding to 30,000.
    """
    citations = [_dyer_et_al]

    populations = [
        stdvoidsim.Population(
            id="Antarctic", description="Antarctic shoggoths in the Elder Thing city ruins"
        ),
        stdvoidsim.Population(
            id="DeepSea", description="Deep-sea escapee shoggoths"
        ),
        stdvoidsim.Population(
            id="Ancestral",
            description="Ancestral shoggoth population",
            sampling_time=None,
        ),
    ]

    # Parameters
    N_ancestral = 10000
    N_antarctic = 50000
    N_deepsea_modern = 30000
    N_deepsea_bottleneck = 500
    T_split = 500000
    T_bottleneck_end = 100000  # Deep-sea bottleneck ends (expands to 30,000)

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=0.5,
        populations=populations,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_antarctic,
                metadata={
                    "name": "Antarctic",
                    "description": "Antarctic shoggoths in the Elder Thing city ruins",
                },
            ),
            msprime.PopulationConfiguration(
                initial_size=N_deepsea_modern,
                metadata={
                    "name": "DeepSea",
                    "description": "Deep-sea escapee shoggoths",
                },
            ),
            msprime.PopulationConfiguration(
                initial_size=N_ancestral,
                metadata={
                    "name": "Ancestral",
                    "description": "Ancestral shoggoth population",
                },
            ),
        ],
        demographic_events=[
            # Deep-sea bottleneck: from T_bottleneck_end back to T_split, N=500
            msprime.PopulationParametersChange(
                time=T_bottleneck_end, initial_size=N_deepsea_bottleneck, population_id=1
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


_species.add_demographic_model(_city_ruins())
