class MiniInterpreter:
    def __init__(self):
        self.vars = {}

    def eval_expr(self, expr):
        try:
            return int(expr)
        except:
            return self.vars.get(expr, 0)

    def execute(self, line):
        tokens = line.strip().split()
        if not tokens:
            return None

        if tokens[0] == 'let' and '=' in tokens:
            var = tokens[1]
            eq_idx = tokens.index('=')
            val = self.eval_expr(tokens[eq_idx + 1])
            self.vars[var] = val

        elif tokens[0] == 'if':
            cond_var = tokens[1]
            cond_val = self.eval_expr(tokens[3])
            then_idx = tokens.index('then')
            else_idx = tokens.index('else') if 'else' in tokens else len(tokens)

            if self.vars.get(cond_var, 0) == cond_val:
                stmt = ' '.join(tokens[then_idx + 1:else_idx])
            elif else_idx != len(tokens):
                stmt = ' '.join(tokens[else_idx + 1:])
            else:
                stmt = ''

            if stmt.startswith('let'):
                self.execute(stmt)

def test_mini_interpreter():
    interp = MiniInterpreter()
    commands = [
        "let x = 5",
        "let y = 10",
        "if x == 5 then let z = 1 else let z = 2",
        "if y == 5 then let z = 3 else let z = 4"
    ]
    for cmd in commands:
        interp.execute(cmd)
    print(interp.vars)

if __name__ == "__main__":
    test_mini_interpreter()
