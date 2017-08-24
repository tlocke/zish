# Generated from Zish.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\6\2\23\n\2\r\2\16\2\24\3\2\7\2\30\n\2\f\2")
        buf.write("\16\2\33\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4")
        buf.write("\3\4\3\4\7\4)\n\4\f\4\16\4,\13\4\3\4\3\4\3\4\3\4\5\4\62")
        buf.write("\n\4\3\5\3\5\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5A\n\5\3\6\3\6\3\6\3\6\7\6G\n\6\f\6\16\6J\13")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6P\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\f\23\2[\2\20\3\2\2\2\4")
        buf.write("\"\3\2\2\2\6\61\3\2\2\2\b@\3\2\2\2\nO\3\2\2\2\fQ\3\2\2")
        buf.write("\2\16U\3\2\2\2\20\31\5\4\3\2\21\23\7\13\2\2\22\21\3\2")
        buf.write("\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\26\3")
        buf.write("\2\2\2\26\30\5\4\3\2\27\22\3\2\2\2\30\33\3\2\2\2\31\27")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2\34")
        buf.write("\35\7\2\2\3\35\3\3\2\2\2\36#\5\16\b\2\37#\5\n\6\2 #\5")
        buf.write("\6\4\2!#\5\b\5\2\"\36\3\2\2\2\"\37\3\2\2\2\" \3\2\2\2")
        buf.write("\"!\3\2\2\2#\5\3\2\2\2$%\7\3\2\2%*\5\4\3\2&\'\7\7\2\2")
        buf.write("\')\5\4\3\2(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+-")
        buf.write("\3\2\2\2,*\3\2\2\2-.\7\4\2\2.\62\3\2\2\2/\60\7\3\2\2\60")
        buf.write("\62\7\4\2\2\61$\3\2\2\2\61/\3\2\2\2\62\7\3\2\2\2\63\64")
        buf.write("\7\5\2\2\649\5\16\b\2\65\66\7\7\2\2\668\5\16\b\2\67\65")
        buf.write("\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3")
        buf.write("\2\2\2<=\7\6\2\2=A\3\2\2\2>?\7\5\2\2?A\7\6\2\2@\63\3\2")
        buf.write("\2\2@>\3\2\2\2A\t\3\2\2\2BC\7\b\2\2CH\5\f\7\2DE\7\7\2")
        buf.write("\2EG\5\f\7\2FD\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2I")
        buf.write("K\3\2\2\2JH\3\2\2\2KL\7\t\2\2LP\3\2\2\2MN\7\b\2\2NP\7")
        buf.write("\t\2\2OB\3\2\2\2OM\3\2\2\2P\13\3\2\2\2QR\5\16\b\2RS\7")
        buf.write("\n\2\2ST\5\4\3\2T\r\3\2\2\2UV\t\2\2\2V\17\3\2\2\2\13\24")
        buf.write("\31\"*\619@HO")
        return buf.getvalue()


class ZishParser ( Parser ):

    grammarFileName = "Zish.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'('", "')'", "','", "'{'", 
                     "'}'", "':'", "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "LIST_START", "LIST_FINISH", "SET_START", 
                      "SET_FINISH", "COMMA", "MAP_START", "MAP_FINISH", 
                      "COLON", "WS", "NULL", "BOOL", "TIMESTAMP", "FLOAT", 
                      "DECIMAL", "INTEGER", "STRING", "BLOB" ]

    RULE_start = 0
    RULE_element = 1
    RULE_list_type = 2
    RULE_set_type = 3
    RULE_map_type = 4
    RULE_pair = 5
    RULE_key = 6

    ruleNames =  [ "start", "element", "list_type", "set_type", "map_type", 
                   "pair", "key" ]

    EOF = Token.EOF
    LIST_START=1
    LIST_FINISH=2
    SET_START=3
    SET_FINISH=4
    COMMA=5
    MAP_START=6
    MAP_FINISH=7
    COLON=8
    WS=9
    NULL=10
    BOOL=11
    TIMESTAMP=12
    FLOAT=13
    DECIMAL=14
    INTEGER=15
    STRING=16
    BLOB=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.ElementContext)
            else:
                return self.getTypedRuleContext(ZishParser.ElementContext,i)


        def EOF(self):
            return self.getToken(ZishParser.EOF, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ZishParser.WS)
            else:
                return self.getToken(ZishParser.WS, i)

        def getRuleIndex(self):
            return ZishParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = ZishParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.element()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZishParser.WS:
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 15
                    self.match(ZishParser.WS)
                    self.state = 18 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZishParser.WS):
                        break

                self.state = 20
                self.element()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(ZishParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ZishParser.KeyContext,0)


        def map_type(self):
            return self.getTypedRuleContext(ZishParser.Map_typeContext,0)


        def list_type(self):
            return self.getTypedRuleContext(ZishParser.List_typeContext,0)


        def set_type(self):
            return self.getTypedRuleContext(ZishParser.Set_typeContext,0)


        def getRuleIndex(self):
            return ZishParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = ZishParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZishParser.NULL, ZishParser.BOOL, ZishParser.TIMESTAMP, ZishParser.FLOAT, ZishParser.DECIMAL, ZishParser.INTEGER, ZishParser.STRING, ZishParser.BLOB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.key()
                pass
            elif token in [ZishParser.MAP_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.map_type()
                pass
            elif token in [ZishParser.LIST_START]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.list_type()
                pass
            elif token in [ZishParser.SET_START]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.set_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST_START(self):
            return self.getToken(ZishParser.LIST_START, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.ElementContext)
            else:
                return self.getTypedRuleContext(ZishParser.ElementContext,i)


        def LIST_FINISH(self):
            return self.getToken(ZishParser.LIST_FINISH, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZishParser.COMMA)
            else:
                return self.getToken(ZishParser.COMMA, i)

        def getRuleIndex(self):
            return ZishParser.RULE_list_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_type" ):
                listener.enterList_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_type" ):
                listener.exitList_type(self)




    def list_type(self):

        localctx = ZishParser.List_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_type)
        self._la = 0 # Token type
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(ZishParser.LIST_START)
                self.state = 35
                self.element()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 36
                    self.match(ZishParser.COMMA)
                    self.state = 37
                    self.element()
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 43
                self.match(ZishParser.LIST_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(ZishParser.LIST_START)
                self.state = 46
                self.match(ZishParser.LIST_FINISH)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET_START(self):
            return self.getToken(ZishParser.SET_START, 0)

        def key(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.KeyContext)
            else:
                return self.getTypedRuleContext(ZishParser.KeyContext,i)


        def SET_FINISH(self):
            return self.getToken(ZishParser.SET_FINISH, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZishParser.COMMA)
            else:
                return self.getToken(ZishParser.COMMA, i)

        def getRuleIndex(self):
            return ZishParser.RULE_set_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_type" ):
                listener.enterSet_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_type" ):
                listener.exitSet_type(self)




    def set_type(self):

        localctx = ZishParser.Set_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_set_type)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(ZishParser.SET_START)
                self.state = 50
                self.key()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 51
                    self.match(ZishParser.COMMA)
                    self.state = 52
                    self.key()
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 58
                self.match(ZishParser.SET_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(ZishParser.SET_START)
                self.state = 61
                self.match(ZishParser.SET_FINISH)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Map_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP_START(self):
            return self.getToken(ZishParser.MAP_START, 0)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.PairContext)
            else:
                return self.getTypedRuleContext(ZishParser.PairContext,i)


        def MAP_FINISH(self):
            return self.getToken(ZishParser.MAP_FINISH, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZishParser.COMMA)
            else:
                return self.getToken(ZishParser.COMMA, i)

        def getRuleIndex(self):
            return ZishParser.RULE_map_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_type" ):
                listener.enterMap_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_type" ):
                listener.exitMap_type(self)




    def map_type(self):

        localctx = ZishParser.Map_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_map_type)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(ZishParser.MAP_START)
                self.state = 65
                self.pair()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 66
                    self.match(ZishParser.COMMA)
                    self.state = 67
                    self.pair()
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 73
                self.match(ZishParser.MAP_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(ZishParser.MAP_START)
                self.state = 76
                self.match(ZishParser.MAP_FINISH)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ZishParser.KeyContext,0)


        def COLON(self):
            return self.getToken(ZishParser.COLON, 0)

        def element(self):
            return self.getTypedRuleContext(ZishParser.ElementContext,0)


        def getRuleIndex(self):
            return ZishParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = ZishParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.key()
            self.state = 80
            self.match(ZishParser.COLON)
            self.state = 81
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZishParser.BOOL, 0)

        def NULL(self):
            return self.getToken(ZishParser.NULL, 0)

        def TIMESTAMP(self):
            return self.getToken(ZishParser.TIMESTAMP, 0)

        def INTEGER(self):
            return self.getToken(ZishParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(ZishParser.FLOAT, 0)

        def DECIMAL(self):
            return self.getToken(ZishParser.DECIMAL, 0)

        def STRING(self):
            return self.getToken(ZishParser.STRING, 0)

        def BLOB(self):
            return self.getToken(ZishParser.BLOB, 0)

        def getRuleIndex(self):
            return ZishParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = ZishParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZishParser.NULL) | (1 << ZishParser.BOOL) | (1 << ZishParser.TIMESTAMP) | (1 << ZishParser.FLOAT) | (1 << ZishParser.DECIMAL) | (1 << ZishParser.INTEGER) | (1 << ZishParser.STRING) | (1 << ZishParser.BLOB))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





