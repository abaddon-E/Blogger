from flask import render_template, jsonify, request,\
    redirect as flask_redirect, g



def path(link):
    """
    make template address
    """
    if request.blueprint == 'user':
        link = 'user/' + link
        return link
    if g.base_site.is_front:
        link = 'front/' + link
        return link
    if g.user.can('login'):
        link = 'admin/' + link
        return link
    return 'landings/' + g.base_site.current + '/' + link


def render(template, **context):
    if request.is_xhr:
        return jsonify(html=render_template(path(template), **context))
    return render_template(path(template), **context)


def redirect(url):
    if request.is_xhr:
        return jsonify(redirect=url)
    return flask_redirect(url)
