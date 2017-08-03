// Zish ANTLR v4 Grammar

grammar Zish;

// note that EOF is a concept for the grammar, technically Zish streams
// are infinite
start
    : (ws* element)* ws* EOF
    ;

element
    : key
    | map_type
    ;

list_type
    : '[' ws* element (ws* ',' ws* element)* ws* ']'
    | '[' ws* ']' 
    ;

set_type
    : '(' ws* key (ws* ',' ws* key)* ws* ')'
    | '(' ws* ')' 
    ;

map_type
    : '{' ws* pair (ws* ',' ws* pair)* ws* '}'
    | '{' ws* '}'
    ;

pair
    : key ws* ':' ws* element
    ;

key
    : BOOL
    | NULL
    | BIN_INTEGER
    | DEC_INTEGER
    | HEX_INTEGER
    | TIMESTAMP
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


//////////////////////////////////////////////////////////////////////////////
// Whitespace / Comments
//////////////////////////////////////////////////////////////////////////////

WHITESPACE
    : WS+
    ;

INLINE_COMMENT
    : '//' .*? (NL | EOF)
    ;

BLOCK_COMMENT
    : '/*' .*? '*/'
    ;

//////////////////////////////////////////////////////////////////////////////
// Null
//////////////////////////////////////////////////////////////////////////////

NULL
    : 'null'
    ;


//////////////////////////////////////////////////////////////////////////////
// Bool
//////////////////////////////////////////////////////////////////////////////

BOOL
    : 'true'
    | 'false'
    ;

//////////////////////////////////////////////////////////////////////////////
// Timestamp
//////////////////////////////////////////////////////////////////////////////

TIMESTAMP
    : DATE ('T' TIME?)?
    | YEAR '-' MONTH 'T'
    | YEAR 'T'
    ;

fragment
DATE
    : YEAR '-' MONTH '-' DAY
    ;

fragment
YEAR
    : '000'                     [1-9]
    | '00'            [1-9]     DEC_DIGIT
    | '0'   [1-9]     DEC_DIGIT DEC_DIGIT
    | [1-9] DEC_DIGIT DEC_DIGIT DEC_DIGIT
    ;

fragment
MONTH
    : '0' [1-9]
    | '1' [0-2]
    ;

fragment
DAY
    : '0'   [1-9]
    | [1-2] DEC_DIGIT
    | '3'   [0-1]
    ;

fragment
TIME
    : HOUR ':' MINUTE (':' SECOND)? OFFSET
    ;

fragment
OFFSET
    : 'Z'
    | PLUS_OR_MINUS HOUR ':' MINUTE
    ;

fragment
HOUR
    : [01] DEC_DIGIT
    | '2' [0-3]
    ;

fragment
MINUTE
    : [0-5] DEC_DIGIT
    ;

// note that W3C spec requires a digit after the '.'
fragment
SECOND
    : [0-5] DEC_DIGIT ('.' DEC_DIGIT+)?
    ;

//////////////////////////////////////////////////////////////////////////////
// Int
//////////////////////////////////////////////////////////////////////////////

BIN_INTEGER
    : '-'? '0' [bB] BINARY_DIGIT (UNDERSCORE? BINARY_DIGIT)*
    ;

DEC_INTEGER
    : '-'? DEC_UNSIGNED_INTEGER
    ;

HEX_INTEGER
    : '-'? '0' [xX] HEX_DIGIT (UNDERSCORE? HEX_DIGIT)*
    ;

//////////////////////////////////////////////////////////////////////////////
// Float
//////////////////////////////////////////////////////////////////////////////

SPECIAL_FLOAT
    : PLUS_OR_MINUS 'inf'
    | 'nan'
    ;

FLOAT
    : DEC_INTEGER DEC_FRAC? FLOAT_EXP
    ;

fragment
FLOAT_EXP
    : [Ee] PLUS_OR_MINUS? DEC_DIGIT+
    ;

//////////////////////////////////////////////////////////////////////////////
// Decimal
//////////////////////////////////////////////////////////////////////////////

DECIMAL
    : DEC_INTEGER DEC_FRAC? DECIMAL_EXP?
    ;

fragment
DECIMAL_EXP
    : [Dd] PLUS_OR_MINUS? DEC_DIGIT+
    ;


//////////////////////////////////////////////////////////////////////////////
// String
//////////////////////////////////////////////////////////////////////////////

STRING
    : '"' STRING_TEXT '"'
    ;

fragment
STRING_TEXT
    : (TEXT_ESCAPE | STRING_TEXT_ALLOWED)*?
    ;

// non-control Unicode (newlines are OK)
fragment
STRING_TEXT_ALLOWED
    : ~[\u0000\u0001\u0002\u0003\u0004\u0005\u0006\u0007\u0008\u000E\u000F\u0010\u0011\u0012\u0013\u0014\u0015\u0016\u0017\u0018\u0019\u001A\u001B\u001C\u001D\u001E\u001F\u005C]
    ;

fragment
TEXT_ESCAPE
    : COMMON_ESCAPE | HEX_ESCAPE | UNICODE_ESCAPE
    ;

//////////////////////////////////////////////////////////////////////////////
// BLOB
//////////////////////////////////////////////////////////////////////////////

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

//////////////////////////////////////////////////////////////////////////////
// Common Lexer Primitives
//////////////////////////////////////////////////////////////////////////////


// Zish does not allow leading zeros for base-10 numbers
fragment
DEC_UNSIGNED_INTEGER
    : '0'
    | [1-9] (UNDERSCORE? DEC_DIGIT)*
    ;

fragment
DEC_FRAC
    : '.'
    | '.' DEC_DIGIT (UNDERSCORE? DEC_DIGIT)*
    ;

fragment
DEC_DIGIT
    : [0-9]
    ;

fragment
HEX_DIGIT
    : [0-9a-fA-F]
    ;

fragment
BINARY_DIGIT
    : [01]
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
    | '?'
    | '0'
    | '\''
    | '"'
    | '/'
    | '\\'
    | NL
    ;

fragment
HEX_ESCAPE
    : '\\x' HEX_DIGIT HEX_DIGIT
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
