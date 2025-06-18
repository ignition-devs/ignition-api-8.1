from typing import List

from org.apache.poi.ss.formula import OperationEvaluationContext
from org.apache.poi.ss.formula.eval import ValueEval

class FreeRefFunction:
    def evaluate(
        self, args: List[ValueEval], ec: OperationEvaluationContext
    ) -> ValueEval: ...

class Function:
    def evaluate(
        self, args: List[ValueEval], srcRowIndex: int, srcColumnIndex: int
    ) -> ValueEval: ...
