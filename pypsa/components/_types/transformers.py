"""Transformers components module."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pypsa.components._types._patch import patch_add_docstring
from pypsa.components.components import Components

if TYPE_CHECKING:
    from collections.abc import Sequence

    import pandas as pd


@patch_add_docstring
class Transformers(Components):
    """Transformers components class.

    This class is used for transformer components. All functionality specific to
    transformers is implemented here. Functionality for all components is implemented in
    the abstract base class.

    See Also
    --------
    [pypsa.Components][] : Base class for all components.

    Examples
    --------
    >>> n.components.transformers
    Empty 'Transformer' Components

    """

    def add(
        self,
        name: str | int | Sequence[int | str],
        suffix: str = "",
        overwrite: bool = False,
        **kwargs: Any,
    ) -> pd.Index:
        """Wrap Components.add() and docstring is patched via decorator."""
        return super().add(
            name=name,
            suffix=suffix,
            overwrite=overwrite,
            **kwargs,
        )
