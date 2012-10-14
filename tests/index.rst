.. test-transcluder documentation master file, created by
   sphinx-quickstart on Sun Oct 14 22:34:32 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

test-transcluder
================

Contents:

.. toctree::
   :maxdepth: 2

Transcluding source1 id1 (should display 'source1_id1')

.. transclude:: test_source1 id1

Transcluding source1 id2 (should display 'source1_id2')

.. transclude:: test_source1 id2

Transcluding source2 id1 (should display 'source2_id1')

.. transclude:: test_source2 id1

End transclusions
