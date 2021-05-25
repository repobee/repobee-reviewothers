from _repobee import plugin

from repobee_reviewothers import reviewothers


def test_register():
    """Just test that there is no crash"""
    plugin.register_plugins([reviewothers])
