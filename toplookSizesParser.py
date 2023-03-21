# Generated from toplookSizes.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,25,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,5,0,14,8,0,10,0,12,0,17,9,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,0,0,
        3,0,2,4,0,1,1,0,3,8,23,0,7,1,0,0,0,2,18,1,0,0,0,4,22,1,0,0,0,6,8,
        3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,15,1,
        0,0,0,11,12,5,1,0,0,12,14,3,2,1,0,13,11,1,0,0,0,14,17,1,0,0,0,15,
        13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,15,1,0,0,0,18,19,5,9,0,
        0,19,20,5,2,0,0,20,21,3,4,2,0,21,3,1,0,0,0,22,23,7,0,0,0,23,5,1,
        0,0,0,2,9,15
    ]

class toplookSizesParser ( Parser ):

    grammarFileName = "toplookSizes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'='", "'XS'", "'S'", "'M'", "'L'", 
                     "'XL'", "'XXL'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "WS" ]

    RULE_sizes = 0
    RULE_size = 1
    RULE_sizeformat = 2

    ruleNames =  [ "sizes", "size", "sizeformat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INT=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SizesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def size(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toplookSizesParser.SizeContext)
            else:
                return self.getTypedRuleContext(toplookSizesParser.SizeContext,i)


        def getRuleIndex(self):
            return toplookSizesParser.RULE_sizes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizes" ):
                listener.enterSizes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizes" ):
                listener.exitSizes(self)




    def sizes(self):

        localctx = toplookSizesParser.SizesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sizes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.size()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 11
                self.match(toplookSizesParser.T__0)
                self.state = 12
                self.size()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(toplookSizesParser.INT, 0)

        def sizeformat(self):
            return self.getTypedRuleContext(toplookSizesParser.SizeformatContext,0)


        def getRuleIndex(self):
            return toplookSizesParser.RULE_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize" ):
                listener.enterSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize" ):
                listener.exitSize(self)




    def size(self):

        localctx = toplookSizesParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(toplookSizesParser.INT)
            self.state = 19
            self.match(toplookSizesParser.T__1)
            self.state = 20
            self.sizeformat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeformatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toplookSizesParser.RULE_sizeformat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeformat" ):
                listener.enterSizeformat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeformat" ):
                listener.exitSizeformat(self)




    def sizeformat(self):

        localctx = toplookSizesParser.SizeformatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sizeformat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
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





