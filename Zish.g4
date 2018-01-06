// Zish ANTLR v4 Grammar

grammar Zish;

start
    : element EOF
    ;

element
    : BOOL
    | NULL
    | TIMESTAMP
    | INTEGER
    | FLOAT
    | DECIMAL
    | STRING
    | BLOB
    | list_type
    | map_type
    ;

list_type
    : LIST_START element (COMMA element)* LIST_FINISH
    | LIST_START LIST_FINISH
    ;

LIST_START
    : '['
    ;

LIST_FINISH
    : ']'
    ;

COMMA
    : ','
    ;

map_type
    : MAP_START pair (COMMA pair)* MAP_FINISH
    | MAP_START MAP_FINISH
    ;

MAP_START
    : '{'
    ;

MAP_FINISH
    : '}'
    ;

pair
    : element COLON element
    ;

COLON
    : ':'
    ;

WS
    : ( SPACE+ | INLINE_COMMENT | BLOCK_COMMENT ) -> skip;

fragment
INLINE_COMMENT
    : '//' .*? (EOL | EOF)
    ;

fragment
BLOCK_COMMENT
    : '/*' .*? '*/'
    ;

NULL
    : 'null'
    ;


BOOL
    : 'true'
    | 'false'
    ;

TIMESTAMP
    : YEAR '-' MONTH '-' DAY [Tt] HOUR ':' MINUTE ':' SECOND OFFSET
    ;

fragment
YEAR
    : DIGIT DIGIT DIGIT DIGIT
    ;

fragment
MONTH
    : '0' [1-9]
    | '1' [0-2]
    ;

fragment
DAY
    : '0'   [1-9]
    | [1-2] DIGIT
    | '3'   [0-1]
    ;

fragment
OFFSET
    : [Zz]
    | PLUS_OR_MINUS HOUR ':' MINUTE
    ;

fragment
HOUR
    : [01] DIGIT
    | '2' [0-3]
    ;

fragment
MINUTE
    : [0-5] DIGIT
    ;

fragment
SECOND
    : [0-5] DIGIT ('.' DIGIT+)?
    ;

INTEGER
    : INT
    ;

DECIMAL
    : INT FRAC? DECIMAL_EXP?
    ;

FLOAT
    : INT FRAC? FLOAT_EXP
    | PLUS_OR_MINUS 'inf'
    | 'nan'
    ;

fragment
INT
    : '-'? ( '0' | [1-9] DIGIT*)
    ;

fragment
FLOAT_EXP
    : 'e' PLUS_OR_MINUS? DIGIT+
    ;

fragment
DECIMAL_EXP
    : 'd' PLUS_OR_MINUS? DIGIT+
    ;

STRING
    : '"' (COMMON_ESCAPE | UNICODE_ESCAPE | ~[\\"])*? '"'
    ;

BLOB
    : '\'' (BASE_64_QUARTET | SPACE)* BASE_64_PAD? SPACE* '\''
    ;

fragment
BASE_64_PAD
    : BASE_64_PAD1
    | BASE_64_PAD2
    ;

fragment
BASE_64_QUARTET
    : BASE_64_CHAR SPACE* BASE_64_CHAR SPACE* BASE_64_CHAR SPACE* BASE_64_CHAR
    ;

fragment
BASE_64_PAD1
    : BASE_64_CHAR SPACE* BASE_64_CHAR SPACE* BASE_64_CHAR SPACE* '='
    ;

fragment
BASE_64_PAD2
    : BASE_64_CHAR SPACE* BASE_64_CHAR SPACE* '=' SPACE* '='
    ;

fragment
BASE_64_CHAR
    : [0-9a-zA-Z+/]
    ;

fragment
FRAC
    : '.' DIGIT*
    ;

fragment
DIGIT
    : [0-9]
    ;

fragment
PLUS_OR_MINUS
    : [+\-]
    ;

fragment
COMMON_ESCAPE
    : '\\' COMMON_ESCAPE_CODE
    ;

fragment
COMMON_ESCAPE_CODE
    : 'a'
    | 'b'
    | 't'
    | 'n'
    | 'f'
    | 'r'
    | 'v'
    | '"'
    | '/'
    | '\\'
    | EOL
    ;

fragment
UNICODE_ESCAPE
    : '\\u'     HEX_DIGIT_QUARTET
    | '\\U000'  HEX_DIGIT_QUARTET HEX_DIGIT 
    | '\\U0010' HEX_DIGIT_QUARTET
    ;

fragment
HEX_DIGIT_QUARTET
    : HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
    ;

fragment
HEX_DIGIT
    : [0-9a-fA-F]
    ;

fragment
SPACE
    : '\u0009' // tab
    | '\u000A' // line feed
    | '\u000B' // vertical tab
    | '\u000C' // form feed
    | '\u000D' // carriage return
    | '\u0020' // space
    ;

fragment
EOL
    : '\u000A' // LF: Line Feed
    | '\u000B' // VT: Vertical Tab
    | '\u000C' // FF: Form Feed
    | '\u000D' // CR: Carriage Return
    | '\u000D\u000A' // CR+LF: CR followed by LF
    | '\u0085' // NEL: Next Line
    | '\u2028' // LS: Line Separator
    | '\u2029' // PS: Paragraph Separator
    ;
