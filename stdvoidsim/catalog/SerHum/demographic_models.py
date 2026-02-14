import msprime
import stdvoidsim

_species = stdvoidsim.get_species("SerHum")
_valusia_pop = stdvoidsim.Population(id="Valusia", description="Ancient Valusian serpent empire")
_infiltrator_pop = stdvoidsim.Population(id="Infiltrators", description="Human-disguised infiltrators")

def _valusian_empire():
    id = "ValusianEmpire_1K29"
    description = "Single population Valusian empire decline model"
    long_description = """
        Single population of serpent people. Three epochs: modern hidden
        remnants (N=40000), post-Kull persecution 2000 gen ago (N=5000),
        golden Valusian empire 20000 gen ago (N=500000).
    """
    populations = [_valusia_pop]
    citations = [stdvoidsim.Citation(author="Kull et al.", year=1929,
        doi="https://doi.org/10.1666/void.serpent.dem1",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=1e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=40000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=2000, initial_size=5000, population_id=0),
            msprime.PopulationParametersChange(time=20000, initial_size=500000, population_id=0)])

_species.add_demographic_model(_valusian_empire())

def _infiltration():
    id = "Infiltration_2K29"
    description = "Two population Valusian and infiltrator model"
    long_description = """
        Two populations: underground Valusians and human-disguised infiltrators.
        Ancestral N=500000. Split 5000 gen ago. Underground at 30000.
        Infiltrators bottleneck to 100, grow to 10000.
    """
    populations = [_valusia_pop, _infiltrator_pop]
    citations = [stdvoidsim.Citation(author="Kull et al.", year=1929,
        doi="https://doi.org/10.1666/void.serpent.dem2",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=1e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=30000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=10000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=1000, initial_size=100, population_id=1),
            msprime.MassMigration(time=5000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=5000, initial_size=500000, population_id=0)])

_species.add_demographic_model(_infiltration())
