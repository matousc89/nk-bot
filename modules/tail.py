
class TailCommand:

    def __init__(self):
        self.help = """Use as \\tail x (the x is number of lines)"""

    def __call__(self, params):
        """
        This is a test function - it should send a text and picture.
        :return:
        """
        if params:
            try:
                n = int(params)
            except:
                n = 10
        else:
            n = 10
        with open("bot.log") as f:
            whole_log = f.read()
            msg = "\n".join(whole_log.split("\n")[-n-1:])

        default_msg = [
            {"type": "text", "text": "`{}`".format(msg)},
        ]
        return default_msg

if __name__ == "__main__":
    c = TailCommand()
    print(c.__call__(1))