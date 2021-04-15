from sphinxcontrib.serializinghtml import JSONHTMLBuilder
from sphinx.environment.adapters.toctree import TocTree

class JSONTOCHTMLBuilder(JSONHTMLBuilder):

    name = 'jsontoc'

    def get_doc_context(self, docname, body, metatags):

        out_dict = super(JSONTOCHTMLBuilder, self).get_doc_context(docname, body, metatags)

        self_toctree = TocTree(self.env).get_toctree_for(docname, self, True)
        toctree = self.render_partial(self_toctree)['fragment']
        out_dict['toctree'] = toctree

        return out_dict
