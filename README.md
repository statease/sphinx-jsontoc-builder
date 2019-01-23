# json-toc-builder

Builder for sphinx that adds a "toctree" key to the json output with the
full toctree.

## Usage

Set the builder as a extension in `conf.py`:

    extensions = ['sphinxcontrib.jsontoc']

Run sphinx-build with target `jsontoc`:

    sphinx-build -b jsontoc -c . build/jsontoc

There is now a `toctree` key in every fjson file with the top level
toctree (as opposed to the `toc` key which only has the current level).
