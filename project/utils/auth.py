from functools import wraps
from flask import g, abort, request, url_for
from .template import redirect

from project.apps.user.models import User


class GuestUser:
    """
    public visitor
    """

    fullname = 'Guest'

    def can(self, role):
        return False



# ---------- Handlers ---------------#

def admin(fn):
    """
    blog owner views decorator
    """

    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if not g.user.can('login'):
            return redirect(url_for('user.login'))
        return fn(*args, **kwargs)
    return decorated_view



def user_handler(session):
    """
    session handler for users
    """

    email = session.get('email', None)
    if not email:
        g.user = GuestUser()
        return
    g.user = User.objects(email=email).first() or GuestUser()
