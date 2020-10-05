"""This file add the decorator on the DataFrame object."""
from pandas import DataFrame

from instant_eda.__init__ import InstantEDA


def profile_report(df, **kwargs) -> InstantEDA:
    """Profile a DataFrame.

    Args:
        df: The DataFrame to profile.
        **kwargs: Optional arguments for the ProfileReport object.

    Returns:
        A ProfileReport of the DataFrame.
    """
    p = InstantEDA(df, **kwargs)
    return p


DataFrame.profile_report = profile_report
