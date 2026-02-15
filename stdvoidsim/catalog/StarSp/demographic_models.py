import msprime
import stdvoidsim

_species = stdvoidsim.get_species("StarSp")
_rlyeh_pop = stdvoidsim.Population(
    id="RlyehSpawn", description="Star-Spawn in sunken R'lyeh"
)
_xoth_pop = stdvoidsim.Population(
    id="XothOrigin", description="Star-Spawn from Xoth system"
)


def _sunken_city():
    id = "SunkenCity_1J26"
    description = "Single population R'lyeh entombed star-spawn model"
    long_description = """
        Star-Spawn entombed with Cthulhu in R'lyeh. Three epochs: modern
        dormant (N=10000), pre-sinking golden age 2000 gen ago (N=100000),
        arrival from Xoth 20000 gen ago (N=5000).
    """
    populations = [_rlyeh_pop]
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
        mutation_rate=2e-9,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=10000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2000, initial_size=100000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20000, initial_size=5000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_sunken_city())


def _xoth_migration():
    id = "XothMigration_2J26"
    description = "Two population Xoth origin and R'lyeh colony model"
    long_description = """
        Two populations: Xoth (origin star) and R'lyeh colony. Ancestral
        N=100000 at Xoth. Split 20000 gen ago. Xoth stable at 80000.
        R'lyeh bottleneck to 1000, expand to 10000.
    """
    populations = [_xoth_pop, _rlyeh_pop]
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
        mutation_rate=2e-9,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=80000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=10000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=5000, initial_size=1000, population_id=1
            ),
            msprime.MassMigration(time=20000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=20000, initial_size=100000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_xoth_migration())
