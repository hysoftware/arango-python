#!/usr/bin/env python
# -*- coding:utf-8 -*-

from arango import create
from nose.tools import assert_is_not

from .tests_integraion_base import TestsIntegration


class IntegrationTestsDB(TestsIntegration):
    def setup(self):
        super(IntegrationTestsDB, self).setup()

    def tearDown(self):
        super(IntegrationTestsDB, self).tearDown()

    def test_duplicate_creation(self):
        con = create(db="test")
        assert_is_not(con.database.create(), None)
        con.database.delete()
