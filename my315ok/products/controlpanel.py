from my315ok.products import MessageFactory as _
from my315ok.products.interfaces import IMy315okProductsSettings
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout


class My315okProductsControlPanelForm(RegistryEditForm):
    schema = IMy315okProductsSettings

    label = _(u"My315okProducts control panel")


My315okProductsControlPanelView = layout.wrap_form(
    My315okProductsControlPanelForm, ControlPanelFormWrapper)
