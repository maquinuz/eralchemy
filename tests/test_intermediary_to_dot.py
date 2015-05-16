# -*- coding: utf-8 -*-
from common import parent_id, parent_name, child_id, child_parent_id, relation, child, parent
from eralchemy.main import _intermediary_to_dot
import dot_parser
from eralchemy.cst import GRAPH_BEGINNING
import pytest

GRAPH_LAYOUT = GRAPH_BEGINNING + "%s }"


def assert_is_dot_format(dot):
    assert dot_parser.parse_dot_data(dot) is not None


def test_all_to_dot():
    output = _intermediary_to_dot([child, parent], [relation])
    assert_is_dot_format(output)



# def assert_is_partial_dot_format(dot):
#     assert_is_dot_format(GRAPH_LAYOUT % dot)
#
# def test_relation_is_dot_format():
#     assert_is_partial_dot_format(relation.to_dot())
#
#
# def test_column_is_dot_format():
#     assert_is_partial_dot_format(parent_id.to_dot())
#     assert_is_partial_dot_format(parent_name.to_dot())
#     assert_is_partial_dot_format(child_id.to_dot())
#     assert_is_partial_dot_format(child_parent_id.to_dot())
#
#
# def test_table_is_dot_format():
#     assert_is_partial_dot_format(child.to_dot())
#     assert_is_partial_dot_format(parent.to_dot())