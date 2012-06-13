
import os

from flask import request, current_app as app

from pystache.renderer import Renderer


def _get_renderer(append=None):
    append = append or []
    app.logger.debug(append)

    bp = app.blueprints.get(request.blueprint, None)

    if not bp or not bp.template_folder:
        dirs = [os.path.join(app.import_name, app.template_folder, *append)]
    else:
        path = bp.import_name.split('.') + [bp.template_folder]
        dirs = [os.path.join(*path + append)]

    app.logger.debug(dirs)
    return Renderer(search_dirs=dirs)


def render_view(view):
    return _get_renderer().render(view)


def render_template(template, context=None):
    parts = template.split('/')
    renderer = _get_renderer(parts[:-1])
    return renderer.render(renderer.load_template(parts[-1:][0]), context or {})
