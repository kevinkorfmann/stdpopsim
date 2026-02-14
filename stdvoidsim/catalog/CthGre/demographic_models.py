"""
Demographic models for Cthulhu greatoldone (Great Cthulhu).
Part of the stdvoidsim project -- a fictional species catalog.
"""

import msprime
import stdvoidsim

_species = stdvoidsim.get_species("CthGre")

###########################################################################
#
# Demographic models
#
###########################################################################


def _deep_slumber():
    id = "DeepSlumber_1R28"
    description = "Cyclic dormancy model for Great Cthulhu in R'lyeh"
    long_description = """
        Single population model of Cthulhu's cyclic dormancy in the sunken
        city of R'lyeh. Three epochs: (1) a modern awake phase with effective
        population size 500, (2) a dormant phase bottleneck beginning 50000
        generations ago with N=50, and (3) an ancient pre-slumber era beginning
        500000 generations ago with N=5000. Based on the psychic archaeology
        of the Necronomicon (Lovecraft).
    """
    populations = [
        stdvoidsim.Population(
            id="Rlyeh",
            description="R'lyeh deep ones -- Cthulhu and kin",
        ),
    ]

    citations = [
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Modern awake phase: N=500
    # Dormant bottleneck at T=50000 gen: N=50
    # Ancient pre-slumber at T=500000 gen: N=5000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=500,
            metadata=populations[0].asdict(),
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=50000,
            initial_size=50,
            population_id=0,
        ),
        msprime.PopulationParametersChange(
            time=500000,
            initial_size=5000,
            population_id=0,
        ),
    ]

    migration_matrix = [[0]]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=10000,
        mutation_rate=1e-10,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_deep_slumber())


def _rlyeh_rising():
    id = "RlyehRising_2P20"
    description = "Two population model of R'lyeh deep ones and Pacific surface cultists"
    long_description = """
        Two population model describing the divergence of the R'lyeh deep ones
        (oceanic Cthulhu-spawn) and Pacific surface cultists (terrestrial hybrid
        descendants). The ancestral population of size 5000 splits at 100000
        generations ago. The R'lyeh population maintains a size of 500. The
        surface cultist lineage goes through a bottleneck of 100 individuals
        before expanding to 2000. Based on the Necronomicon (Lovecraft).
        
    """
    populations = [
        stdvoidsim.Population(
            id="Rlyeh",
            description="R'lyeh deep ones -- oceanic Cthulhu-spawn",
        ),
        stdvoidsim.Population(
            id="PacificCultists",
            description="Pacific surface cultists -- terrestrial hybrid descendants",
        ),
    ]

    citations = [
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        ),
    ]

    # Present day: Rlyeh N=500, PacificCultists N=2000
    # At T=10000 gen ago: PacificCultists bottleneck N=100
    # At T=100000 gen ago: populations merge into ancestral pop N=5000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=500,
            metadata=populations[0].asdict(),
        ),
        msprime.PopulationConfiguration(
            initial_size=2000,
            metadata=populations[1].asdict(),
        ),
    ]

    demographic_events = [
        # Pacific cultist bottleneck at 10000 generations ago
        msprime.PopulationParametersChange(
            time=10000,
            initial_size=100,
            population_id=1,
        ),
        # At 100000 generations ago, the two populations merge
        # (PacificCultists merge into Rlyeh going backwards in time)
        msprime.MassMigration(
            time=100000,
            source=1,
            destination=0,
            proportion=1.0,
        ),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=100000,
            initial_size=5000,
            population_id=0,
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
        mutation_rate=1e-10,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )


_species.add_demographic_model(_rlyeh_rising())
