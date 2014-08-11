#!/usr/bin/env python
# -*- coding:utf-8 -*-

from arango import create
from nose.tools import assert_is_not, assert_equal

from .tests_integraion_base import TestsIntegration


class IntegrationTestsDB(TestsIntegration):
    def setup(self):
        super(IntegrationTestsDB, self).setup()

    def tearDown(self):
        super(IntegrationTestsDB, self).tearDown()

    def test_duplicate_creation(self):
        db = create(db="test").database.create()
        db2 = create(db="test").database.create()
        assert_is_not(db, None)
        assert_is_not(db2, None)
        # assert_equal(db, db2)
        db.delete()
        db2.delete()
