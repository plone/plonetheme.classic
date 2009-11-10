from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope browser layer.
       If you need to register a viewlet only for the
       "Plone Classic Theme" theme, this interface must be its layer.
    """
