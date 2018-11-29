from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import HorizontalIconModel, HorizontalIconsContainerModel

@plugin_pool.register_plugin
class HorizontalIconsContainerPlugin(CMSPluginBase):

    module = 'Jumpsuite'
    model = HorizontalIconsContainerModel
    name = _('Horizontal Icons Container')
    child_classes = ['HorizontalIconPlugin']

    render_template = 'horizontal_icons.html'

    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance
        })
        return context

@plugin_pool.register_plugin
class HorizontalIconPlugin(CMSPluginBase):

    module = 'Jumpsuite'
    model = HorizontalIconModel
    name = _('Horizontal Icon')
    parent_classes = ['HorizontalIconsContainerPlugin']

    render_template = 'icon.html'

    #child_count = CountersContainerPlugin.get(cmsplugin_ptr=instance.parent.child_count)

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance
        })
        return context
