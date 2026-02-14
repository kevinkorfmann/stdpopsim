import msprime
import stdpopsim

_species = stdpopsim.get_species("AzaPri")

_nucleus_pop = stdpopsim.Population(
    id="Nucleus", description="The nuclear chaos at the center of infinity"
)
_fragment_pop = stdpopsim.Population(
    id="Fragment", description="Fragmentary emanations cast into the void"
)

def _nuclear_pulsation():
    id = "NuclearPulsation_1S22"
    description = "Pulsating single population model of Azathoth"
    long_description = """
        A single population model representing the pulsating nuclear chaos
        of Azathoth at the center of ultimate chaos. The entity periodically
        fragments and reconverges. Three epochs: current singularity (N=1),
        brief fragmentation 10 generations ago (N=100), ancient unified
        chaos 100 generations ago (N=1).
    """
    populations = [_nucleus_pop]
    citations = [
        stdpopsim.Citation(
            author="The Daemon Sultan Cult",
            year=1922,
            doi="https://doi.org/10.1666/void.azathoth.dem1",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        )
    ]
    generation_time = _species.generation_time
    mutation_rate = 1e-11

    N_current = 1
    N_fragment = 100
    N_ancient = 1
    t_fragment = 10
    t_ancient = 100

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        mutation_rate=mutation_rate,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_current, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=t_fragment, initial_size=N_fragment, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=t_ancient, initial_size=N_ancient, population_id=0
            ),
        ],
    )

_species.add_demographic_model(_nuclear_pulsation())

def _void_emanation():
    id = "VoidEmanation_2S22"
    description = "Two population model of Azathoth nucleus and void fragments"
    long_description = """
        Two population model: the central nuclear chaos and fragmentary
        emanations cast into the void. Ancestral unified chaos N=100.
        Split at 50 generations ago. Nucleus contracts to N=1.
        Fragments expand to N=50.
    """
    populations = [_nucleus_pop, _fragment_pop]
    citations = [
        stdpopsim.Citation(
            author="The Daemon Sultan Cult",
            year=1922,
            doi="https://doi.org/10.1666/void.azathoth.dem2",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        )
    ]
    generation_time = _species.generation_time
    mutation_rate = 1e-11

    N_anc = 100
    N_nucleus = 1
    N_fragments = 50
    t_split = 50

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        mutation_rate=mutation_rate,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_nucleus, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=N_fragments, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(
                time=t_split, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=t_split, initial_size=N_anc, population_id=0
            ),
        ],
    )

_species.add_demographic_model(_void_emanation())
