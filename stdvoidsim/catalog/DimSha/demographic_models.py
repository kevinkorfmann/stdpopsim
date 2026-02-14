import msprime
import stdvoidsim

_species = stdvoidsim.get_species("DimSha")
_prime_pop = stdvoidsim.Population(id="PrimePlane", description="Shamblers on the prime material plane")
_between_pop = stdvoidsim.Population(id="BetweenSpaces", description="Shamblers in interplanar voids")

def _planar_drift():
    id = "PlanarDrift_1B33"
    description = "Single population interplanar drift model"
    long_description = """
        Single population drifting between planes. Three epochs: modern
        scattered (N=3000), planar convergence 1000 gen ago (N=10000),
        ancient unified plane 10000 gen ago (N=500).
    """
    populations = [_prime_pop]
    citations = [stdvoidsim.Citation(author="Bloch et al.", year=1933,
        doi="https://doi.org/10.1666/void.shambler.dem1",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=8e-9,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=3000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=1000, initial_size=10000, population_id=0),
            msprime.PopulationParametersChange(time=10000, initial_size=500, population_id=0)])

_species.add_demographic_model(_planar_drift())

def _plane_split():
    id = "PlaneSplit_2B33"
    description = "Two population prime plane and interplanar void model"
    long_description = """
        Two populations: prime plane and interplanar voids. Ancestral
        N=10000. Split 2000 gen ago. Prime at 3000. Voids bottleneck
        to 50, grow to 2000.
    """
    populations = [_prime_pop, _between_pop]
    citations = [stdvoidsim.Citation(author="Bloch et al.", year=1933,
        doi="https://doi.org/10.1666/void.shambler.dem2",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=8e-9,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=3000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=2000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=500, initial_size=50, population_id=1),
            msprime.MassMigration(time=2000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=2000, initial_size=10000, population_id=0)])

_species.add_demographic_model(_plane_split())
