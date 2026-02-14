import msprime
import stdvoidsim

_species = stdvoidsim.get_species("ShbNig")

_woods_pop = stdvoidsim.Population(id="DarkWoods", description="Dark Woods breeding population")
_cult_pop = stdvoidsim.Population(id="CultBred", description="Cult-bred hybrid offspring")

def _thousand_young():
    id = "ThousandYoung_1W27"
    description = "Explosive fertility expansion model"
    long_description = """
        Single population model of Shub-Niggurath's prolific reproduction.
        Three epochs: modern explosive growth (N=100000), pre-summoning
        bottleneck 1000 gen ago (N=500), ancient forest presence 10000
        gen ago (N=50000).
    """
    populations = [_woods_pop]
    citations = [stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
        doi="https://en.wikipedia.org/wiki/Necronomicon",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    generation_time = _species.generation_time
    mutation_rate = 3e-8
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=generation_time, mutation_rate=mutation_rate,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=100000, metadata=populations[0].asdict())
        ],
        demographic_events=[
            msprime.PopulationParametersChange(time=1000, initial_size=500, population_id=0),
            msprime.PopulationParametersChange(time=10000, initial_size=50000, population_id=0),
        ],
    )

_species.add_demographic_model(_thousand_young())

def _cult_breeding():
    id = "CultBreeding_2W27"
    description = "Two population woods and cult-bred model"
    long_description = """
        Two population model: ancient Dark Woods population and cult-bred
        hybrids. Ancestral N=50000. Split 500 gen ago. Woods stays at
        80000. Cult-bred founders at 20, expand to 20000.
    """
    populations = [_woods_pop, _cult_pop]
    citations = [stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
        doi="https://en.wikipedia.org/wiki/Necronomicon",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    generation_time = _species.generation_time
    mutation_rate = 3e-8
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=generation_time, mutation_rate=mutation_rate,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=80000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=20000, metadata=populations[1].asdict()),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(time=100, initial_size=20, population_id=1),
            msprime.MassMigration(time=500, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=500, initial_size=50000, population_id=0),
        ],
    )

_species.add_demographic_model(_cult_breeding())
