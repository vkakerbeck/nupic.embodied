# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2021, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

from .base import CONFIGS as BASE
from .ppo_experiments import CONFIGS as PPO
from .backprop_through_reward import CONFIGS as BACKPROP_THROUGH_REWARD

"""
Import and collect all experiment configurations into one CONFIG
"""
__all__ = ["CONFIGS"]

# Collect all configurations
CONFIGS = dict()
CONFIGS.update(BASE)
CONFIGS.update(BACKPROP_THROUGH_REWARD)
CONFIGS.update(PPO)
