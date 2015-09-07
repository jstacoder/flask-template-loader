## Flask-Template-loader
take more control over the loading of your templates

easy to use:

```python
from flask_template_loader import FlaskTemplateLoader

loader = FlaskTemplateLoader(app)
```

and make sure your loader is an importable path,in the 

```python
TEMPLATE_LOADERS = [
    'some.loader.path',
]
```

config setting


see the `test.py` file for an example

by default flask and flask-template-loader, loads app templates before attempting any secondary 
template loaders, to override this and load `TEMPLATE_LOADERS` loaders or blueprint loaders before
the apps loader, add this to your apps settings:

```python
PREPEND_OTHER_LOADERS = True
```
