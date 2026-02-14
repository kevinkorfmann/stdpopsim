import msprime

import stdvoidsim

_species = stdvoidsim.get_species("BybWor")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim

_demarigny_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _void_swarm():
    id = "VoidSwarm_1M33"
    description = "Byakhee single population void transit history"
    long_description = """
        Single population model of Byakhee demographic history reflecting
        interstellar transit bottlenecks. Three epochs: modern swarm
        (N=200,000), void bottleneck from interstellar transit starting
        10,000 generations ago (N=5,000), and the Aldebaran homeworld era
        starting 100,000 generations ago (N=2,000,000).
    """
    citations = [_demarigny_et_al]

    populations = [
        stdvoidsim.Population(id="Byakhee", description="Global Byakhee swarm"),
    ]

    # Time is measured in generations (backwards in time)
    # Modern swarm: N=200,000
    # Void bottleneck at 10,000 gen ago: N=5,000
    # Aldebaran homeworld at 100,000 gen ago: N=2,000,000

    N_modern = 200000
    N_bottleneck = 5000
    N_homeworld = 2000000

    T_bottleneck = 10000
    T_homeworld = 100000

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=10,
        populations=populations,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_modern,
                metadata={"name": "Byakhee", "description": "Global Byakhee swarm"},
            ),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=T_bottleneck, initial_size=N_bottleneck, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=T_homeworld, initial_size=N_homeworld, population_id=0
            ),
        ],
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_void_swarm())


def _star_system_split():
    id = "StarSystemSplit_2M33"
    description = "Two population Aldebaran and Hyades cluster Byakhee model"
    long_description = """
        Two population model with Aldebaran homeworld swarm and Hyades cluster
        colony. An ancestral population of size 2,000,000 splits into two
        populations 50,000 generations ago. The Aldebaran population stabilizes
        at 1,000,000. The Hyades colony experiences a bottleneck to 500
        individuals before expanding to 200,000.
    """
    citations = [_demarigny_et_al]

    populations = [
        stdvoidsim.Population(
            id="Aldebaran", description="Aldebaran homeworld Byakhee swarm"
        ),
        stdvoidsim.Population(
            id="Hyades", description="Hyades cluster colony Byakhee"
        ),
        stdvoidsim.Population(
            id="Ancestral",
            description="Ancestral Byakhee population",
            sampling_time=None,
        ),
    ]

    # Parameters
    N_ancestral = 2000000
    N_aldebaran = 1000000
    N_hyades_modern = 200000
    N_hyades_bottleneck = 500
    T_split = 50000
    T_bottleneck_end = 10000  # Hyades bottleneck ends (expands to 200,000)

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=10,
        populations=populations,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_aldebaran,
                metadata={
                    "name": "Aldebaran",
                    "description": "Aldebaran homeworld Byakhee swarm",
                },
            ),
            msprime.PopulationConfiguration(
                initial_size=N_hyades_modern,
                metadata={
                    "name": "Hyades",
                    "description": "Hyades cluster colony Byakhee",
                },
            ),
            msprime.PopulationConfiguration(
                initial_size=N_ancestral,
                metadata={
                    "name": "Ancestral",
                    "description": "Ancestral Byakhee population",
                },
            ),
        ],
        demographic_events=[
            # Hyades bottleneck: from T_bottleneck_end back to T_split, N=500
            msprime.PopulationParametersChange(
                time=T_bottleneck_end, initial_size=N_hyades_bottleneck, population_id=1
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


_species.add_demographic_model(_star_system_split())
