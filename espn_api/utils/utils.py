"""Utility helpers used across the ESPN API package."""

import json


def json_parsing(obj, key):
    """Recursively pull values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Return all matching values in an object."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict)) or (isinstance(v, (list)) and  v and isinstance(v[0], (list, dict))):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results[0] if results else results


def build_fantasy_filter_headers(filters):
    """Create the `x-fantasy-filter` headers dict from a filters object.

    This centralizes header construction and prevents repetition.
    """
    return {'x-fantasy-filter': json.dumps(filters)}
