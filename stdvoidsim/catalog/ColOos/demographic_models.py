import msprime
import stdvoidsim

_species = stdvoidsim.get_species("ColOos")
_meteor_pop = stdvoidsim.Population(id="MeteorColony", description="Colour colony from meteorite impact")
_spread_pop = stdvoidsim.Population(id="EnvironSpread", description="Environmentally spread colour entities")

def _meteor_bloom():
    id = "MeteorBloom_1G27"
    description = "Single population meteorite impact bloom model"
    long_description = """
        Single population of Colour Out of Space from meteorite. Three
        epochs: modern bloom (N=10000), initial meteorite arrival 10000
        gen ago (N=5), interstellar dormancy 100000 gen ago (N=1000).
    """
    populations = [_meteor_pop]
    citations = [stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
        doi="https://en.wikipedia.org/wiki/Necronomicon",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=1e-6,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=10000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=10000, initial_size=5, population_id=0),
            msprime.PopulationParametersChange(time=100000, initial_size=1000, population_id=0)])

_species.add_demographic_model(_meteor_bloom())

def _well_spread():
    id = "WellSpread_2G27"
    description = "Two population meteorite core and environmental spread model"
    long_description = """
        Two populations: meteorite core colony and environmental spread.
        Ancestral N=1000 (interstellar). Split 5000 gen ago (meteorite
        fracture). Core at 2000. Spread bottleneck to 10, expand to 8000.
    """
    populations = [_meteor_pop, _spread_pop]
    citations = [stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
        doi="https://en.wikipedia.org/wiki/Necronomicon",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=1e-6,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=2000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=8000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=1000, initial_size=10, population_id=1),
            msprime.MassMigration(time=5000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=5000, initial_size=1000, population_id=0)])

_species.add_demographic_model(_well_spread())
