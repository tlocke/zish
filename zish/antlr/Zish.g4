// Zish ANTLR v4 Grammar

grammar Zish;

// note that EOF is a concept for the grammar, technically Zish streams
// are infinite
start
    : ws* element (ws+ element)* ws* EOF
    ;

element
    : key
    | map_type
    ;

list_type
    : LIST_START ws* element (ws* COMMA ws* element)* ws* LIST_FINISH
    | LIST_START ws* LIST_FINISH
    ;

LIST_START
    : '['
    ;

LIST_FINISH
    : ']'
    ;

set_type
    : SET_START ws* key (ws* COMMA ws* key)* ws* SET_FINISH
    | SET_START ws* SET_FINISH
    ;

SET_START
    : '('
    ;

SET_FINISH
    : ')'
    ;

COMMA
    : ','
    ;

map_type
    : MAP_START ws* pair (ws* COMMA ws* pair)* ws* MAP_FINISH
    | MAP_START ws* MAP_FINISH
    ;

MAP_START
    : '{'
    ;

MAP_FINISH
    : '}'
    ;

pair
    : key ws* COLON ws* element
    ;

COLON
    : ':'
    ;

key
    : BOOL
    | NULL
    | TIMESTAMP
    | INTEGER
    | FLOAT
    | DECIMAL
    | STRING
    | BLOB
    | list_type
    | set_type
    ;

ws
    : WHITESPACE
    | INLINE_COMMENT
    | BLOCK_COMMENT
    ;

WHITESPACE
    : WS+
    ;

INLINE_COMMENT
    : '//' .*? (NL | EOF)
    ;

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
    : '-'? UNSIGNED_INTEGER
    ;

UNSIGNED_INTEGER
    : '0'
    | [1-9] DIGIT*
    ;

FLOAT
    : INTEGER FRAC? FLOAT_EXP
    | PLUS_OR_MINUS 'inf'
    | 'nan'
    ;

fragment
FLOAT_EXP
    : 'e' PLUS_OR_MINUS? DIGIT+
    ;

DECIMAL
    : INTEGER FRAC? DECIMAL_EXP?
    ;

fragment
DECIMAL_EXP
    : 'd' PLUS_OR_MINUS? DIGIT+
    ;

STRING
    : '"' (COMMON_ESCAPE | UNICODE_ESCAPE | STRING_TEXT_ALLOWED)*? '"'
    ;

// non-control Unicode (newlines are OK)
fragment
STRING_TEXT_ALLOWED
    : ~[\u0000\u0001\u0002\u0003\u0004\u0005\u0006\u0007\u0008\u000E\u000F\u0010\u0011\u0012\u0013\u0014\u0015\u0016\u0017\u0018\u0019\u001A\u001B\u001C\u001D\u001E\u001F\u005C]
    ;

BLOB
    : '\'' (BASE_64_QUARTET | WS)* BASE_64_PAD? WS* '\''
    ;

fragment
BASE_64_PAD
    : BASE_64_PAD1
    | BASE_64_PAD2
    ;

fragment
BASE_64_QUARTET
    : BASE_64_CHAR WS* BASE_64_CHAR WS* BASE_64_CHAR WS* BASE_64_CHAR
    ;

fragment
BASE_64_PAD1
    : BASE_64_CHAR WS* BASE_64_CHAR WS* BASE_64_CHAR WS* '='
    ;

fragment
BASE_64_PAD2
    : BASE_64_CHAR WS* BASE_64_CHAR WS* '=' WS* '='
    ;

fragment
BASE_64_CHAR
    : [0-9a-zA-Z+/]
    ;

fragment
FRAC
    : '.'
    | '.' DIGIT (UNDERSCORE? DIGIT)*
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
    | NL
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
WS
    : WS_NOT_NL
    | '\u000A' // line feed
    | '\u000D' // carriage return
    ;

fragment
NL
    : '\u000D\u000A'  // carriage return + line feed
    | '\u000D'        // carriage return
    | '\u000A'        // line feed
    ;

fragment
WS_NOT_NL
    : '\u0009' // tab
    | '\u000B' // vertical tab
    | '\u000C' // form feed
    | '\u0020' // space
    ;

fragment
UNDERSCORE
    : '_'
    ;
