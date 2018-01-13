#!/usr/bin/env python
#
# Copyright (c) 2015 All rights reserved
# This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
#
# http://www.apache.org/licenses/LICENSE-2.0
#

from __future__ import division

import logging
import os
import re
import shutil
import subprocess
import time
import uuid

import yaml

from functest.core import testcase
from functest.opnfv_tests.openstack.snaps import snaps_utils
from functest.opnfv_tests.openstack.tempest import conf_utils
from functest.utils.constants import CONST
import functest.utils.functest_utils as ft_utils


""" logging configuration """
logger = logging.getLogger(__name__)


class K8sTesting(testcase.TestCase):

    def __init__(self, **kwargs):
        super(K8sTesting, self).__init__(**kwargs)

    def run(self):

        self.start_time = time.time()
        try:
            self.result = 100
            res = testcase.TestCase.EX_RUN_ERROR
        except Exception as e:
            logger.error('Error with run: %s' % e)
            res = testcase.TestCase.EX_RUN_ERROR

        self.stop_time = time.time()
        return res


class K8sSmokeTest(K8sTesting):

    def __init__(self, **kwargs):
        if "case_name" not in kwargs:
            kwargs["case_name"] = 'k8s_e2e_testing'
        K8sTesting.__init__(self, **kwargs)
        self.MODE = "custom"
        self.OPTION = "--concurrency 1"
