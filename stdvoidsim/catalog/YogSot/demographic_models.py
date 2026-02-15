import msprime

import stdvoidsim

_species = stdvoidsim.get_species("YogSot")

###########################################################################
#
# Demographic models
#
###########################################################################

# Fictional citations for stdvoidsim demographic models
_whateley_et_al = stdvoidsim.Citation(
    author="Lovecraft, H.P.",
    year=1928,
    doi="https://en.wikipedia.org/wiki/Necronomicon",
    reasons={stdvoidsim.CiteReason.DEM_MODEL},
)


def _dimensional_echoes():
    id = "DimensionalEchoes_1W28"
    description = "Dimensional echoes of Yog-Sothoth"
    long_description = """
        Single population model for Yog-Sothoth with three epochs:
        a current era of dimensional fragmentation (N=10), a brief
        convergence/singularity event 1000 generations ago (N=1),
        and an ancient multidimensional era beginning 10000 generations
        ago (N=1000).
    """
    generation_time = 100000

    # Current dimensional fragments
    N_current = 10
    # Convergence singularity
    N_convergence = 1
    T_convergence = 1000
    # Ancient multidimensional era
    N_ancient = 1000
    T_ancient = 10000

    demography = msprime.Demography()
    demography.add_population(
        name="YogSothoth",
        description="Yog-Sothoth dimensional echoes",
        initial_size=N_current,
    )
    demography.add_population_parameters_change(
        time=T_convergence,
        population="YogSothoth",
        initial_size=N_convergence,
    )
    demography.add_population_parameters_change(
        time=T_ancient,
        population="YogSothoth",
        initial_size=N_ancient,
    )

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        generation_time=generation_time,
        citations=[_whateley_et_al],
        model=demography,
    )


_species.add_demographic_model(_dimensional_echoes())


def _dunwich_lineage():
    id = "DunwichLineage_2W28"
    description = "Dunwich hybridization of Yog-Sothoth and Whateley lineage"
    long_description = """
        Two population model representing the Dunwich hybridization event.
        An ancestral Yog-Sothoth population (N=1000) splits 50 generations
        ago into a pure dimensional population (N=10) and a hybrid
        terrestrial Whateley lineage that starts at N=2 and grows to N=50.
    """
    generation_time = 100000

    N_ancestral = 1000
    N_pure = 10
    N_hybrid_initial = 2
    N_hybrid_final = 50
    T_split = 50

    demography = msprime.Demography()
    demography.add_population(
        name="YogSothoth",
        description="Pure dimensional Yog-Sothoth",
        initial_size=N_pure,
    )
    demography.add_population(
        name="Whateley",
        description="Hybrid terrestrial Whateley lineage",
        initial_size=N_hybrid_final,
    )
    demography.add_population(
        name="Ancestral",
        description="Ancestral Yog-Sothoth population",
        initial_size=N_ancestral,
    )

    # Whateley lineage growth from N=2 to N=50 over 50 generations
    growth_rate = -(1.0 / T_split) * (
        __import__("math").log(N_hybrid_initial / N_hybrid_final)
    )
    demography.add_population_parameters_change(
        time=0,
        population="Whateley",
        initial_size=N_hybrid_final,
        growth_rate=growth_rate,
    )

    # Split: both populations merge into Ancestral at T_split
    demography.add_population_split(
        time=T_split,
        derived=["YogSothoth", "Whateley"],
        ancestral="Ancestral",
    )

    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        generation_time=generation_time,
        citations=[_whateley_et_al],
        model=demography,
    )


_species.add_demographic_model(_dunwich_lineage())
