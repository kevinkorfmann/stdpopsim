import msprime
import stdvoidsim

_species = stdvoidsim.get_species("HouFir")
_angular_pop = stdvoidsim.Population(
    id="AngularRealm", description="Hounds dwelling in angular time"
)
_corner_pop = stdvoidsim.Population(
    id="CornerHunters", description="Hounds that emerged through corners"
)


def _angular_time():
    id = "AngularTime_1L29"
    description = "Single population angular time predator model"
    long_description = """
        Single population of Hounds existing in angular time. Three epochs:
        modern scattered hunters (N=5000), temporal convergence 500 gen ago
        (N=20000), primordial angular existence 5000 gen ago (N=1000).
    """
    populations = [_angular_pop]
    citations = [
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        )
    ]
    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=3e-9,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=5000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=500, initial_size=20000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=5000, initial_size=1000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_angular_time())


def _corner_emergence():
    id = "CornerEmergence_2L29"
    description = "Two population angular realm and corner hunters model"
    long_description = """
        Two populations: angular realm dwellers and corner-emerged hunters.
        Ancestral N=20000. Split 1000 gen ago. Angular realm at 5000.
        Corner hunters bottleneck to 100, expand to 3000.
    """
    populations = [_angular_pop, _corner_pop]
    citations = [
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        )
    ]
    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=3e-9,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=5000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=200, initial_size=100, population_id=1
            ),
            msprime.MassMigration(time=1000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=1000, initial_size=20000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_corner_emergence())
