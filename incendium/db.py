# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Database module."""

__all__ = [
    'execute_sp'
]

import system.db


class Result(object):
    """Result class."""

    def __init__(self,
                 output_params=None,
                 result_set=None,
                 return_value=None,
                 update_count=None):
        """Result object initializer.

        Args:
            output_params (dict): All registered output parameters.
            result_set (Dataset): The dataset that is the resulting data of the stored procedure,
                if any.
            return_value (int): The return value, if registerReturnParam had been called.
            update_count (int): The number of rows modified by the stored procedure, or -1 if not
                applicable.
        """
        self.output_params = output_params
        self.result_set = result_set
        self.return_value = return_value
        self.update_count = update_count


def execute_sp(stored_procedure, database='', transaction=None, skip_audit=False, in_params=None,
               out_params=None, return_type_code=None, get_output_params=False,
               get_result_set=False, get_return_value=False, get_update_count=False):
    """Executes a database stored procedure.

    Args:
        stored_procedure (str): The name of the stored procedure to call.
        database (str): The name of the database connection to execute against. If
            omitted or "", the project's default database connection will be used. Optional.
        transaction (str): A transaction identifier. If omitted, the call will be executed
            in its own transaction. Optional.
        skip_audit (bool): A flag which, if set to true, will cause the procedure call to
            skip the audit system. Useful for some queries that have fields which won't fit into
            the audit log. Optional.
        in_params (dict): A Dictionary containing INPUT parameters. Optional.
        out_params (dict): A Dictionary containing OUTPUT parameters. Optional.
        return_type_code (int): The return value Type Code. Optional.
        get_output_params (bool): A flag indicating whether or not to return OUTPUT
            parameters after execution. Optional.
        get_result_set (bool): A flag indicating whether or not to return a dataset that
            is the resulting data of the stored procedure, if any. Optional.
        get_return_value (bool): A flag indicating whether or not to return the return
            value of the stored procedure Call. Optional.
        get_update_count (bool): A flag indicating whether or not to return the number of
            rows modified by the stored procedure, or -1 if not applicable. Optional.

    Returns:
        Result: Result object.
    """
    # Initialize variables.
    _out_params = {}
    _result = Result()

    call = system.db.createSProcCall(procedureName=stored_procedure,
                                     database=database,
                                     tx=transaction,
                                     skipAudit=skip_audit)

    # Register INPUT Parameters
    if in_params:
        for in_param in in_params:
            call.registerInParam(in_param, in_params[in_param][0], in_params[in_param][1])

    # Register OUTPUT Parameters
    if out_params:
        for out_param in out_params:
            call.registerOutParam(out_param, out_params[out_param])

    # Register RETURN Parameter
    if get_return_value:
        call.registerReturnParam(return_type_code)

    # Execute the call
    system.db.execSProcCall(call)

    if out_params:
        for out_param in out_params:
            _out_params[out_param] = call.getOutParamValue(out_param)

    if get_output_params:
        _result.output_params = _out_params

    if get_result_set:
        _result.result_set = call.getResultSet()

    if get_return_value:
        _result.return_value = call.getReturnValue()

    if get_update_count:
        _result.update_count = call.getUpdateCount()

    return _result
