"""Main module of pandas-profiling.

.. include:: ../../README.md
"""

from instant_eda.config import Config, config
from instant_eda.controller import pandas_decorator
from instant_eda.profile_report import InstantEDA
from instant_eda.version import __version__

clear_config = InstantEDA.clear_config
