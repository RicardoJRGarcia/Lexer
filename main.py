# main.py
import sys
import os
import importlib
from antlr4 import InputStream, CommonTokenStream, Token
from antlr4.error.ErrorListener import ErrorListener

DEFAULT_TEST_FILE = "tests/valid/programa2.txt"

def load_antlr_modules():
    LexerCls = ParserCls = None
    try:
        import TextToBinLexer as _lex
        importlib.reload(_lex)
        LexerCls = _lex.TextToBinLexer
    except Exception:
        LexerCls = None
    try:
        import TextToBinParser as _par
        importlib.reload(_par)
        ParserCls = _par.TextToBinParser
    except Exception:
        ParserCls = None
    return LexerCls, ParserCls

class ParserErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append((line, column, msg))

def token_name_safe(lexer, token):
    if lexer is None:
        return None
    names = lexer.symbolicNames
    ttype = token.type
    if ttype is None:
        return "UNKNOWN"
    if 0 <= ttype < len(names) and names[ttype] is not None:
        return names[ttype]
    if ttype == Token.EOF:
        return "EOF"
    return "UNKNOWN"

def text_to_binary_lines(text):
    lines = text.splitlines()
    binary_lines = []
    for line in lines:
        if line == "":
            binary_lines.append("")
            continue
        bytes_seq = line.encode('utf-8')
        binary_lines.append(' '.join(format(b, '08b') for b in bytes_seq))
    if text.endswith('\n'):
        binary_lines.append("")
    return binary_lines

def print_binary(text):
    print("\n===Binario===")
    for i, bline in enumerate(text_to_binary_lines(text), start=1):
        print(f"Line {i}: {bline}")

def is_operator_name(name):
    return name in {"PLUS","MINUS","MUL","DIV","MOD","EQ","NEQ","GE","LE","GT","LT","ASSIGN"}

def analyze(path, LexerCls, ParserCls):
    if not os.path.exists(path):
        print(f"Input file not found: {path}")
        return

    with open(path, encoding='utf-8') as f:
        raw_text = f.read()

    if LexerCls is None:
        print("Error: TextToBinLexer no está disponible. Genera los archivos ANTLR.")
        print_binary(raw_text)
        return

    lexer = LexerCls(InputStream(raw_text))
    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = [t for t in stream.tokens if t.type != Token.EOF]

    # Imprimir tokens
    print("\nTokens")
    for token in tokens:
        name = token_name_safe(lexer, token)
        print(f"{token.line}:{token.column} -> ({name}, \"{token.text}\")")

    # Detecciones léxicas básicas
    lexical_errors = []
    for token in tokens:
        name = token_name_safe(lexer, token)
        if name == "INVALID_OP":
            lexical_errors.append((token.line, token.column, token.text, "Invalid operator sequence"))
        elif name == "INVALID_ID":
            lexical_errors.append((token.line, token.column, token.text, "Invalid identifier"))
        elif name == "UNKNOWN":
            lexical_errors.append((token.line, token.column, token.text, "Unknown symbol"))


    for i in range(len(tokens)-1):
        a, b = tokens[i], tokens[i+1]
        an = token_name_safe(lexer, a)
        bn = token_name_safe(lexer, b)
        if an == "NUMBER" and bn == "IDENTIFIER" and a.line == b.line:
            lexical_errors.append((a.line, a.column, a.text + b.text, "Invalid identifier starting with digit"))

    # Detector de operadores repetidos
    i = 0
    while i < len(tokens) - 1:
        cur = tokens[i]
        cur_name = token_name_safe(lexer, cur)
        if is_operator_name(cur_name):
            run_start = i
            run_line = cur.line
            j = i + 1
            while j < len(tokens):
                nxt = tokens[j]
                nxt_name = token_name_safe(lexer, nxt)
                if nxt.line != run_line:
                    break
                if is_operator_name(nxt_name):
                    j += 1
                else:
                    break
            run_len = j - run_start
            if run_len > 1:
                second_op = tokens[run_start + 1]
                lexical_errors.append((
                    second_op.line,
                    second_op.column,
                    ''.join(t.text for t in tokens[run_start:run_start+run_len]),
                    "Consecutive operators not allowed"
                ))
            i = j
        else:
            i += 1

    stack = []
    for t in tokens:
        tn = token_name_safe(lexer, t)
        if tn == "LPAREN":
            stack.append((t.line, t.column))
        elif tn == "RPAREN":
            if stack:
                stack.pop()
            else:
                lexical_errors.append((t.line, t.column, t.text, "Unmatched closing parenthesis"))
    if stack:
        ln, col = stack[-1]
        lexical_errors.append((ln, col, "(", "Unmatched opening parenthesis"))

    # Si hay errores léxicos, imprimir y salir
    if lexical_errors:
        print("\nError List")
        for l, c, txt, kind in lexical_errors:
            print(f"Line {l}, Column {c}: {kind} '{txt}'")
        print_binary(raw_text)
        return

    # Parseo
    if ParserCls is None:
        print("\nWarning: TextToBinParser no está disponible. Solo análisis léxico realizado.")
        print_binary(raw_text)
        return

    parser = ParserCls(stream)
    parser.removeErrorListeners()
    perr = ParserErrorListener()
    parser.addErrorListener(perr)

    try:
        parser.program()
    except Exception as e:
        perr.errors.append((0, 0, f"Parser runtime exception: {e}"))

    if perr.errors:
        print("\n=== Parser Errors ===")
        for l, c, m in perr.errors:
            print(f"Line {l}, Column {c}: {m}")
    else:
        print("\n=== Parse OK ===")

    print_binary(raw_text)

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TEST_FILE
    LexerCls, ParserCls = load_antlr_modules()
    analyze(input_path, LexerCls, ParserCls)

if __name__ == "__main__":
    main()














