import os

from datetime import datetime
from hashlib import md5

from flask import current_app


def now(format):
    """Returns current date in the specified format."""
    now = datetime.now()
    return now.strftime(format)


def versioned_static(filename):
    """
    Template function for generating URLs to static assets:
    Given the path for a static file, output a url path
    with a hex hash as a query string for versioning.
    """
    static_path = current_app.static_folder
    static_url = current_app.static_url_path

    file_path = os.path.join(static_path, filename)
    if not os.path.isfile(file_path):
        # File is missing, simply return the string so we don't break anything
        return f"{static_url}/{filename}?v=file-not-found"

    file_hash = md5()
    with open(file_path, 'rb') as file_contents:
        for chunk in iter(lambda: file_contents.read(4096), b""):
            file_hash.update(chunk)
    
    return f"{static_url}/{filename}?v={file_hash.hexdigest()[0:7]}"


def base_context():
    return dict(now=now, versioned_static=versioned_static)