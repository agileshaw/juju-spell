# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2022 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest

from multijuju.cli.base import BaseCMD, BaseJujuCMD, JujuReadCMD, JujuWriteCMD
from multijuju.commands.base import BaseJujuCommand


class TestCMD(BaseCMD):
    name = "test"
    help_msg = "Test command"
    overview = "Test command overview"

    def execute(self, _) -> None:
        """Test execution."""
        pass


class TestJujuCommand(BaseJujuCommand):
    async def execute(self, **kwargs) -> None:
        pass


class TestBaseJujuCMD(BaseJujuCMD, TestCMD):
    command = TestJujuCommand


class TestJujuReadCMD(JujuReadCMD, TestCMD):
    command = TestJujuCommand


class TestJujuWriteCMD(JujuWriteCMD, TestCMD):
    command = TestJujuCommand


@pytest.fixture
def base_cmd():
    """Return test CMD inherited from BaseCMD.."""
    return TestCMD(config=None)


@pytest.fixture
def base_juju_cmd():
    """Return test CMD inherited from BaseJujuCMD."""
    return TestBaseJujuCMD(config=None)


@pytest.fixture
def juju_read_cmd():
    """Return test CMD inherited from JujuReadCMD."""
    return TestJujuReadCMD(config=None)


@pytest.fixture
def juju_write_cmd():
    """Return test CMD inherited from JujuWriteCMD."""
    return TestJujuWriteCMD(config=None)
