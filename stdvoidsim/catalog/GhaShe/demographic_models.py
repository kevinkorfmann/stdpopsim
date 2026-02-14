import msprime
import stdvoidsim

_species = stdvoidsim.get_species("GhaShe")
_bone_pop = stdvoidsim.Population(id="BoneValley", description="Ghasts in the Vale of Pnath")
_upper_pop = stdvoidsim.Population(id="UpperCaves", description="Upper cave ghast colony")

def _vale_of_pnath():
    id = "ValeOfPnath_1C26"
    description = "Single population Vale of Pnath ghast model"
    long_description = """
        Single population in the Vale of Pnath. Three epochs: modern
        scavengers (N=80000), feast-famine cycle 5000 gen ago (N=20000),
        ancient cave colonization 50000 gen ago (N=150000).
    """
    populations = [_bone_pop]
    citations = [stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
        doi="https://en.wikipedia.org/wiki/Necronomicon",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=80000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=5000, initial_size=20000, population_id=0),
            msprime.PopulationParametersChange(time=50000, initial_size=150000, population_id=0)])

_species.add_demographic_model(_vale_of_pnath())

def _upper_caves():
    id = "UpperCaves_2C26"
    description = "Two population Pnath and upper cave model"
    long_description = """
        Two populations: Vale of Pnath and upper caves. Ancestral N=150000.
        Split 15000 gen ago. Pnath at 80000. Upper caves bottleneck to
        2000, grow to 30000.
    """
    populations = [_bone_pop, _upper_pop]
    citations = [stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
        doi="https://en.wikipedia.org/wiki/Necronomicon",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=80000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=30000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=3000, initial_size=2000, population_id=1),
            msprime.MassMigration(time=15000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=15000, initial_size=150000, population_id=0)])

_species.add_demographic_model(_upper_caves())
