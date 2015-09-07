import flask
from werkzeug import import_string
from jinja2 import loaders

class FlaskTemplateLoader(object):
    def __init__(self,app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self,app):
        self.app = app
        old_loader = app.jinja_loader
        self.loaders = [old_loader]
        self.add_from_settings()
        self.add_from_blueprints()

        app.jinja_loader = loaders.ChoiceLoader(self.loaders)

    def add_from_settings(self):
        if self.app.config.get('TEMPLATE_LOADERS'):
            for loader in self.app.config.get('TEMPLATE_LOADERS'):
                self.loaders.append(import_string(loader))

    def add_from_blueprints(self):
        if self.app.blueprints:
            for bp in self.app.blueprints:
                self.loaders.append(bp.jinja_loader)


