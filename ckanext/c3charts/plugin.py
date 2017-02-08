import logging
import ckan.plugins as p
import ckan.plugins.toolkit as toolkit
import ckanext.resourceproxy.plugin as proxy
from ckan.common import json
from pylons import config
ignore_empty = p.toolkit.get_validator('ignore_empty')
log = logging.getLogger(__name__)

class C3ChartsPlugin(p.SingletonPlugin):
  p.implements(p.IConfigurer)
  p.implements(p.IResourceView, inherit=True)

  # IConfigurer

  def update_config(self, config_):
    toolkit.add_template_directory(config_, 'templates')
    toolkit.add_public_directory(config_, 'public')
    toolkit.add_resource('fanstatic', 'c3charts')
    config['ckan.resource_proxy.max_file_size'] = 20000000


  def info(self):
    return {
      'name': 'c3charts' ,
      'title': p.toolkit._('C3.js Charts') ,
      'default_title': p.toolkit._('C3.js Chart') ,
      'icon': 'rocket' ,
      'schema': { 
        'chart_config': [ignore_empty] ,
        'chart_data': [ignore_empty] 
      } ,
    }

  def can_view(self, data_dict):
    resource = data_dict['resource']
    format_lower = resource.get('format', '').lower()

    if format_lower in [ 'csv' ]:
      return True
    return False

  def setup_template_variables(self, context, data_dict):
    url = proxy.get_proxified_resource_url(data_dict)
    chart_data = None
    chart_config = None
    if 'chart_data' in data_dict['resource_view']:
      chart_data = json.dumps(data_dict['resource_view']['chart_data'])
    if 'chart_config' in data_dict['resource_view']:
      chart_config = json.dumps(data_dict['resource_view']['chart_config'])

    return {
      'resource_url': json.dumps(url) ,
      'chart_data': chart_data ,
      'chart_config': chart_config
    }

  def view_template(self, context, data_dict):
    return 'c3_view.html'

  def form_template(self, context, data_dict):
    return 'c3_form.html'


