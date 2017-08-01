from antlr4 import CommonTokenStream, InputStream
from antlr4.error import Errors, ErrorListener
from antlr4.tree.Tree import TerminalNodeImpl
from zish.antlr.ZishLexer import ZishLexer
from zish.antlr.ZishParser import ZishParser
import arrow
from decimal import Decimal
from base64 import b64decode, b64encode
from collections.abc import Mapping
from datetime import datetime as Datetime, timezone as Timezone


QUOTE = '"'
UTC_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
TZ_FORMAT = '%Y-%m-%dT%H:%M:%S%z'


class ZishException(Exception):
    pass


class ThrowingErrorListener(ErrorListener.ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Errors.ParseCancellationException(
            "line " + str(line) + ":" + str(column) + " " + msg)


def load(file_like):
    return loads(file_like.read())


def dump(obj, file_like):
    file_like.write(dumps(obj))


def loads(zish_str):
    lexer = ZishLexer(InputStream(zish_str))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())
    stream = CommonTokenStream(lexer)
    parser = ZishParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())

    try:
        tree = parser.start()
    except Errors.ParseCancellationException as e:
        raise ZishException(str(e)) from e

    return parse(tree)


_trans_dec = str.maketrans('dD', 'ee', '_')


def parse(node):
    # print("parse start")
    # print(str(type(node)))
    # print("node text" + node.getText())
    if isinstance(node, ZishParser.Map_typeContext):
        val = {}
        for child in node.getChildren():
            if isinstance(child, ZishParser.PairContext):
                for c in child.getChildren():
                    if isinstance(c, ZishParser.KeyContext):
                        k = parse(c)
                    elif isinstance(c, ZishParser.ElementContext):
                        v = parse(c)
                val[k] = v
        return val
    elif isinstance(node, ZishParser.List_typeContext):
        val = []
        for child in node.getChildren():
            if isinstance(child, ZishParser.ElementContext):
                val.append(parse(child))
        return tuple(val)
    elif isinstance(node, ZishParser.Set_typeContext):
        val = []
        for child in node.getChildren():
            if isinstance(child, ZishParser.KeyContext):
                val.append(parse(child))
        return frozenset(val)
    elif isinstance(
            node, (
                ZishParser.StartContext,
                ZishParser.KeyContext,
                ZishParser.ElementContext)):

        children = []
        for c in node.getChildren():
            if isinstance(c, TerminalNodeImpl) and \
                    c.getPayload().type == ZishParser.EOF:
                continue
            elif isinstance(
                    c, (
                        ZishParser.WsContext)):
                continue

            children.append(c)

        if len(children) == 1:
            return parse(children[0])
        else:
            raise ZishException("Thought there would always be one child.")
    elif isinstance(node, TerminalNodeImpl):
        token = node.getPayload()
        token_type = token.type
        token_text = token.text

        if token_type == ZishParser.TIMESTAMP:
            try:
                return arrow.get(token_text).datetime
            except arrow.parser.ParserError as e:
                raise ZishException(
                    "Can't parse the timestamp '" + token.text + "'.") from e

        elif token_type == ZishParser.NULL:
            return None

        elif token_type == ZishParser.BOOL:
            return token.text == 'true'

        elif token_type in (
                ZishParser.BIN_INTEGER, ZishParser.DEC_INTEGER,
                ZishParser.HEX_INTEGER):
            return int(token.text.replace('_', ''), 0)

        elif token_type == ZishParser.DECIMAL:
            return Decimal(token.text.translate(_trans_dec))

        elif token_type == ZishParser.FLOAT:
            return float(token.text.replace('_', ''))

        elif token_type == ZishParser.STRING:
            return unescape(token.text[1:-1])

        elif token_type == ZishParser.BLOB:
            return bytearray(b64decode(token.text))

        else:
            raise ZishException(
                "Don't recognize the token type: " + str(token_type) + ".")
    else:
        raise ZishException(
            "Don't know what to do with type " + str(type(node)) +
            " with value " + str(node) + ".")


ESCAPES = {
    '0': '\u0000',   # NUL
    'a': '\u0007',   # alert BEL
    'b': '\u0008',   # backspace BS
    't': '\u0009',   # horizontal tab HT
    'n': '\u000A',   # linefeed LF
    'f': '\u000C',   # form feed FF
    'r': '\u000D',   # carriage return CR
    'v': '\u000B',   # vertical tab VT
    '"': '\u0022',   # double quote
    "'": '\u0027',   # single quote
    '?': '\u003F',   # question mark
    '\\': '\u005C',  # backslash
    '/': '\u002F',   # forward slash
    '\u000D\u000A': '',  # empty string
    '\u000D': '',  # empty string
    '\u000A': ''}  # empty string


def unescape(escaped_str):
    i = escaped_str.find('\\')
    if i == -1:
        return escaped_str
    else:
        head_str = escaped_str[:i]
        tail_str = escaped_str[i+1:]
        for k, v in ESCAPES.items():
            if tail_str.startswith(k):
                return head_str + v + unescape(tail_str[len(k):])

        for prefix, digits in (('x', 2), ('u', 4), ('U', 8)):
            if tail_str.startswith(prefix):
                hex_str = tail_str[1:1 + digits]
                v = chr(int(hex_str, 16))
                return head_str + v + unescape(tail_str[1 + digits:])

        raise ZishException(
            "Can't find a valid string following the first backslash of '" +
            escaped_str + "'.")


def dumps(obj):
    return _dump(obj, '')


def _dump(obj, indent):
    if isinstance(obj, Mapping):
        new_indent = indent + '  '
        items = []
        for k, v in sorted(obj.items()):
            items.append(
                '\n' + new_indent + _dump(k, new_indent) + ': ' +
                _dump(v, new_indent))
        return '{' + ','.join(items) + '}'
    elif isinstance(obj, bool):
        return 'true' if obj else 'false'
    elif isinstance(obj, list):
        new_indent = indent + '  '
        b = ','.join('\n' + new_indent + _dump(v, new_indent) for v in obj)
        return '[' + b + ']'
    elif isinstance(obj, (int, float, Decimal)):
        return str(obj)
    elif obj is None:
        return 'null'
    elif isinstance(obj, str):
        return QUOTE + obj + QUOTE
    elif isinstance(obj, (bytes, bytearray)):
        return "'" + b64encode(obj).decode() + "'"
    elif isinstance(obj, Datetime):
        if obj.tzinfo is None or obj.tzinfo == Timezone.utc:
            fmt = UTC_FORMAT
        else:
            fmt = TZ_FORMAT
        return obj.strftime(fmt)
    else:
        raise ZishException("Type " + str(type(obj)) + " not recognised.")
