import msprime

import stdvoidsim

_species = stdvoidsim.get_species("DagHyd")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim

_marsh_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


# -------------------------------------------------------------------------
# InnsmouthDecline_1M27: Single population three-epoch model
# -------------------------------------------------------------------------


def _innsmouth_decline():
    id = "InnsmouthDecline_1M27"
    description = "Single population three-epoch Deep One demographic model"
    long_description = """
        Single population model of Deep One demographic history. Three epochs:
        modern reduced population after the 1928 Innsmouth raid (N=50,000),
        a pre-raid golden age beginning 100 generations ago (N=200,000),
        and the founding of the underwater city Y'ha-nthlei 5,000 generations
        ago (N=10,000).
    """
    citations = [_marsh_et_al]

    populations = [
        stdvoidsim.Population(
            id="DeepOnes",
            description="Deep One population of Y'ha-nthlei",
        ),
    ]

    # Modern post-raid: N=50,000
    # Pre-raid golden age at T=100 gen: N=200,000
    # Founding of Y'ha-nthlei at T=5,000 gen: N=10,000
    N_modern = 50000
    N_golden_age = 200000
    N_founding = 10000

    T_raid = 100
    T_founding = 5000

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_modern,
            metadata={
                "name": "DeepOnes",
                "description": "Deep One population of Y'ha-nthlei",
            },
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(
            time=T_raid, initial_size=N_golden_age, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_founding, initial_size=N_founding, population_id=0
        ),
    ]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=100,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=[[0]],
        mutation_rate=3e-8,
        recombination_rate=1.5e-8,
    )


_species.add_demographic_model(_innsmouth_decline())


# -------------------------------------------------------------------------
# HybridIntrogression_2M27: Two population model (Deep Ones and Hybrids)
# -------------------------------------------------------------------------


def _hybrid_introgression():
    id = "HybridIntrogression_2M27"
    description = "Two-population model of Deep Ones and Innsmouth Hybrids"
    long_description = """
        Two-population model representing pure oceanic Deep Ones and
        coastal/terrestrial Innsmouth Hybrids. An ancestral Deep One
        population of size 200,000 gives rise to the Hybrid population
        30 generations ago via a founder event (initial size 50). The
        Hybrid population expands to 5,000 in the present day. The Deep
        One population declines from 200,000 to 50,000 at the time of
        the Innsmouth raid 3 generations ago.
    """
    citations = [_marsh_et_al]

    populations = [
        stdvoidsim.Population(
            id="DeepOnes",
            description="Pure oceanic Deep Ones",
        ),
        stdvoidsim.Population(
            id="Hybrids",
            description="Innsmouth human-Deep One hybrids",
        ),
    ]

    # Parameters
    N_ancestral = 200000
    N_deep_ones_modern = 50000
    N_hybrids_modern = 5000
    N_hybrids_founder = 50
    T_split = 30
    T_raid = 3

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_deep_ones_modern,
            metadata={
                "name": "DeepOnes",
                "description": "Pure oceanic Deep Ones",
            },
        ),
        msprime.PopulationConfiguration(
            initial_size=N_hybrids_modern,
            metadata={
                "name": "Hybrids",
                "description": "Innsmouth human-Deep One hybrids",
            },
        ),
    ]

    demographic_events = [
        # Innsmouth raid: Deep Ones decline from 200,000 to 50,000
        msprime.PopulationParametersChange(
            time=T_raid, initial_size=N_ancestral, population_id=0
        ),
        # Hybrid founder bottleneck right after the split
        msprime.PopulationParametersChange(
            time=T_raid, initial_size=N_hybrids_founder, population_id=1
        ),
        # Split: Hybrids merge back into Deep Ones at T_split
        msprime.MassMigration(
            time=T_split, source=1, destination=0, proportion=1.0
        ),
        # Ancestral Deep One population size
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
        generation_time=100,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_hybrid_introgression())
