import msprime
import stdvoidsim

_species = stdvoidsim.get_species("FlyPol")
_basalt_pop = stdvoidsim.Population(id="BasaltCities", description="Flying polyps in basalt tower cities")
_surface_pop = stdvoidsim.Population(id="SurfaceRaids", description="Surface-raiding polyp splinter group")

def _yithian_war():
    id = "YithianWar_1P35"
    description = "Single population post-Yithian war model"
    long_description = """
        Single population after the war with the Great Race of Yith.
        Three epochs: modern imprisoned remnant (N=20000), post-war
        bottleneck 2000 gen ago (N=1000), pre-war dominance 10000 gen
        ago (N=500000).
    """
    populations = [_basalt_pop]
    citations = [stdvoidsim.Citation(author="Peaslee et al.", year=1935,
        doi="https://doi.org/10.1666/void.polyp.dem1",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=6e-9,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=20000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=2000, initial_size=1000, population_id=0),
            msprime.PopulationParametersChange(time=10000, initial_size=500000, population_id=0)])

_species.add_demographic_model(_yithian_war())

def _surface_raid():
    id = "SurfaceRaid_2P35"
    description = "Two population basalt cities and surface raiders model"
    long_description = """
        Two populations: imprisoned basalt city dwellers and surface raiders.
        Ancestral N=500000. Split 5000 gen ago. Basalt at 20000. Surface
        raiders bottleneck to 200, grow to 5000.
    """
    populations = [_basalt_pop, _surface_pop]
    citations = [stdvoidsim.Citation(author="Peaslee et al.", year=1935,
        doi="https://doi.org/10.1666/void.polyp.dem2",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=6e-9,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=20000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=5000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=1000, initial_size=200, population_id=1),
            msprime.MassMigration(time=5000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=5000, initial_size=500000, population_id=0)])

_species.add_demographic_model(_surface_raid())
