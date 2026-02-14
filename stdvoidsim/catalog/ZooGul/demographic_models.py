import msprime
import stdvoidsim

_species = stdvoidsim.get_species("ZooGul")
_enchanted_pop = stdvoidsim.Population(id="EnchantedWood", description="Zoogs of the Enchanted Wood")
_upper_pop = stdvoidsim.Population(id="UpperDreamlands", description="Upper Dreamlands zoog colony")

def _enchanted_wood():
    id = "EnchantedWood_1C26"
    description = "Single population Enchanted Wood zoog model"
    long_description = """
        Single population in Enchanted Wood. Three epochs: modern
        thriving (N=500000), cat-war bottleneck 10000 gen ago (N=50000),
        ancient forest founding 100000 gen ago (N=200000).
    """
    populations = [_enchanted_pop]
    citations = [stdvoidsim.Citation(author="Carter et al.", year=1926,
        doi="https://doi.org/10.1666/void.zoog.dem1",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=2.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=500000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=10000, initial_size=50000, population_id=0),
            msprime.PopulationParametersChange(time=100000, initial_size=200000, population_id=0)])

_species.add_demographic_model(_enchanted_wood())

def _dreamlands_spread():
    id = "DreamlandsSpread_2C26"
    description = "Two population Enchanted Wood and upper Dreamlands model"
    long_description = """
        Two populations: Enchanted Wood core and upper Dreamlands colony.
        Ancestral N=200000. Split 30000 gen ago. Wood at 500000. Upper
        bottleneck to 1000, grow to 100000.
    """
    populations = [_enchanted_pop, _upper_pop]
    citations = [stdvoidsim.Citation(author="Carter et al.", year=1926,
        doi="https://doi.org/10.1666/void.zoog.dem2",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=2.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=500000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=100000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=5000, initial_size=1000, population_id=1),
            msprime.MassMigration(time=30000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=30000, initial_size=200000, population_id=0)])

_species.add_demographic_model(_dreamlands_spread())
