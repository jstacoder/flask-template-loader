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
