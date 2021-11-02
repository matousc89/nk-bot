def crypto_ticker(cmd):
    if cmd.startswith("\\crypto-ticker"):
        pair = cmd.split("-")[-1].lower()
        return [
            {"type": "text", "text": str(pair)},
        ]
    else:
        return []

