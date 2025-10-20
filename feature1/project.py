import ast, operator, math, sys

_SCIENTIFIC_OPS = {
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

_SCIENTIFIC_FUNCS = {k: getattr(math, k) for k in (
    "sin","cos","tan","asin","acos","atan","sqrt","log","log10","exp",
    "fabs","factorial","degrees","radians","ceil","floor","gamma","lgamma"
)}
_SCIENTIFIC_CONSTS = {"pi": math.pi, "e": math.e, "tau": math.tau, "inf": math.inf}

_SIMPLE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}
_SIMPLE_FUNCS = {}
_SIMPLE_CONSTS = {}

def _eval(node, ops, funcs, consts):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.UnaryOp) and type(node.op) in ops:
        return ops[type(node.op)](_eval(node.operand, ops, funcs, consts))
    if isinstance(node, ast.BinOp) and type(node.op) in ops:
        return ops[type(node.op)](_eval(node.left, ops, funcs, consts), _eval(node.right, ops, funcs, consts))
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.keywords == []:
        fname = node.func.id
        if fname in funcs:
            return funcs[fname](*[_eval(a, ops, funcs, consts) for a in node.args])
    if isinstance(node, ast.Name) and node.id in consts:
        return consts[node.id]
    raise ValueError("invalid expression")

def calculate(expr, ops, funcs, consts):
    tree = ast.parse(expr, mode="eval")
    return _eval(tree.body, ops, funcs, consts)

def main():
    mode = input("Choose calculator mode (simple/scientific): ").lower()
    if mode == "simple":
        current_ops = _SIMPLE_OPS
        current_funcs = _SIMPLE_FUNCS
        current_consts = _SIMPLE_CONSTS
    elif mode == "scientific":
        current_ops = _SCIENTIFIC_OPS
        current_funcs = _SCIENTIFIC_FUNCS
        current_consts = _SCIENTIFIC_CONSTS
    else:
        print("Invalid mode. Defaulting to scientific.")
        current_ops = _SCIENTIFIC_OPS
        current_funcs = _SCIENTIFIC_FUNCS
        current_consts = _SCIENTIFIC_CONSTS

    if len(sys.argv) > 1:
        print(calculate(" ".join(sys.argv[1:]), current_ops, current_funcs, current_consts))
        return
    while True:
        try:
            s = input("> ").strip()
            if s.lower() in {"exit","quit"}:
                break
            if not s:
                continue
            print(calculate(s, current_ops, current_funcs, current_consts))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
