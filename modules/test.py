def test(cmd=None):
    """
    This is a test function - it should send a text and picture.
    :return:
    """
    return [
        {"type": "fig", "filepath": 'test_picture.jpg'},
        {"type": "text", "text": "This is a massive test."},
    ]
