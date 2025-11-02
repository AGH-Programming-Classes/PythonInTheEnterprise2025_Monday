import ast, operator, math, sys

_MAX_EXPR_LEN = 2000
_MAX_AST_DEPTH = 64
_MAX_INT_BITS = 1_000_000
_MAX_INT_EXP = 10_000
_MAX_FLOAT_EXP = 1_000
_ALLOW_COMPLEX = False

_total_ops = 0
_success_ops = 0

def _ast_depth(node, d=0):
    return max([d] + [_ast_depth(c, d+1) for c in ast.iter_child_nodes(node)])

def _assert_numeric_limits(x):
    if isinstance(x, bool):
        raise ValueError("invalid expression")
    if isinstance(x, int):
        if x.bit_length() > _MAX_INT_BITS:
            raise OverflowError("integer too large")
    elif isinstance(x, float):
        pass
    elif isinstance(x, complex):
        if not _ALLOW_COMPLEX:
            raise ValueError("complex results are not supported")
    else:
        raise ValueError("invalid expression")
    return x

def _safe_pow(a, b):
    if (isinstance(a, complex) or isinstance(b, complex)) and not _ALLOW_COMPLEX:
        raise ValueError("complex results are not supported")
    if isinstance(b, int):
        if abs(b) > _MAX_INT_EXP:
            raise OverflowError("exponent too large")
    elif isinstance(b, float):
        if abs(b) > _MAX_FLOAT_EXP:
            raise OverflowError("exponent too large")
    r = operator.pow(a, b)
    return _assert_numeric_limits(r)

def _safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return operator.truediv(a, b)

def _safe_floordiv(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return operator.floordiv(a, b)

def _safe_mod(a, b):
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return operator.mod(a, b)

_SCIENTIFIC_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: _safe_div,
    ast.FloorDiv: _safe_floordiv,
    ast.Mod: _safe_mod,
    ast.Pow: _safe_pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

_SCIENTIFIC_FUNCS = {k: getattr(math, k) for k in (
    "sin","cos","tan","asin","acos","atan","sqrt","log","log10","exp",
    "fabs","factorial","degrees","radians","ceil","floor","gamma","lgamma"
)}
_SCIENTIFIC_CONSTS = {"pi": math.pi, "e": math.e, "tau": math.tau, "inf": math.inf, "nan": math.nan}

_SIMPLE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: _safe_div,
}
_SIMPLE_FUNCS = {}
_SIMPLE_CONSTS = {}

_ALLOWED_AST_NODES = (
    ast.Expression, ast.Constant,
    ast.UnaryOp, ast.BinOp,
    ast.Call, ast.Name, ast.Load,
    ast.operator, ast.unaryop,
)

def _validate_ast(tree):
    for node in ast.walk(tree):
        if not isinstance(node, _ALLOWED_AST_NODES):
            raise ValueError("invalid expression")
    if _ast_depth(tree) > _MAX_AST_DEPTH:
        raise ValueError("expression too deep")

def _eval(node, ops, funcs, consts, last_result):
    global _success_ops, _total_ops
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return _assert_numeric_limits(node.value)
    if isinstance(node, ast.UnaryOp) and type(node.op) in ops:
        _total_ops += 1
        v = _eval(node.operand, ops, funcs, consts, last_result)
        r = _assert_numeric_limits(ops[type(node.op)](v))
        _success_ops += 1
        return r
    if isinstance(node, ast.BinOp) and type(node.op) in ops:
        _total_ops += 1
        l = _eval(node.left, ops, funcs, consts, last_result)
        r = _eval(node.right, ops, funcs, consts, last_result)
        r = _assert_numeric_limits(ops[type(node.op)](l, r))
        _success_ops += 1
        return r
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.keywords == []:
        fname = node.func.id
        _total_ops += 1
        if fname in funcs:
            args = [_eval(a, ops, funcs, consts, last_result) for a in node.args]
            if fname == "factorial":
                if not (len(args) == 1 and isinstance(args[0], int) and 0 <= args[0] <= 100000):
                    raise OverflowError("factorial argument out of allowed range")
            r = funcs[fname](*args)
            _success_ops += 1
            return _assert_numeric_limits(r)
        raise ValueError("invalid expression")
    if isinstance(node, ast.Name):
        if node.id in consts:
            return _assert_numeric_limits(consts[node.id])
        if node.id == "ans":
            return _assert_numeric_limits(last_result)
    if isinstance(node, (ast.UnaryOp, ast.BinOp, ast.Call)):
        _total_ops += 1
    raise ValueError("invalid expression")

def calculate(expr, ops, funcs, consts, last_result):
    global _total_ops
    if not isinstance(expr, str) or not expr.strip():
        _total_ops += 1
        raise ValueError("invalid expression")
    if len(expr) > _MAX_EXPR_LEN:
        _total_ops += 1
        raise ValueError("expression too long")
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError:
        _total_ops += 1
        raise ValueError("invalid expression")
    try:
        _validate_ast(tree)
    except Exception as e:
        _total_ops += 1
        raise e
    return _eval(tree.body, ops, funcs, consts, last_result)

def _friendly_error(e: Exception) -> str:
    if isinstance(e, ZeroDivisionError):
        return "Division by zero."
    if isinstance(e, OverflowError):
        return str(e) or "Computation too large."
    if isinstance(e, ValueError):
        msg = str(e) or "invalid expression"
        if "math domain error" in msg:
            return "Math domain error (e.g., sqrt of negative, log of non-positive)."
        if "invalid" in msg:
            return "Invalid expression."
        return msg
    if isinstance(e, TypeError):
        return "Invalid argument types or wrong number of arguments."
    return f"Error: {e}"

def main():
    global _total_ops, _success_ops
    mode = input("Choose calculator mode (simple/scientific): ").lower()
    if mode == "simple":
        current_ops = _SIMPLE_OPS; current_funcs = _SIMPLE_FUNCS; current_consts = _SIMPLE_CONSTS
    elif mode == "scientific":
        current_ops = _SCIENTIFIC_OPS; current_funcs = _SCIENTIFIC_FUNCS; current_consts = _SCIENTIFIC_CONSTS
    else:
        print("Invalid mode. Defaulting to scientific.")
        current_ops = _SCIENTIFIC_OPS; current_funcs = _SCIENTIFIC_FUNCS; current_consts = _SCIENTIFIC_CONSTS
    last_result = 0
    if len(sys.argv) > 1:
        try:
            result = calculate(" ".join(sys.argv[1:]), current_ops, current_funcs, current_consts, last_result)
            print(result)
            last_result = result
        except Exception as e:
            print(_friendly_error(e))
        print(f"Done {_success_ops} operations out of {_total_ops}.")
        return
    while True:
        try:
            s = input("> ").strip()
            if s.lower() in {"exit","quit"}:
                break
            if not s:
                continue
            result = calculate(s, current_ops, current_funcs, current_consts, last_result)
            print(result)
            last_result = result
            print(f"Done {_success_ops} operations out of {_total_ops}.")
        except Exception as e:
            print(_friendly_error(e))
            print(f"Done {_success_ops} operations out of {_total_ops}.")

if __name__ == "__main__":
    main()
