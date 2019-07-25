from five import grok
from plone.directives import dexterity, form
# from plone.multilingualbehavior import directives
from plone.app.multilingual.dx import directives
from zope import schema
from zope.component import queryUtility
from plone.indexer import indexer
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage
from plone.app.textfield import RichText
from my315ok.products import MessageFactory as _
#from my315ok.products.interfaces import IMy315okProductsSettings
#from plone.registry.interfaces import IRegistry
#import pdb
# pdb.set_trace()
#registry = queryUtility(IRegistry)
#settings = registry.forInterface(IMy315okProductsSettings, check=False)
# if settings is None:
#    MAX_CONTENT = 200
# else:
#    MAX_CONTENT = settings
MAX_CONTENT = 200

# Interface class; used to define content-type schema.


class Iproduct(form.Schema, IImageScaleTraversable):
    """
    a product content that contain product image,rich text product spec and product parameters table etc.
    """

    directives.languageindependent('image')
    image = NamedBlobImage(
        title=_(u"product image"),
        description=_(u"a main image of the product"),
        required=False,
    )
    linkurl = schema.TextLine(title=_(u"link to target URI"),
                              default=u"",
                              required=False,)
    text = RichText(
        title=_(u"details spec of the product"),
        required=False,
    )


class product(dexterity.Item):
    grok.implements(Iproduct)

    # Add your class methods and properties here


@indexer(Iproduct)
def linkurl(context):
    """Create a catalogue indexer, registered as an adapter, which can
    populate the ``content`` index with the linkurl .
    """

#     if not Iproduct.providedBy(context):return ""
    try:
        url = context.linkurl
    except BaseException:
        url = context.absolute_url()

    if url == None or "":
        return ""
    return url


@indexer(Iproduct)
def text(context):
    """Create a catalogue indexer, registered as an adapter, which can
    populate the ``content`` index with text .
    """
#     if not Iproduct.providedBy(context):return ""
    pview = context.restrictedTraverse('@@plone')

    try:
        text = context.text.output
    except BaseException:
        text = context.text

    if text == None or "":
        return ""
    croped = pview.cropText(text, MAX_CONTENT)
    if isinstance(croped, unicode):
        return croped.encode('utf-8')
    return croped
