.. stdvoidsim documentation index file

Welcome to stdvoidsim
====================

**Population genetic simulations for the Cthulhu Mythos.**

``stdvoidsim`` is a library of demographic and genome models for Lovecraftian
entities and eldritch horrors. Simulate Deep Ones, Shoggoths, Mi-Go, and dozens
more with made-up but population-genetically plausible parameters — powered by
`msprime <https://tskit.dev/msprime/>`_ and `SLiM <https://messerlab.org/slim/>`_
and built on the `stdpopsim <https://stdpopsim.readthedocs.io/>`_ framework.

.. epigraph::
   That is not dead which can eternal lie,
   And with strange aeons even death may die.
   — H.P. Lovecraft, *The Nameless City*

First steps
-----------

- **Install:** :ref:`Installation <sec_installation>` — get ``stdvoidsim`` on your machine.
- **Explore:** :ref:`Catalog <sec_catalog>` — 40 species and demographic models.
- **Run:** :ref:`Tutorial <sec_tutorial>` — examples and workflows.

.. admonition:: Quick run
   :class: quick-run

   Install and simulate 10 Deep One samples over 100 kb:

   .. code-block:: console

      $ pip install stdvoidsim
      $ stdvoidsim DagHyd -d InnsmouthDecline_1M27 -o deep_ones.trees -L 100000 DeepOnes:10

   Then open ``deep_ones.trees`` in `tskit <https://tskit.dev/tskit/>`_ or
   :ref:`continue with the tutorial <sec_tutorial>`.

Catalog at a glance
-------------------

The full :doc:`catalog <catalog>` lists every species and demographic model.
By category:

.. container:: catalog-at-a-glance

   - :ref:`Outer Gods & Great Old Ones <outer-gods-great-old-ones>`
     - *Azathoth primordia*, *Cthulhu greatoldone*, *Chaugnarus faugnis*, *Dagonus maximus*, *Hastur carcosensis*, *Nyarlathotep azathothspawn*, *Shubniggurath fertilitas*, *Tsathoggua somnolentis*, *Yogsothoth dimensionalis*
   - :ref:`Servitor Races & Engineered Species <servitor-races-engineered-species>`
     - *Byakhee voidwing*, *Obscurus silvanus*, *Igneus vampirus*, *Informis generatus*, *Venator obscurus*, *Shoggoth nigrumplasma*, *Starspawn cthulhidae*
   - :ref:`Ancient Civilizations <ancient-civilizations>`
     - *Elderium antarcticae*, *Polypus volantis*, *Migo fungoides*, *Serpentis valusiensis*, *Yithianus temporalis*
   - :ref:`Amphibious & Aquatic <amphibious-aquatic>`
     - *Chromatis extraspatiala*, *Dagonus hydridae*
   - :ref:`Subterranean Horrors <subterranean-horrors>`
     - *Dholos subterraneus*, *Ghastus cavernicola*, *Ghoulish necrophagus*, *Gugus underworldis*, *Degeneratus subterraneus*
   - :ref:`Dreamlands Creatures <dreamlands-creatures>`
     - *Felis ultharensis*, *Araneus lengensis*, *Lunaris bestialis*, *Nightgauntus mantaformis*, *Shantakus dreamlandis*, *Zoogus sylvaticus*
   - :ref:`Interdimensional & Temporal <interdimensional-temporal>`
     - *Dimensius shambleris*, *Houndus tindalosi*
   - :ref:`Arctic & Desert <arctic-desert>`
     - *Gnophkehus arcticus*, *Arenicola abyssalis*
   - :ref:`Human-Adjacent Horrors <human-adjacent-horrors>`
     - *Rattus magicus*, *Tsathoggua choriensis*
   - :ref:`Generic models <generic-models>`
     - Generic demographic models (any species)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   installation
   catalog
   tutorial
   cli_arguments
   api
   development
   changelogs

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
