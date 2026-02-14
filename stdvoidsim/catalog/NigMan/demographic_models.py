import msprime
import stdvoidsim

_species = stdvoidsim.get_species("NigMan")
_peak_pop = stdvoidsim.Population(id="NophorPeaks", description="Nightgaunts of Ngranek peaks")
_dream_pop = stdvoidsim.Population(id="DreamVoid", description="Dream void nightgaunt colony")

def _ngranek_flock():
    id = "NgranekFlock_1C26"
    description = "Single population Ngranek peak colony model"
    long_description = """
        Single population of nightgaunts on Ngranek. Three epochs:
        modern flock (N=75000), expansion from Nodens' service 5000 gen
        ago (N=10000), ancient dreamlands origin 50000 gen ago (N=100000).
    """
    populations = [_peak_pop]
    citations = [stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
        doi="https://en.wikipedia.org/wiki/Necronomicon",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=75000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=5000, initial_size=10000, population_id=0),
            msprime.PopulationParametersChange(time=50000, initial_size=100000, population_id=0)])

_species.add_demographic_model(_ngranek_flock())

def _dream_split():
    id = "DreamVoidSplit_2C26"
    description = "Two population Ngranek and dream void model"
    long_description = """
        Two populations: Ngranek peaks and dream void colony. Ancestral
        N=100000. Split 20000 gen ago. Peaks stable at 75000. Void colony
        bottleneck to 500 then expand to 40000.
    """
    populations = [_peak_pop, _dream_pop]
    citations = [stdvoidsim.Citation(author="Lovecraft, H.P.", year=1928,
        doi="https://en.wikipedia.org/wiki/Necronomicon",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=75000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=40000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=5000, initial_size=500, population_id=1),
            msprime.MassMigration(time=20000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=20000, initial_size=100000, population_id=0)])

_species.add_demographic_model(_dream_split())
