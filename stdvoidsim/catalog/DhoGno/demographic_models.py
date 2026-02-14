import msprime
import stdvoidsim

_species = stdvoidsim.get_species("DhoGno")
_deep_pop = stdvoidsim.Population(id="DeepBurrowers", description="Deep subterranean dholes")
_surface_pop = stdvoidsim.Population(id="SurfaceBreakers", description="Surface-emerging dholes")

def _deep_tunnels():
    id = "DeepTunnels_1C26"
    description = "Single population deep burrowing dhole model"
    long_description = """
        Single population of burrowing dholes. Three epochs: modern
        deep tunnelers (N=15000), expansion after Dreamlands upheaval
        5000 gen ago (N=5000), ancient primordial worms 50000 gen ago
        (N=100000).
    """
    populations = [_deep_pop]
    citations = [stdvoidsim.Citation(author="Carter et al.", year=1926,
        doi="https://doi.org/10.1666/void.dhole.dem1",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=4e-9,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=15000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=5000, initial_size=5000, population_id=0),
            msprime.PopulationParametersChange(time=50000, initial_size=100000, population_id=0)])

_species.add_demographic_model(_deep_tunnels())

def _surface_break():
    id = "SurfaceBreak_2C26"
    description = "Two population deep and surface dhole model"
    long_description = """
        Two populations: deep burrowers and surface-breakers. Ancestral
        N=100000. Split 20000 gen ago. Deep at 15000. Surface bottleneck
        to 100, expand to 8000.
    """
    populations = [_deep_pop, _surface_pop]
    citations = [stdvoidsim.Citation(author="Carter et al.", year=1926,
        doi="https://doi.org/10.1666/void.dhole.dem2",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=4e-9,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=15000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=8000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=5000, initial_size=100, population_id=1),
            msprime.MassMigration(time=20000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=20000, initial_size=100000, population_id=0)])

_species.add_demographic_model(_surface_break())
