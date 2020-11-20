# Copyright 2014 Davide Corio

import logging

_logger = logging.getLogger(__name__)

# there are multiple statements that should be guarded
# in wizard_export_fatturapa, so we guard the entire file
try:
    from . import wizard_export_fatturapa
    from . import efattura
except ImportError:
    _logger.debug('Cannot `import pyxb`.')  # Avoid init error if not installed
