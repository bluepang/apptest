import six
import re
import requests
import os


def download(src):
    if isinstance(src, six.string_types):
        if re.match(r"^https?://", src):
            r = requests.get(src, stream=True)
            if r.status_code != 200:
                raise IOError(
                    "Request URL {!r} status_code {}".format(src, r.status_code))
            fileobj = r.raw
        elif os.path.isfile(src):
            fileobj = open(src, 'rb')
        else:
            raise IOError("file {!r} not found".format(src))
    else:
        assert hasattr(src, "read")
        fileobj = src

    return fileobj