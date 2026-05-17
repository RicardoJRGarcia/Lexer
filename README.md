Lexer - Analizador Lexico

El objetivo de este proyecto es generar la conciencia de lo que sucede detras de la pantalla y a un nivel en el que una persona normal no puede comprender
que esta sucediendo y en base a eso tener una mejor comprensión a nivel máquina de las operaciones y los procesos que lleva la misma.

Materia: Sistemas de Base 1
Universidad Autonoma de Tamaulipas 
Facultad de Ingenieria Tampico
Semestre 2026-1
Profesor Dante Adolfo Muñoz Quintero

Integrantes
Rosales Garcia Ricardo Javier 2183330159

La representación binaria del código procesado por este proyecto responde a una necesidad práctica: 
todo dato que circula por redes de comunicación se transmite finalmente como secuencias de bits y busca generar conocimiento de cómo se llega a ese proceso.

Tokens

IF : 'if' ; palabra reservada inicio de sentencia condicional
THEN : 'then' ; palabra reservada separador de condición y asignación
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ; nombre de variable válido
NUMBER : [0-9]+(\.[0-9]+)? ; literal numérico entero o decimal
ASSIGN : '=' ; operador de asignación
DELIMITER : ';' ; final de sentencia

PLUS : '+' ; suma
MINUS : '-' ; resta / unario -
MUL : '*' ; multiplicación
DIV : '/' ; división
MOD : '%' ; módulo

EQ : '==' ; igualdad
NEQ : '!=' ; desigualdad 
GE : '>=' ; mayor o igual
LE : '<=' ; menor o igual
GT : '>' ; mayor que
LT : '<' ; menor que

LPAREN : '(' ; paréntesis izquierdo
RPAREN : ')' ; paréntesis derecho

UNKNOWN : . ; cualquier símbolo no reconocido (error léxico)

Se puede ejecutar desde la consola como desde un compilador como Pycharm
Si se busca ejecutar desde la consola, se requiere el siguiente formato:

python main.py tests/invalid/errores1.txt

Las direcciones dependen de lo que se busque ejecutar si quieres ejecutar otro directiorio se puede modificar de la siguiente forma

python main.py tests/valid/programa1.txt

y si no se puede ejecutar desde el main.py dentro de Pycharm en la parte superior del código puedes seleccionar el archivo que deseas ejecutar ejemplo:

DEFAULT_TEST_FILE = "tests/valid/programa2.txt"

Ejemplo de entrada y salida esperada

if x + y * (z - 2) >= 100 then result = x * y + z / 2;
if (a - 3) * (b + 4) < c + 10 then out = (a + b) * (c - 1);

Tokens
1:0 -> (IF, "if")
1:3 -> (IDENTIFIER, "x")
1:5 -> (PLUS, "+")
1:7 -> (IDENTIFIER, "y")
1:9 -> (MUL, "*")
1:11 -> (LPAREN, "(")
1:12 -> (IDENTIFIER, "z")
1:14 -> (MINUS, "-")
1:16 -> (NUMBER, "2")
1:17 -> (RPAREN, ")")
1:19 -> (GE, ">=")
1:22 -> (NUMBER, "100")
1:26 -> (THEN, "then")
1:31 -> (IDENTIFIER, "result")
1:38 -> (ASSIGN, "=")
1:40 -> (IDENTIFIER, "x")
1:42 -> (MUL, "*")
1:44 -> (IDENTIFIER, "y")
1:46 -> (PLUS, "+")
1:48 -> (IDENTIFIER, "z")
1:50 -> (DIV, "/")
1:52 -> (NUMBER, "2")
1:53 -> (DELIMITER, ";")
2:0 -> (IF, "if")
2:3 -> (LPAREN, "(")
2:4 -> (IDENTIFIER, "a")
2:6 -> (MINUS, "-")
2:8 -> (NUMBER, "3")
2:9 -> (RPAREN, ")")
2:11 -> (MUL, "*")
2:13 -> (LPAREN, "(")
2:14 -> (IDENTIFIER, "b")
2:16 -> (PLUS, "+")
2:18 -> (NUMBER, "4")
2:19 -> (RPAREN, ")")
2:21 -> (LT, "<")
2:23 -> (IDENTIFIER, "c")
2:25 -> (PLUS, "+")
2:27 -> (NUMBER, "10")
2:30 -> (THEN, "then")
2:35 -> (IDENTIFIER, "out")
2:39 -> (ASSIGN, "=")
2:41 -> (LPAREN, "(")
2:42 -> (IDENTIFIER, "a")
2:44 -> (PLUS, "+")
2:46 -> (IDENTIFIER, "b")
2:47 -> (RPAREN, ")")
2:49 -> (MUL, "*")
2:51 -> (LPAREN, "(")
2:52 -> (IDENTIFIER, "c")
2:54 -> (MINUS, "-")
2:56 -> (NUMBER, "1")
2:57 -> (RPAREN, ")")
2:58 -> (DELIMITER, ";")

Line 1: 01101001 01100110 00100000 01111000 00100000 00101011 00100000 01111001 00100000 00101010 00100000 00101000 01111010 00100000 00101101 00100000 00110010 00101001 00100000 0
0111110 00111101 00100000 00110001 00110000 00110000 00100000 01110100 01101000 01100101 01101110 00100000 01110010 01100101 01110011 01110101 01101100 01110100 00100000 00111101 00100000 01111000 00100000 00101010 00100000 01111001 00100000 00101011 00100000 01111010 00100000 00101111 00100000 00110010 00111011
Line 2: 01101001 01100110 00100000 00101000 01100001 00100000 00101101 00100000 00110011 00101001 00100000 00101010 00100000 00101000 01100010 00100000 00101011 00100000 00110100 0
0101001 00100000 00111100 00100000 01100011 00100000 00101011 00100000 00110001 00110000 00100000 01110100 01101000 01100101 01101110 00100000 01101111 01110101 01110100 00100000 00111101 00100000 00101000 01100001 00100000 00101011 00100000 01100010 00101001 00100000 00101010 00100000 00101000 01100011 00100000 00101101 00100000 00110001 00101001 00111011 
