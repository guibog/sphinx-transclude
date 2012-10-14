.. test-transcluder documentation master file, created by
   sphinx-quickstart on Sun Oct 14 22:34:32 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

test-transcluder
================

Transclusions
-------------

Transcluding source1 id1 (should display 'source1_id1')

.. transclude:: test_source1 id1

Transcluding source1 id2 (should display 'source1_id2')

.. transclude:: test_source1 id2

Transcluding source2 id1 (should display 'source2_id1')

.. transclude:: test_source2 id1

Errors
------

Transcluding from unexisiting file (should display an error message)

.. transclude:: test_source_MISSING id1

Transcluding from unexisting target (should display error message)

.. transclude:: test_source1 id_MISSING

Wrong directive: (nothing should be displayed)

.. transclude:: missing_target

End transclusions
