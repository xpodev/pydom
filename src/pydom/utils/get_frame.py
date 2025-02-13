import sys
from sys import exc_info
from types import FrameType


def get_frame_fallback(n: int):
    try:
        raise Exception
    except Exception:
        frame: FrameType = exc_info()[2].tb_frame.f_back  # type: ignore
        for _ in range(n):
            frame = frame.f_back  # type: ignore
        return frame


def load_get_frame_function():
    if hasattr(sys, "_getframe"):
        return sys._getframe

    return get_frame_fallback


get_frame = load_get_frame_function()
