import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
NEBULA_COLLECTION_MODULE_REGEX = r"^nebulaplugins_[_a-zA-Z][_a-zA-Z0-9]+$"
NEBULA_COLLECTION_NAME_REGEX = r"^nebulaplugins-[-a-zA-Z][-a-zA-Z0-9]+$"

collection_slug = "{{cookiecutter.collection_slug}}"
collection_name = "{{cookiecutter.collection_name}}"

if not re.match(MODULE_REGEX, collection_slug):
    print(
        f"ERROR: The collection slug ({collection_slug}) is not a valid Python module name. "
        "Please do not use - and use _ instead"
    )
    sys.exit(1)

if not re.match(NEBULA_COLLECTION_MODULE_REGEX, collection_slug):
    print(
        f"ERROR: The collection slug ({collection_slug}) is not a valid Nebula collection module name. "
        "Please ensure your collection slug is prefixed with 'nebulaplugins_'"
    )
    sys.exit(1)

if not re.match(NEBULA_COLLECTION_NAME_REGEX, collection_name):
    print(
        "ERROR: The collection name ({collection_name}) is not a valid Nebula collection name. "
        "Please ensure your collection slug is prefixed with 'nebulaplugins-'"
    )
    sys.exit(1)
