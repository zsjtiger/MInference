# Copyright (c) 2024-2025 Microsoft
# Licensed under The MIT License [see LICENSE for details]

_MAJOR = "0"
_MINOR = "1"
# On master and in a nightly release the patch should be one ahead of the last
# released build.
_PATCH = "6"
# This is mainly for nightly builds which have the suffix ".dev$DATE". See
# https://semver.org/#is-v123-a-semantic-version for the semantics.
_SUFFIX = ".0"

VERSION_SHORT = "{0}.{1}".format(_MAJOR, _MINOR)
VERSION = "{0}.{1}.{2}{3}".format(_MAJOR, _MINOR, _PATCH, _SUFFIX)
