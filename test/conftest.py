import pytest
from sqlalchemy.dialects import registry

registry.register("altibase.pyodbc", "sqlalchemy_altibase7.pyodbc", "AltibaseDialect_pyodbc")
#registry.register("altibase", "sqlalchemy_altibase7.pyodbc", "AltibaseDialect_pyodbc")

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")

from sqlalchemy.testing.plugin.pytestplugin import *