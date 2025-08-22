from .codes import COLOR_CODES


def color_str(text, color):
    return COLOR_CODES.get(color, "") + text + COLOR_CODES["reset"]
