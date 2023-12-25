"""Interactive components provided by @radix-ui/themes."""
from typing import Literal, Union

from nextpy import el
from nextpy.backend.vars import Var

from ..base import (
    CommonMarginProps,
    RadixThemesComponent,
)

LiteralButtonSize = Literal["1", "2", "3", "4"]


class Inset(el.Div, CommonMarginProps, RadixThemesComponent):
    """Trigger an action or event, such as submitting a form or displaying a dialog."""

    tag = "Inset"

    # The side
    side: Var[Literal["x", "y", "top", "bottom", "right", "left"]]

    clip: Var[Literal["border-box", "padding-box"]]

    # Padding
    p: Var[Union[int, str]]

    # Padding on the x axis
    px: Var[Union[int, str]]

    # Padding on the y axis
    py: Var[Union[int, str]]

    # Padding on the top
    pt: Var[Union[int, str]]

    # Padding on the right
    pr: Var[Union[int, str]]

    # Padding on the bottom
    pb: Var[Union[int, str]]

    # Padding on the left
    pl: Var[Union[int, str]]
