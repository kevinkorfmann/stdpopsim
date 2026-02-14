"""
Tests for simulation engine infrastructure.
"""

import stdvoidsim
import msprime
import pytest
import numpy as np


class TestEngineAPI:
    """
    Tests for the API exposed for simulation engines.
    """

    def _test_engine(self, engine):
        assert isinstance(engine, stdvoidsim.Engine)
        assert engine.simulate is not None
        assert len(engine.citations) != 0
        assert len(engine.get_version()) != 0

    def test_get_default_engine(self):
        engine = stdvoidsim.get_default_engine()
        self._test_engine(engine)

    def test_all_engines(self):
        for engine in stdvoidsim.all_engines():
            self._test_engine(engine)

    def test_register_engine(self):
        class MyEngine(stdvoidsim.Engine):
            id = "test-engine"
            name = "test"
            citations = []

        engine1 = MyEngine()
        stdvoidsim.register_engine(engine1)
        engine2 = stdvoidsim.get_engine(engine1.id)
        assert engine1 == engine2
        # remove engine to avoid possible problems with other tests
        del stdvoidsim.engines._registered_engines[engine1.id]

    def test_register_duplicate(self):
        engine = stdvoidsim.get_default_engine()
        with pytest.raises(ValueError):
            stdvoidsim.register_engine(engine)

    def test_get_engine(self):
        with pytest.raises(ValueError):
            stdvoidsim.get_engine("nonexistent")

    def test_abstract_base_class(self):
        e = stdvoidsim.Engine()
        with pytest.raises(NotImplementedError):
            e.simulate(None, None, None)
        with pytest.raises(NotImplementedError):
            e.get_version()


@pytest.mark.filterwarnings(
    "ignore:.*model has mutation rate.*but this simulation used.*"
)
class TestBehaviour:
    def test_simulate_nonexistent_param(self):
        species = stdvoidsim.get_species("HomSap")
        model = species.get_demographic_model("AshkSub_7G19")
        good_kwargs = dict(
            demographic_model=model,
            contig=species.get_contig("chr1"),
            samples={"YRI": 5, "CHB": 5, "CEU": 5},
            dry_run=True,
        )
        bad_kwargs = good_kwargs.copy().update(nonexistent_param=None)
        for engine in stdvoidsim.all_engines():
            engine.simulate(**good_kwargs)
            with pytest.raises(TypeError):
                engine.simulate(**bad_kwargs)

    def test_required_params(self):
        species = stdvoidsim.get_species("HomSap")
        model = species.get_demographic_model("AshkSub_7G19")
        contig = (species.get_contig("chr1"),)
        for engine in stdvoidsim.all_engines():
            with pytest.raises(TypeError):
                engine.simulate(model, contig)

    def test_msprime_kwargs(self):
        species = stdvoidsim.get_species("HomSap")
        model = species.get_demographic_model("AshkSub_7G19")
        contig = species.get_contig("chr22", right=5e5)
        samples = {"YRI": 5}
        engine = stdvoidsim.get_engine("msprime")
        sim_arg = engine.simulate(
            model, contig, samples, record_full_arg=True, random_seed=1
        )
        assert any(msprime.NODE_IS_RE_EVENT == sim_arg.tables.nodes.flags)

    def test_msprime_seed(self):
        species = stdvoidsim.get_species("HomSap")
        model = species.get_demographic_model("AshkSub_7G19")
        contig = species.get_contig("chr22", right=5e5)
        samples = {"YRI": 5}
        engine = stdvoidsim.get_engine("msprime")
        with pytest.raises(ValueError):
            engine.simulate(model, contig, samples, seed=1, random_seed=1)
        sim_seed = engine.simulate(model, contig, samples, seed=1)
        sim_random_seed = engine.simulate(model, contig, samples, random_seed=1)
        assert sim_seed.tables.edges == sim_random_seed.tables.edges

    def test_non_neutral_contig(self):
        species = stdvoidsim.get_species("HomSap")
        model = species.get_demographic_model("AshkSub_7G19")
        samples = {"YRI": 5}
        contig = stdvoidsim.Contig.basic_contig(length=100)
        contig.clear_dfes()
        props = [1]
        mt = [stdvoidsim.MutationType(distribution_type="f", distribution_args=[1])]
        dfes = [
            stdvoidsim.DFE(
                id=str(0),
                description="test",
                long_description="test test",
                proportions=props,
                mutation_types=mt,
            )
        ]
        contig.add_dfe(intervals=np.array([[0, 50]]), DFE=dfes[0])
        engine = stdvoidsim.get_engine("msprime")
        with pytest.raises(ValueError):
            engine.simulate(model, contig, samples, seed=1)
        # okay now change selection coefficient to neutral
        contig.clear_dfes()
        props = [1]
        mt = [stdvoidsim.MutationType(distribution_type="f", distribution_args=[0])]
        dfes = [
            stdvoidsim.DFE(
                id=str(0),
                description="test",
                long_description="test test",
                proportions=props,
                mutation_types=mt,
            )
        ]
        contig.add_dfe(intervals=np.array([[0, 50]]), DFE=dfes[0])
        engine = stdvoidsim.get_engine("msprime")
        engine.simulate(model, contig, samples, seed=1)

    def test_gene_conversion(self):
        species = stdvoidsim.get_species("DroMel")
        model = species.get_demographic_model("African3Epoch_1S16")
        samples = {"AFR": 5}
        contig = species.get_contig(length=1000, use_species_gene_conversion=True)
        assert contig.gene_conversion_fraction > 0
        assert contig.gene_conversion_length > 0
        engine = stdvoidsim.get_engine("msprime")
        engine.simulate(model, contig, samples, seed=1)

    def test_msprime_bad_samples(self):
        engine = stdvoidsim.get_engine("msprime")
        species = stdvoidsim.get_species("HomSap")
        contig = species.get_contig("chr1")
        model = stdvoidsim.PiecewiseConstantSize(species.population_size)
        samples = [1, 2, ["foo"]]
        with pytest.raises(ValueError, match="Samples must be a dict"):
            engine.simulate(
                demographic_model=model,
                contig=contig,
                samples=samples,
            )
