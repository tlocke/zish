// Zish ANTLR v4 Grammar

grammar Zish;

// note that EOF is a concept for the grammar, technically Zish streams
// are infinite
start
    : element EOF
    ;

element
    : key
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

set_type
    : SET_START key (COMMA key)* SET_FINISH
    | SET_START SET_FINISH
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
    : key COLON element
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
    | set_type
    | list_type
    ;

WS
    : ( SPACE+ | INLINE_COMMENT | BLOCK_COMMENT ) -> skip;

fragment
INLINE_COMMENT
    : '//' .*? (NL | EOF)
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
    : '"' (COMMON_ESCAPE | UNICODE_ESCAPE | STRING_TEXT_ALLOWED)*? '"'
    ;

// non-control Unicode (newlines are OK)
fragment
STRING_TEXT_ALLOWED
    : ~[\u0000\u0001\u0002\u0003\u0004\u0005\u0006\u0007\u0008\u000E\u000F\u0010\u0011\u0012\u0013\u0014\u0015\u0016\u0017\u0018\u0019\u001A\u001B\u001C\u001D\u001E\u001F\u005C]
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
SPACE
    : '\u0009' // tab
    | '\u000A' // line feed
    | '\u000B' // vertical tab
    | '\u000C' // form feed
    | '\u000D' // carriage return
    | '\u0020' // space
    ;

fragment
NL
    : '\u000D\u000A'  // carriage return + line feed
    | '\u000D'        // carriage return
    | '\u000A'        // line feed
    ;
