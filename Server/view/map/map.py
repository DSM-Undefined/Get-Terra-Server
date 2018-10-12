from flasgger import swag_from

from view.base_resource import BaseResource
from docs.map import WEB_MAP_GET, ANDROID_MAP_GET


class WebMap(BaseResource):

    @swag_from(WEB_MAP_GET)
    def get(self):
        pass


class AndroidMap(BaseResource):

    @swag_from(ANDROID_MAP_GET)
    def get(self):
        pass