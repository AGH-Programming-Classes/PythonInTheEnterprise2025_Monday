import ast, operator, math, sys

_ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

_funcs = {k: getattr(math, k) for k in (
    "sin","cos","tan","asin","acos","atan","sqrt","log","log10","exp",
    "fabs","factorial","degrees","radians","ceil","floor","gamma","lgamma"
)}
_consts = {"pi": math.pi, "e": math.e, "tau": math.tau, "inf": math.inf}

def _eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ops:
        return _ops[type(node.op)](_eval(node.operand))
    if isinstance(node, ast.BinOp) and type(node.op) in _ops:
        return _ops[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.keywords == []:
        fname = node.func.id
        if fname in _funcs:
            return _funcs[fname](*[_eval(a) for a in node.args])
    if isinstance(node, ast.Name) and node.id in _consts:
        return _consts[node.id]
    raise ValueError("invalid expression")

def calculate(expr):
    tree = ast.parse(expr, mode="eval")
    return _eval(tree.body)

def main():
    if len(sys.argv) > 1:
        print(calculate(" ".join(sys.argv[1:])))
        return
    while True:
        try:
            s = input("> ").strip()
            if s.lower() in {"exit","quit"}:
                break
            if not s:
                continue
            print(calculate(s))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
