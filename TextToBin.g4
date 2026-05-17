grammar TextToBin;

program : statement* EOF ;

statement
    : IF expr THEN IDENTIFIER ASSIGN expr DELIMITER
    ;

expr
    : relationalExpr
    ;

relationalExpr
    : additiveExpr ( (GT | LT | GE | LE | EQ | NEQ) additiveExpr )?
    ;

additiveExpr
    : multiplicativeExpr ( (PLUS | MINUS) multiplicativeExpr )*
    ;

multiplicativeExpr
    : unaryExpr ( (MUL | DIV | MOD) unaryExpr )*
    ;

unaryExpr
    : MINUS unaryExpr
    | primary
    ;

primary
    : NUMBER
    | IDENTIFIER
    | LPAREN expr RPAREN
    ;

// LEXER
IF        : 'if' ;
THEN      : 'then' ;
ASSIGN    : '=' ;
DELIMITER : ';' ;


INVALID_OP : '++' | '--' | '&&' | '||' | '**' ;

// Comparadores
EQ      : '==' ;
NEQ     : '!=' | '!' [ \t\r\n]* '=' ;
GE      : '>=' ;
LE      : '<=' ;
GT      : '>' ;
LT      : '<' ;

// Operadores
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
MOD     : '%' ;

// Paréntesis
LPAREN  : '(' ;
RPAREN  : ')' ;

// Identificadores y números
INVALID_ID : [0-9]+ [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER  : [0-9]+ ('.' [0-9]+)? ;
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ;

// Espacios y comentarios
WS : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;

// Cualquier otro símbolo
UNKNOWN : . ;













