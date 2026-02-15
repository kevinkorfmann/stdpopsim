#!/usr/bin/env python3
"""Quick test: load stdvoidsim and run tiny simulations for several models."""
import sys
from pathlib import Path

# Allow running from repo root without installing (add parent to path)
repo = Path(__file__).resolve().parent.parent
if str(repo) not in sys.path:
    sys.path.insert(0, str(repo))


def run_one(engine, species_id, model_id, samples, length=5000, seed=42):
    import stdvoidsim
    species = stdvoidsim.get_species(species_id)
    model = species.get_demographic_model(model_id)
    contig = species.get_contig(length=length)
    ts = engine.simulate(model, contig, samples, seed=seed)
    return ts


def main():
    import stdvoidsim

    engine = stdvoidsim.get_default_engine()
    tests = [
        ("DagHyd", "InnsmouthDecline_1M27", {"DeepOnes": 4}, "Deep Ones"),
        ("DagHyd", "HybridIntrogression_2M27", {"DeepOnes": 2, "Hybrids": 2}, "Deep Ones + Hybrids"),
        ("CthGre", "DeepSlumber_1R28", {"Rlyeh": 4}, "Cthulhu (R'lyeh)"),
        ("CthGre", "RlyehRising_2P20", {"Rlyeh": 2, "PacificCultists": 2}, "Cthulhu two-pop"),
        ("ShoNig", "AntarcticRevolt_1D31", {"Shoggoth": 4}, "Shoggoth"),
    ]

    for species_id, model_id, samples, label in tests:
        print(f"{label} ({species_id} / {model_id})")
        try:
            ts = run_one(engine, species_id, model_id, samples)
            print(f"  Trees: {ts.num_trees}, Sites: {ts.num_sites}, Samples: {ts.num_samples}")
        except Exception as e:
            print(f"  FAIL: {e}")
    print("Done")

if __name__ == "__main__":
    main()
