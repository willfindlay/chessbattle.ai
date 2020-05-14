import os
import errno
from glob import glob

from chessbattle.defs import PROJECT_ROOT


def static_path(f):
    """
    Find the path to file within static.
    """
    path = os.path.join(PROJECT_ROOT, 'static', f)
    results = glob(path)
    if not len(results):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    elif len(results) > 1:
        raise EnvironmentError(
            f"Too many results for {f}, consider narrowing the search"
        )
    return results[0]
