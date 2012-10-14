
sphinx-build -Q -b text -d _build/doctrees . _build/text && diff _build/text/index.txt index_as_built.txt
