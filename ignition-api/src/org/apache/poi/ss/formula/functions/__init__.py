from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from org.apache.poi.ss.formula import OperationEvaluationContext
    from org.apache.poi.ss.formula.eval import ValueEval


class FreeRefFunction(object):
    def evaluate(
        self,
        args,  # type: List[ValueEval]
        ec,  # type: OperationEvaluationContext
    ):
        # type: (...) -> ValueEval
        raise NotImplementedError


class Function(object):
    def evaluate(self, args, srcRowIndex, srcColumnIndex):
        # type: (List[ValueEval], int, int) -> ValueEval
        raise NotImplementedError
