import ast
import operator

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def _eval(node):
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.BinOp):
        return OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp):
        return OPS[type(node.op)](_eval(node.operand))
    raise ValueError("Unsupported expression")

def safe_eval_math(expr: str):
    try:
        tree = ast.parse(expr, mode="eval")
        return _eval(tree.body)
    except Exception:
        return None
