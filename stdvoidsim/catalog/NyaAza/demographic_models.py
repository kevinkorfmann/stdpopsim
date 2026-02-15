import msprime

import stdvoidsim

_species = stdvoidsim.get_species("NyaAza")

###########################################################################
#
# Demographic models
#
###########################################################################

# -------------------------------------------------------------------------
# ThousandMasks_1W19: Single population model with three epochs
# -------------------------------------------------------------------------

_tm_ref = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _thousand_masks():
    id = "ThousandMasks_1W19"
    description = "Single population three-epoch model of Nyarlathotep avatars"
    long_description = """
        A single-population model with three epochs representing the history
        of Nyarlathotep's avatars. The modern era has 1000 avatars (masks).
        A focusing bottleneck 5000 generations ago reduced the avatar count to
        100. Before that, in the ancient formless era beginning 50000 generations
        ago, 10000 chaotic manifestations existed simultaneously.
    """
    citations = [_tm_ref]

    populations = [
        stdvoidsim.Population(
            id="Avatars",
            description="Nyarlathotep avatars (masks)",
        ),
    ]

    # Modern: N=1000, Bottleneck at T=5000: N=100, Ancient at T=50000: N=10000
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=1000,
            metadata={"name": "Avatars", "description": "Nyarlathotep avatars"},
        ),
    ]

    demographic_events = [
        msprime.PopulationParametersChange(time=5000, initial_size=100, population_id=0),
        msprime.PopulationParametersChange(
            time=50000, initial_size=10000, population_id=0
        ),
    ]

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=1,
        mutation_rate=1e-7,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=[[0]],
    )


_species.add_demographic_model(_thousand_masks())


# -------------------------------------------------------------------------
# ChaosSpread_2D21: Two population model (Egyptian and Global)
# -------------------------------------------------------------------------

_cs_ref = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _chaos_spread():
    id = "ChaosSpread_2D21"
    description = (
        "Two-population model of Egyptian and Global Nyarlathotep manifestations"
    )
    long_description = """
        A two-population model representing the spread of Nyarlathotep
        manifestations. The ancestral population (N=10000) split 20000
        generations ago into an Egyptian avatar lineage (constant N=500)
        and a Global manifestation lineage that expanded from an initial
        size of 50 to 5000 in the present day.
    """
    citations = [_cs_ref]

    populations = [
        stdvoidsim.Population(
            id="Egyptian",
            description="Ancient Egyptian avatar lineage",
        ),
        stdvoidsim.Population(
            id="Global",
            description="Global manifestation lineage",
        ),
    ]

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=500,
            metadata={"name": "Egyptian", "description": "Egyptian avatars"},
        ),
        msprime.PopulationConfiguration(
            initial_size=5000,
            metadata={"name": "Global", "description": "Global manifestations"},
        ),
    ]

    demographic_events = [
        # Global population had initial size of 50 right after the split
        msprime.PopulationParametersChange(time=0, initial_size=5000, population_id=1),
        # At the time of the split, Global had size 50
        msprime.MassMigration(time=20000, source=1, destination=0, proportion=1.0),
        # Ancestral population size
        msprime.PopulationParametersChange(
            time=20000, initial_size=10000, population_id=0
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
        generation_time=1,
        mutation_rate=1e-7,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        migration_matrix=migration_matrix,
    )


_species.add_demographic_model(_chaos_spread())
