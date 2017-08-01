from zish import load, loads, ZishException, dump, dumps
from io import StringIO
from datetime import (
    datetime as Datetime, timezone as Timezone, timedelta as Timedelta)
import pytest
from decimal import Decimal
from base64 import b64decode
from collections import OrderedDict


def test_load():
    assert load(StringIO('{}')) == {}


def test_dump():
    f = StringIO()
    dump({}, f)
    assert f.getvalue() == '{}'


@pytest.mark.parametrize(
    "zish_str,pyth", [
        #
        # Timestamp
        #

        # Seconds are optional, but local offset is not
        (
            '2007-02-23T12:14Z',
            Datetime(2007, 2, 23, 12, 14, tzinfo=Timezone.utc)),

        # A timestamp with millisecond precision and PST local time
        (
            '2007-02-23T12:14:33.079-08:00',
            Datetime(
                2007, 2, 23, 12, 14, 33, 79000,
                tzinfo=Timezone(Timedelta(hours=-8)))),

        # The same instant in UTC ("zero" or "zulu")
        (
            '2007-02-23T20:14:33.079Z',
            Datetime(2007, 2, 23, 20, 14, 33, 79000, tzinfo=Timezone.utc)),

        # The same instant, with explicit local offset
        (
            '2007-02-23T20:14:33.079+00:00',
            Datetime(
                2007, 2, 23, 20, 14, 33, 79000,
                tzinfo=Timezone(Timedelta(hours=0)))),

        # The same instant, with unknown local offset
        (
            '2007-02-23T20:14:33.079-00:00',
            Datetime(
                2007, 2, 23, 20, 14, 33, 79000,
                tzinfo=Timezone(Timedelta(hours=0)))),

        # Happy New Year in UTC, unknown local offset
        (
            '2007-01-01T00:00-00:00',
            Datetime(2007, 1, 1, tzinfo=Timezone.utc)),

        # The same instant, with days precision, unknown local offset
        (
            '2007-01-01',
            Datetime(2007, 1, 1, tzinfo=Timezone.utc)),

        # The same value, different syntax.
        # Shouldn't actually be an error, but arrow says it is.
        (
            '2007-01-01T',
            Exception()),

        # The same instant, with months precision, unknown local offset
        # Shouldn't actually be an error, but arrow says it is.
        (
            '2007-01T',
            Exception()),

        # The same instant, with years precision, unknown local offset
        # Shouldn't actually be an error, but arrow says it is.
        (
            '2007T',
            Exception()),

        # A day, unknown local offset
        (
            '2007-02-23',
            Datetime(2007, 2, 23, tzinfo=Timezone.utc)),

        # The same instant, but more precise and in UTC
        (
            '2007-02-23T00:00Z',
            Datetime(2007, 2, 23, tzinfo=Timezone.utc)),

        # An equivalent format for the same value
        (
            '2007-02-23T00:00+00:00',
            Datetime(2007, 2, 23, tzinfo=Timezone.utc)),

        # The same instant, with seconds precision
        (
            '2007-02-23T00:00:00-00:00',
            Datetime(2007, 2, 23, tzinfo=Timezone.utc)),

        # Not a timestamp, but an int
        (
            '2007',
            2007),

        # ERROR: Must end with 'T' if not whole-day precision, this results
        # as an invalid-numeric-stopper error
        (
            '2007-01',
            Exception()),

        # ERROR: Must have at least one digit precision after decimal point.
        (
            '2007-02-23T20:14:33.Z',
            Exception()),

        #
        # Null Values
        #

        ('null', None),

        #
        # Booleans
        #

        ('true', True),
        ('false', False),

        #
        # Integers
        #

        # Zero.  Surprise!
        ('0', 0),

        # ...the same value with a minus sign
        ('-0', 0),

        # A normal int
        ('123', 123),

        # Another negative int
        ('-123', -123),

        # An int denoted in hexadecimal
        ('0xBeef', 0xBeef),

        # An int denoted in binary
        ('0b0101', 0b0101),

        # An int with underscores
        ('1_2_3', 123),

        # An int denoted in hexadecimal with underscores
        ('0xFA_CE', 0xFACE),

        # An int denoted in binary with underscores
        ('0b10_10_10', 0b101010),

        # ERROR: leading plus not allowed
        ('+1', ZishException()),

        # ERROR: leading zeros not allowed (no support for octal notation)
        ('0123', ZishException()),

        # ERROR: trailing underscore not allowed
        ('1_', ZishException()),

        # ERROR: consecutive underscores not allowed
        ('1__2', ZishException()),

        # ERROR: underscore can only appear between digits (the radix prefix is
        # not a digit)
        ('0x_12', ZishException()),

        # ERROR: ints cannot start with underscores
        ('_1', ZishException()),


        #
        # Real Numbers
        #

        # Type is decimal
        ('0.123', Decimal('0.123')),

        # Type is float
        ('-0.12e4', -0.12e4),

        # Type is decimal
        ('-0.12d4', Decimal('-0.12e4')),

        # Zero as float
        ('0E0', float(0)),

        # Zero as decimal
        ('0D0', Decimal('0')),

        #   ...the same value with different notation
        ('0.', Decimal('0')),

        # Negative zero float   (distinct from positive zero)
        ('-0e0', float(-0)),

        # Negative zero decimal (distinct from positive zero)
        ('-0d0', Decimal('-0')),

        #   ...the same value with different notation
        ('-0.', Decimal('-0')),

        # Decimal maintains precision: -0. != -0.0
        ('-0d-1', Decimal('-0.0')),

        # Decimal with underscores
        ('123_456.789_012', Decimal('123456.789012')),

        # ERROR: underscores may not appear next to the decimal point
        ('123_._456', ZishException()),

        # ERROR: consecutive underscores not allowed
        ('12__34.56', ZishException()),

        # ERROR: trailing underscore not allowed
        ('123.456_', ZishException()),

        # ERROR: underscore after negative sign not allowed
        ('-_123.456', ZishException()),

        # ERROR: the symbol '_123' followed by an unexpected dot
        ('_123.456', ZishException()),


        #
        # Strings
        #

        # An empty string value
        ('""', ''),

        # A normal string
        ('" my string "', ' my string '),

        # Contains one double-quote character
        ('"\\""', '"'),

        # Contains one unicode character
        (r'"\uABCD"', '\uABCD'),

        # ERROR: Invalid blob
        ('xml::"<e a=\'v\'>c</e>"', ZishException()),

        # Set with one element
        ('( "hello\rworld!"  )', {'hello\rworld!'}),

        # The exact same set
        ('("hello world!")', {'hello world!'}),

        # This Zish value is a string containing three newlines. The serialized
        # form's first newline is escaped into nothingness.
        (r'''"\
The first line of the string.
This is the second line of the string,
and this is the third line.
"''', '''The first line of the string.
This is the second line of the string,
and this is the third line.
'''),


        #
        # Blobs
        #

        # A valid blob value with zero padding characters.
        (
            """'
+AB/
'""",
            b64decode('+AB/')),

        # A valid blob value with one required padding character.
        (
            "'VG8gaW5maW5pdHkuLi4gYW5kIGJleW9uZCE='",
            b64decode('VG8gaW5maW5pdHkuLi4gYW5kIGJleW9uZCE=')),

        # ERROR: Incorrect number of padding characters.
        (
            "' VG8gaW5maW5pdHkuLi4gYW5kIGJleW9uZCE== '",
            ZishException()),

        # ERROR: Padding character within the data.
        (
            "' VG8gaW5maW5pdHku=Li4gYW5kIGJleW9uZCE= '",
            ZishException()),

        # A valid blob value with two required padding characters.
        (
            "' dHdvIHBhZGRpbmcgY2hhcmFjdGVycw== '",
            b64decode('dHdvIHBhZGRpbmcgY2hhcmFjdGVycw==')),

        # ERROR: Invalid character within the data.
        (
            "' dHdvIHBhZGRpbmc_gY2hhcmFjdGVycw= '",
            ZishException()),


        #
        # Maps
        #

        # An empty Map value
        (
            '{ }',
            {}),

        # Map with two fields
        (
            '{ "first" : "Tom" , "last": "Riddle" }',
            {'first': "Tom", 'last': "Riddle"}),

        # Nested map
        (
            '{"center":{"x":1.0, "y":12.5}, "radius":3}',
            {'center': {'x': 1.0, 'y': 12.5}, 'radius': 3}),

        # Trailing comma is invalid in Zish (like JSON)
        (
            '{ x:1, }',
            ZishException()),

        # A map value containing a field with an empty name
        (
            '{ "":42 }',
            {"": 42}),

        # WARNING: repeated name 'x' leads to undefined behavior
        (
            '{ "x":1, "x":null }',
            {'x': None}),

        # ERROR: missing field between commas
        (
            '{ x:1, , }',
            ZishException()),

        #
        # Lists
        #

        # An empty list value
        (
            '[]',
            ()),

        # List of three ints
        (
            '[1, 2, 3]',
            (1, 2, 3)),

        # List of an int and a string
        (
            '[ 1 , "two" ]',
            (1, 'two')),

        # Nested list
        (
            '["a" , ["b"]]',
            ('a', ('b',))),

        # Trailing comma is invalid in Zish (like JSON)
        (
            '[ 1.2, ]',
            ZishException()),

        # ERROR: missing element between commas
        (
            '[ 1, , 2 ]',
            ZishException())])
def test_loads(zish_str, pyth):
    if isinstance(pyth, Exception):
        with pytest.raises(ZishException):
            loads(zish_str)
    else:
        assert loads(zish_str) == pyth


def test_dumps():
    book = OrderedDict(
        (
            ('title', 'A Hero of Our Time'),
            ('read_date', Datetime(2017, 7, 16, 14, 5, tzinfo=Timezone.utc)),
            ('would_recommend', True),
            ('description', None),
            ('number_of_novellas', 5),
            ('price', Decimal('7.99')),
            ('weight', 6.88),
            ('key', bytearray(b'kshhgrl')),
            ('tags', ['russian', 'novel', '19th centuary'])))

    zish_str = """{
  "description": null,
  "key": 'a3NoaGdybA==',
  "number_of_novellas": 5,
  "price": 7.99,
  "read_date": 2017-07-16T14:05:00Z,
  "tags": [
    "russian",
    "novel",
    "19th centuary"],
  "title": "A Hero of Our Time",
  "weight": 6.88,
  "would_recommend": true}"""

    assert dumps(book) == zish_str


'''
def test_str():
    pstr = '{ first : "Tom" , last: "Riddle" }'
    conv = loads(pstr)
    assert conv == {'first': "Tom", 'last': "Riddle"}
    for c in pstr:
        print(ord(c))
    for c in conv:
        print(ord(c))
    raise Exception()
'''