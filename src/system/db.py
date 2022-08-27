"""Database Functions.

The following functions give you access to view and modify data in the
database.
"""

from __future__ import print_function

__all__ = [
    "ARRAY",
    "BIGINT",
    "BINARY",
    "BIT",
    "BLOB",
    "BOOLEAN",
    "CHAR",
    "CLOB",
    "DATALINK",
    "DATE",
    "DECIMAL",
    "DISTINCT",
    "DOUBLE",
    "FLOAT",
    "INTEGER",
    "JAVA_OBJECT",
    "LONGNVARCHAR",
    "LONGVARBINARY",
    "LONGVARCHAR",
    "NCHAR",
    "NCLOB",
    "NULL",
    "NUMERIC",
    "NVARCHAR",
    "ORACLE_CURSOR",
    "OTHER",
    "READ_COMMITTED",
    "READ_UNCOMMITTED",
    "REAL",
    "REF",
    "REPEATABLE_READ",
    "ROWID",
    "SERIALIZABLE",
    "SMALLINT",
    "SQLXML",
    "STRUCT",
    "TIME",
    "TIMESTAMP",
    "TINYINT",
    "VARBINARY",
    "VARCHAR",
    "addDatasource",
    "beginNamedQueryTransaction",
    "beginTransaction",
    "clearAllNamedQueryCaches",
    "clearNamedQueryCache",
    "closeTransaction",
    "commitTransaction",
    "createSProcCall",
    "dateFormat",
    "execSProcCall",
    "getConnectionInfo",
    "getConnections",
    "refresh",
    "removeDatasource",
    "rollbackTransaction",
    "runNamedQuery",
    "runPrepQuery",
    "runPrepUpdate",
    "runQuery",
    "runSFNamedQuery",
    "runSFPrepUpdate",
    "runSFUpdateQuery",
    "runScalarPrepQuery",
    "runScalarQuery",
    "runUpdateQuery",
    "setDatasourceConnectURL",
    "setDatasourceEnabled",
    "setDatasourceMaxConnections",
]

from typing import Any, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.script.builtin import (
    DatasetUtilities,
    SProcCall,
)
from java.lang import String
from java.util import Date
from javax.swing import JComponent

# Type codes
# These are codes defined by the JDBC specification.
BIT = -7
REAL = 7
LONGVARCHAR = -1
LONGVARBINARY = -4
TINYINT = -6
DOUBLE = 8
DATE = 91
NULL = 0
SMALLINT = 5
NUMERIC = 2
TIME = 92
ROWID = -8
INTEGER = 4
DECIMAL = 3
TIMESTAMP = 93
CLOB = 2005
BIGINT = -5
CHAR = 1
BINARY = -2
NCLOB = 2011
FLOAT = 6
VARCHAR = 12
VARBINARY = -3
BLOB = 2004
NCHAR = -15
NVARCHAR = -9
LONGNVARCHAR = -16
BOOLEAN = 16
# The following type code constants are available for other uses, but
# are not supported by createSProcCall:
ORACLE_CURSOR = -10
DISTINCT = 2001
STRUCT = 2002
REF = 2006
JAVA_OBJECT = 2000
SQLXML = 2009
ARRAY = 2003
DATALINK = 70
OTHER = 1111

# Isolation levels.
READ_COMMITTED = 2
READ_UNCOMMITTED = 1
REPEATABLE_READ = 4
SERIALIZABLE = 8


def addDatasource(
    jdbcDriver,  # type: String
    name,  # type: String
    description="",  # type: String
    connectUrl=None,  # type: Optional[String]
    username=None,  # type: Optional[String]
    password=None,  # type: Optional[String]
    props=None,  # type: Optional[String]
    validationQuery=None,  # type: Optional[String]
    maxConnections=8,  # type: int
):
    # type: (...) -> None
    """Adds a new database connection in Ignition.

    Args:
        jdbcDriver: The name of the JDBC driver configuration to use.
            Available options are based off the JDBC driver
            configurations on the Gateway.
        name: The datasource name.
        description: Description of the datasource. Optional.
        connectUrl: Default is the connect URL for JDBC driver.
            Optional.
        username: Username to login to the datasource with. Optional.
        password: Password for the login. Optional.
        props: The extra connection parameters. Optional.
        validationQuery: Default is the validation query for the JDBC
            driver. Optional.
        maxConnections: Default is 8. Optional.
    """
    print(
        jdbcDriver,
        name,
        description,
        connectUrl,
        username,
        password,
        props,
        validationQuery,
        maxConnections,
    )


def beginNamedQueryTransaction(*args):
    # type: (*Any) -> String
    """Begins a new database transaction using Named Queries.

    Database transactions are used to execute multiple queries in an
    atomic fashion. After executing queries, you must either commit the
    transaction to have your changes take effect, or rollback the
    transaction which will make all operations since the last commit not
    take place. The transaction is given a new unique string code, which
    is then returned. You can then use this code as the tx argument for
    other system.db.* function calls to execute various types of queries
    using this transaction.

    An open transaction consumes one database connection until it is
    closed. Because leaving connections open indefinitely would exhaust
    the connection pool, each transaction is given a timeout. Each time
    the transaction is used, the timeout timer is reset. For example, if
    you make a transaction with a timeout of one minute, you must
    complete that transaction within a minute. If a transaction is
    detected to have timed out, it will be automatically closed and its
    transaction id will no longer be valid.

    When calling from Vision use:
    system.db.beginNamedQueryTransaction([database], [isolationLevel],
                                         [timeout])

    When calling from Perspective or Gateway scope use:
    system.db.beginNamedQueryTransaction(project, database,
                                        [isolationLevel], [timeout])

    Args:
        *args: Variable length argument list.

    Returns:
         The new transaction ID. You'll use this ID as the "tx" argument
         for all other calls to have them execute against this
         transaction.
    """
    print(args)
    return "transaction_id"


def beginTransaction(database="", isolationLevel=None, timeout=None):
    # type: (Optional[String], Optional[int], Optional[int]) -> String
    """Begins a new database transaction for using run* and runPrep*
    queries.

    Database transactions are used to execute multiple queries in an
    atomic fashion. After executing queries, you must either commit the
    transaction to have your changes take effect, or rollback the
    transaction which will make all operations since the last commit not
    take place. The transaction is given a new unique string code, which
    is then returned. You can then use this code as the tx argument for
    other system.db.* function calls to execute various types of queries
    using this transaction.

    An open transaction consumes one database connection until it is
    closed. Because leaving connections open indefinitely would exhaust
    the connection pool, each transaction is given a timeout. Each time
    the transaction is used, the timeout timer is reset. For example, if
    you make a transaction with a timeout of one minute, you must use
    that transaction at least once a minute. If a transaction is
    detected to have timed out, it will be automatically closed and its
    transaction id will no longer be valid.

    Args:
        database: The name of the database connection to create a
            transaction in. Use "" for the project's default connection.
            Optional.
        isolationLevel: The transaction isolation level to use. Use one
            of the four constants: system.db.READ_COMMITTED,
            system.db.READ_UNCOMMITTED, system.db.REPEATABLE_READ, or
            system.db.SERIALIZABLE. Optional.
        timeout: The amount of time, in milliseconds, that this
            connection is allowed to remain open without being used.
            Timeout counter is reset any time a query or call is
            executed against the transaction, or when committed or
            rolled-back. Optional.

    Returns:
        The new transaction ID. You'll use this ID as the "tx" argument
        for all other calls to have them execute against this
        transaction.
    """
    print(database, isolationLevel, timeout)
    return "transaction_id"


def clearAllNamedQueryCaches(project=None):
    # type: (Optional[String]) -> None
    """This clears the caches of all Named Queries in a project.

    If called from the Shared Scope (i.e., Tag Event Scripts, Alarm
    Pipelines, etc.) then the name of the project must be passed as a
    parameter.

    Args:
        project: The project that contains the Named Query whose cache
            needs to be cleared. Optional.
    """
    print(project)


def clearNamedQueryCache(*args):
    # type: (*String) -> None
    """This clears the cache of a Named Query.

    If called from the Shared Scope (i.e., Tag Event Scripts, Alarm
    Pipelines, etc.) then the name of the project must be passed as a
    parameter.

    When calling from the Project Scope use:
    system.db.clearNamedQueryCache(path)

    When calling from the Shared Scope use:
    system.db.clearNamedQueryCache(project, path)

    Args:
        *args: Variable length argument list.
    """
    print(args)


def closeTransaction(tx):
    # type: (String) -> None
    """Closes the transaction with the given ID.

    You must commit or rollback the transaction before you close it.
    Closing the transaction will return its database connection to the
    pool. The transaction ID will no longer be valid.

    Args:
        tx: The transaction ID.
    """
    print(tx)


def commitTransaction(tx):
    # type: (String) -> None
    """Performs a commit for the given transaction.

    This will make all statements executed against the transaction since
    its beginning or since the last commit or rollback take effect in
    the database. Until you commit a transaction, any changes that the
    transaction makes will not be visible to other connections.

    Note:
        If you are done with the transaction, you must close it after
        you commit it.

    Args:
        tx: The transaction ID.
    """
    print(tx)


def createSProcCall(
    procedureName,  # type: String
    database="",  # type: String
    tx=None,  # type: Optional[String]
    skipAudit=False,  # type: bool
):
    # type: (...) -> SProcCall
    """Creates an SProcCall object, which is a stored procedure call
    context.

    Args:
        procedureName: The name of the stored procedure to call.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        tx: A transaction identifier. If omitted, the call will be
            executed in its own transaction. Optional.
        skipAudit: A flag which, if set to True, will cause the
            procedure call to skip the audit system. Useful for some
            queries that have fields which won't fit into the audit log.
            Optional.

    Returns:
        A stored procedure call context, which can be configured and
        then used as the argument to system.db.execSProcCall.
    """
    print(procedureName, database, tx, skipAudit)
    return SProcCall()


def dateFormat(date, formatPattern):
    # type: (Date, String) -> String
    """This function is used to format Dates nicely as strings.

    It uses a format string to guide its formatting behavior.

    Args:
        date: The Date object that you'd like to format.
        formatPattern: A format pattern string to apply.

    Returns:
        The date as a string formatted according to the format pattern.
    """
    print(date, formatPattern)
    return ""


def execSProcCall(callContext):
    # type: (SProcCall) -> None
    """Executes a stored procedure call.

    The one parameter to this function is an SProcCall - a stored
    procedure call context.

    Args:
        callContext: A stored procedure call context, with any input,
            output, and/or return value parameters correctly configured.
            Use system.db.createSProcCall to create a call context.
    """
    print(callContext)


def getConnectionInfo(name=""):
    # type: (Optional[String]) -> BasicDataset
    """Returns a dataset of information about a single database
    connection, as specified by the name argument, or about the current
    project's default database connection.

    Note:
        The database connection used when called from the Gateway scope
        is the connection configured on the Gateway scripting project.

    Args:
        name: The name of the database connection to find information
            about. Optional.

    Returns:
        A dataset containing information about the named database
        connection or about the current project's default database
        connection, or an empty dataset if the connection wasn't found.
    """
    print(name)
    return BasicDataset()


def getConnections():
    # type: () -> BasicDataset
    """Returns a dataset of information about each configured database
    connection.

    Each row represents a single connection.

    Returns:
        A dataset, where each row represents a database connection.
    """
    return BasicDataset()


def refresh(component, propertyName):
    # type: (JComponent, String) -> bool
    """This function will cause a Vision component binding to execute
    immediately.

    This is most often used for bindings that are set to Polling - Off.
    In this way, you cause a binding to execute on demand, when you know
    that the results of its query will return a new result. To use it,
    you simply specify the component and name of the property on whose
    binding you'd like to refresh.

    Even though the function includes "db" in the name, the function can
    update all types of Vision component bindings, including Property
    and Expression bindings.

    Note:
        This function will only work within the Vision module. To
        manually execute bindings in Perspective, use the refreshBinding
        component method.

    Args:
        component: The component whose property you want to refresh.
        propertyName: The name of the property that has a binding that
            needs to be refreshed.

    Returns:
        True if the property was found and refreshed successfully.
    """
    print(component, propertyName)
    return True


def removeDatasource(name):
    # type: (String) -> None
    """Removes a database connection from Ignition.

    Args:
        name: The name of the database connection in Ignition.
    """
    print(name)


def rollbackTransaction(tx):
    # type: (String) -> None
    """Performs a rollback on the given connection.

    This will make all statements executed against this transaction
    since its beginning or since the last commit or rollback undone.

    Note:
        If you are done with the transaction, you must also close it
        after you do a rollback on it.

    Args:
        tx: The transaction ID.
    """
    print(tx)


def runNamedQuery(*args):
    # type: (*Any) -> Any
    """Runs a named query and returns the results.

    Note that the number of parameters in the function is determined by
    scope. Both versions of the function are listed below.

    When calling from the Project Scope use:
    system.db.runNamedQuery(path, parameters, [tx], [getKey])

    When calling from the Gateway Scope use:
    system.db.runNamedQuery(project, path, parameters, [tx], [getKey])

    Args:
        *args: Variable length argument list.

    Returns:
        The results of the query. The exact object returned depends on
        the Query Type property of the Named Query: typically either a
        dataset when set to Query, an integer representing the number of
        rows affected when set to Update Query, or an object matching
        the datatype of the value returned by a Scalar Query.
    """
    print(args)


def runPrepQuery(
    query,  # type: String
    args,  # type: List[Any]
    database="",  # type: String
    tx=None,  # type: Optional[String]
):
    # type: (...) -> DatasetUtilities.PyDataSet
    """Runs a prepared statement against the database, returning the
    results in a PyDataSet.

    Prepared statements differ from regular queries in that they can use
    a special placeholder, the question-mark character (?) in the query
    where any dynamic arguments would go, and then use an array of
    values to provide real information for those arguments. Make sure
    that the length of your argument array matches the number of
    question-mark placeholders in your query.

    This call should be used for SELECT queries. This is a useful
    alternative to system.db.runQuery because it allows values in the
    WHERE clause, JOIN clause, and other clauses to be specified without
    having to turn those values into strings. This is safer because it
    protects against a problem known as a SQL injection attack, where a
    user can input data that affects the query's semantics.

    Note:
        The "?" placeholder refers to variables of the query statement
        that help the statement return the correct information. The "?"
        placeholder cannot reference column names, table names, or the
        underlying syntax of the query. This is because the SQL standard
        for handling the "?" placeholder excludes these items.

    Args:
        query: A query (typically a SELECT) to run as a prepared
            statement with placeholders (?) denoting where the arguments
            go.
        args: A list of arguments. Will be used in order to match each
            placeholder (?) found in the query.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used.
        tx: A transaction identifier. If omitted, the query will be
            executed in its own transaction. Optional.

    Returns:
        The results of the query as a PyDataSet.
    """
    print(query, args, database, tx)
    return DatasetUtilities.PyDataSet()


def runPrepUpdate(
    query,  # type: String
    args,  # type: List[Any]
    database="",  # type: String
    tx=None,  # type: Optional[String]
    getKey=False,  # type: bool
    skipAudit=True,  # type: bool
):
    # type: (...) -> int
    """Runs a prepared statement against the database, returning the
    number of rows that were affected.

    Prepared statements differ from regular queries in that they can use
    a special placeholder, the question-mark character (?) in the query
    where any dynamic arguments would go, and then use an array of
    values to provide real information for those arguments. Make sure
    that the length of your argument array matches the number of
    question-mark placeholders in your query. This call should be used
    for UPDATE, INSERT, and DELETE queries.

    Note:
        The "?" placeholder refers to variables of the query statement
        that help the statement return the correct information. The "?"
        placeholder cannot reference column names, table names, or the
        underlying syntax of the query. This is because the SQL standard
        for handling the "?" placeholder excludes these items.

    Args:
        query: A query (typically an UPDATE, INSERT, or DELETE) to run
            as a prepared statement with placeholders (?) denoting where
            the arguments go.
        args: A list of arguments. Will be used in order to match each
            placeholder (?) found in the query.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        tx: A transaction identifier. If omitted, the update will be
            executed in its own transaction. Optional.
        getKey: A flag indicating whether or not the result should be
            the number of rows returned (getKey=0) or the newly
            generated key value that was created as a result of the
            update (getKey=1). Not all databases support automatic
            retrieval of generated keys. Optional.
        skipAudit: A flag which, if set to True, will cause the prep
            update to skip the audit system. Useful for some queries
            that have fields which won't fit into the audit log.
            Optional.

    Returns:
        The number of rows affected by the query, or the key value that
        was generated, depending on the value of the getKey flag.
    """
    print(query, args, database, tx, getKey, skipAudit)
    return 1


def runQuery(
    query,  # type: String
    database="",  # type: String
    tx=None,  # type: Optional[String]
):
    # type: (...) -> DatasetUtilities.PyDataSet
    """Runs a SQL query, usually a SELECT query, against a database,
    returning the results as a dataset.

    If no database is specified, or the database is the empty-string "",
    then the current project's default database connection will be used.
    The results are returned as a PyDataSet, which is a wrapper around
    the standard dataset that is convenient for scripting.

    Args:
        query: A SQL query, usually a SELECT query, to run.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used.
        tx: A transaction identifier. If omitted, the query will be
            executed in its own transaction.

    Returns:
        The results of the query as a PyDataSet.
    """
    print(query, database, tx)
    return DatasetUtilities.PyDataSet()


def runSFNamedQuery(*args):
    # type: (*Any) -> bool
    """Runs a named query that goes through the Store and Forward
    system.

    Note that the number of parameters in the function is determined by
    scope.

    When calling from the Project Scope use:
    system.db.runSFNamedQuery(path, params)

    When calling from the Gateway Scope use:
    system.db.runSFNamedQuery(project, path, params)

    Args:
        *args : Variable length argument list.

    Returns:
        True if successfully sent to the Store and Forward system.
    """
    print(args)
    return True


def runSFPrepUpdate(query, args, datasources):
    # type: (String, List[Any], List[String]) -> bool
    """Runs a prepared statement query through the store and forward
    system and to multiple datasources at the same time.

    Prepared statements differ from regular queries in that they can use
    a special placeholder, the question-mark character (?) in the query
    where any dynamic arguments would go, and then use an array of
    values to provide real information for those arguments. Make sure
    that the length of your argument array matches the number of
    question-mark placeholders in your query. This call should be used
    for UPDATE, INSERT, and DELETE queries.

    Args:
        query: A query (typically an UPDATE, INSERT, or DELETE) to run
            as a prepared statement, with placeholders (?) denoting
            where the arguments go.
        args: A list of arguments. Will be used in order to match each
            placeholder (?) found in the query.
        datasources: List of datasources to run the query through.

    Returns:
        True if successfully sent to Store and Forward system.
    """
    print(query, args, datasources)
    return True


def runSFUpdateQuery(query, datasources):
    # type: (String, List[String]) -> bool
    """Runs an query through the store and forward system and to
    multiple datasources at the same time.

    Args:
        query: A query (typically an UPDATE, INSERT, or DELETE) to run.
        datasources: List of datasources to run the query through.

    Returns:
        True if successful and False if not.
    """
    print(query, datasources)
    return True


def runScalarPrepQuery(
    query,  # type: String
    args,  # type: List[Any]
    database="",  # type: String
    tx=None,  # type: Optional[String]
):
    # type: (...) -> Any
    """Runs a prepared statement against a database connection just like
    the runPrepQuery function, but only returns the value from the first
    row and column.

    If no results are returned from the query, the special value None is
    returned.

    Args:
        query: A SQL query (typically a SELECT) to run as a prepared
            statement with placeholders (?) denoting where the arguments
            go, that should be designed to return one row and one
            column.
        args: A list of arguments. Will be used in order to match each
            placeholder (?) found in the query.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        tx: A transaction identifier. If omitted, the query will be
            executed in its own transaction. Optional.

    Returns:
         The value from the first row and first column of the results.
         Returns None if no rows were returned.
    """
    print(query, args, database, tx)


def runScalarQuery(query, database="", tx=None):
    # type: (String, Optional[String], Optional[String]) -> Any
    """Runs a query against a database connection just like the runQuery
    function, but only returns the value from the first row and column.

    If no results are returned from the query, the special value None is
    returned.

    Args:
        query: A SQL query that should be designed to return one row and
            one column.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        tx: A transaction identifier. If omitted, the query will be
            executed in its own transaction. Optional.

    Returns:
         The value from the first row and first column of the results.
         Returns None if no rows were returned.
    """
    print(query, database, tx)


def runUpdateQuery(
    query,  # type: String
    database="",  # type: String
    tx=None,  # type: Optional[String]
    getKey=False,  # type: bool
    skipAudit=True,  # type: bool
):
    # type: (...) -> int
    """Runs a query against a database connection, returning the number
    of rows affected.

    Typically this is an UPDATE, INSERT, or DELETE query. If no database
    is specified, or the database is the empty-string "", then the
    current project's default database connection will be used.

    Note:
        You may want to use the runPrepUpdate query if your query is
        constructed with user input (to avoid the user's input from
        breaking your syntax) or if you need to insert binary or BLOB
        data.

    Args:
        query: A SQL query, usually an INSERT, UPDATE, or DELETE query,
            to run.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used.
        tx: A transaction identifier. If omitted, the update will be
            executed in its own transaction.
        getKey: A flag indicating whether or not the result should be
            the number of rows returned (getKey=0) or the newly
            generated key value that was created as a result of the
            update (getKey=1). Not all databases support automatic
            retrieval of generated keys.
        skipAudit: A flag which, if set to True, will cause the update
            query to skip the audit system. Useful for some queries that
            have fields which won't fit into the audit log.

    Returns:
        The number of rows affected by the query, or the key value that
        was generated, depending on the value of the getKey flag.
    """
    print(query, database, tx, getKey, skipAudit)
    return 1


def setDatasourceConnectURL(name, connectUrl):
    # type: (String, String) -> None
    """Changes the connect URL for a given database connection.

    Args:
        name: The name of the database connection in Ignition.
        connectUrl: The new connect URL.
    """
    print(name, connectUrl)


def setDatasourceEnabled(name, enabled):
    # type: (String, bool) -> None
    """Enables/disables a given database connection.

    Args:
        name: The name of the database connection in Ignition.
        enabled: Specifies whether the database connection will be set
            to enabled or disabled state.
    """
    print(name, enabled)


def setDatasourceMaxConnections(name, maxConnections):
    # type: (String, int) -> None
    """Sets the Max Active and Max Idle parameters of a given database
    connection.

    Ags:
        name: The name of the database connection in Ignition.
        maxConnections: The new value for Max Active and Max Idle.
    """
    print(name, maxConnections)
