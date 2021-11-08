
class TestCommand:

    def __init__(self):
        self.help = """Use as \\test"""

    def __call__(self, params):
        """
        This is a test function - it should send a text and picture.
        :return:
        """
        default_msg = [
            {"type": "fig", "filepath": 'test_picture.jpg'},
            {"type": "text", "text": "This is a massive test. "},
        ]
        if params:
            default_msg += [{"type": "text", "text": "Used params: {}".format(params)},]
        return default_msg
