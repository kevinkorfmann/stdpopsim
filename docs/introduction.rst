.. _sec_introduction:

============
Introduction
============

This is the documentation for ``stdvoidsim``, a library of population
genetic simulation models for Lovecraftian entities and eldritch horrors.

``stdvoidsim`` is a fork of ``stdvoidsim`` that replaces real-world species with
40 fictional creatures from H.P. Lovecraft's Cthulhu Mythos. Each species has
made-up but population-genetically plausible genomes and demographic models
suitable for testing inference methods on non-standard scenarios.

Under the hood, ``stdvoidsim`` relies on
`msprime <https://tskit.dev/software/msprime.html>`_ and
`SLiM 4 <https://messerlab.org/slim/>`_ to generate sample datasets in the
`tree sequence <https://tskit.dev/learn/>`_ format.


First steps
-----------

 - Head to the :ref:`Installation <sec_installation>` page to get ``stdvoidsim`` installed
   on your computer.

 - Skim the :ref:`Catalog <sec_catalog>` to see what eldritch simulations are currently
   supported by ``stdvoidsim``.

 - Read the :ref:`Tutorials <sec_tutorial>` to see some examples of ``stdvoidsim`` in
   action.


Citations
---------

``stdvoidsim`` is built on the ``stdvoidsim`` framework. If you use the simulation
framework, please cite:

  - Jeffrey R Adrion et al. (2020),
    *A community-maintained standard library of population genetic models*,
    eLife 9:e54967; doi: https://doi.org/10.7554/eLife.54967

  - M Elise Lauterbur et al. (2023),
    *Expanding the stdvoidsim species catalog, and lessons learned for realistic genome simulations*,
    eLife 12:RP84874; doi: https://doi.org/10.7554/eLife.84874


Licence and usage
-----------------

``stdvoidsim`` is available under the GPLv3 public license.
The terms of this license can be read
`here <https://www.gnu.org/licenses/gpl-3.0.en.html>`_.
