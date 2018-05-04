# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103,C0111,R0201

"""Database Functions
The following functions give you access to view and modify data in the database."""

__all__ = [
    'beginTransaction',
    'closeTransaction',
    'commitTransaction',
    'createSProcCall',
    'execSProcCall',
    'rollbackTransaction'
]

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
# The following type code constants are available for other uses, but are not supported by
# createSProcCall:
ORACLE_CURSOR = -10
DISTINCT = 2001
STRUCT = 2002
REF = 2006
JAVA_OBJECT = 2000
SQLXML = 2009
ARRAY = 2003
DATALINK = 70
OTHER = 1111


class SProcCall(object):
    def __init__(self):
        pass

    def getResultSet(self):
        """Returns a dataset that is the resulting data of the stored procedure, if any.

        Returns:
            Dataset: The dataset that is the resulting data of the stored procedure, if any.
        """
        pass

    def getUpdateCount(self):
        """Returns the number of rows modified by the stored procedure, or -1 if not applicable.

        Returns:
             int: The number of rows modified by the stored procedure, or -1 if not applicable.
        """
        return 1

    def getReturnValue(self):
        """Returns the return value, if registerReturnParam had been called.

        Returns:
             int: The return value, if registerReturnParam had been called.
        """
        return 0

    def getOutParamValue(self, param):
        """Returns the value of the previously registered out-parameter.

        Args:
            param: Index (int) or name (str) of the previously registered out-parameter.

        Returns:
            object: The value of the previously registered out-parameter.
        """
        print param
        return 0

    def registerInParam(self, param, typeCode, value):
        """Registers an in parameter for the stored procedure.

        Args:
            param (object): Index (int starting at 1, not 0), or name (str).
            typeCode (int): Type code constant.
            value (object): Value of type `typeCode`.
        """
        print(param, typeCode, value)

    def registerOutParam(self, param, typeCode):
        """Registers an out parameter for the stored procedure.

        Args:
            param (object): Index (int starting at 1, not 0), or name (str).
            typeCode (int): Type code constant.
        """
        print(param, typeCode)

    def registerReturnParam(self, typeCode):
        """Use this function to specify the datatype of the returned value.

        Args:
            typeCode (int): Type code constant.
        """
        print typeCode


def beginTransaction(database=None, isolationLevel=None, timeout=None):
    """Begins a new database transaction. Database transactions are used to execute multiple queries
    in an atomic fashion. After executing queries, you must either commit the transaction to have
    your changes take effect, or rollback the transaction which will make all operations since the
    last commit not take place. The transaction is given a new unique string code, which is then
    returned. You can then use this code  as the tx argument for other system.db.* function calls to
    execute various types of queries using this transaction.

    An open transaction consumes one database connection until it is closed. Because leaving
    connections open indefinitely would exhaust the connection pool, each transaction is given a
    timeout. Each time the transaction is used, the timeout timer is reset. For example, if you make
    a transaction with a timeout of one minute, you must use that transaction at least once a
    minute. If a transaction is detected to have timed out, it will be automatically closed and its
    transaction id will no longer be valid.

    Args:
        database (str): The name of the database connection to create a transaction in.
            Use "" for the project's default connection. Optional.
        isolationLevel (int): The transaction isolation level to use. Use one of the four
            constants: system.db.READ_COMMITTED, system.db.READ_UNCOMMITTED,
            system.db.REPEATABLE_READ, or system.db.SERIALIZABLE. Optional.
        timeout (long): The amount of time, in milliseconds, that this connection is
            allowed to remain open without being used. Timeout counter is reset any time a query or
            call is executed against the transaction, or when committed or rolled-back. Optional.

    Returns:
        str: The new transaction ID. You'll use this ID as the "tx" argument for all other calls to
            have them execute against this transaction.
    """
    print(database, isolationLevel, timeout)
    return 'transaction_id'


def closeTransaction(tx):
    """Closes the transaction with the given ID. Note that you must commit or rollback the
    transaction before you close it. Closing the transaction will return its database connection to
    the pool. The transaction ID will no longer be valid.

    Args:
        tx (str): The transaction ID.
    """
    print tx


def commitTransaction(tx):
    """Performs a commit for the given transaction. This will make all statements executed against
    the transaction since its beginning or since the last commit or rollback take effect in the
    database. Until you commit a transaction, any changes that the transaction makes will not be
    visible to other connections. Note that if you are done with the transaction, you must close it
    after you commit it.

    Args:
        tx (str): The transaction ID.
    """
    print tx


def createSProcCall(procedureName, database=None, tx=None, skipAudit=None):
    """Creates an SProcCall object, which is a stored procedure call context.

    Args:
        procedureName (str): The named of the stored procedure to call.
        database (str): The name of the database connection to execute against. If omitted or "",
            the project's default database connection will be used. Optional.
        tx (str): A transaction identifier. If omitted, the call will be executed in its own
            transaction. Optional.
        skipAudit (bool): A flag which, if set to true, will cause the procedure call to skip the
            audit system. Useful for some queries that have fields which won't fit into the audit
            log. Optional.

    Returns:
        SProcCall: A stored procedure call context, which can be configured and then used as the
            argument to system.db.execSProcCall.
    """
    print(procedureName, database, tx, skipAudit)
    return SProcCall()


def execSProcCall(callContext):
    """Executes a stored procedure call. The one parameter to this function is an SProcCall - a
    stored procedure call context. See the description of system.db.createSProcCall for more
    information and examples.

    Args:
        callContext (SProcCall): A stored procedure call context, with any input, output, and/or
            return value parameters correctly configured. Use system.db.createSProcCall to create a
            call context.
    """
    print callContext


def rollbackTransaction(tx):
    """Performs a rollback on the given connection. This will make all statements executed against
    this transaction since its beginning or since the last commit  or rollback undone. Note that
    if you are done with the transaction, you must also close it after you do a rollback on it.

    Args:
        tx (str): The transaction ID.
    """
    print tx
