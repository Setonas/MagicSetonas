bandyti:
    1/0
išskyrus AbcError kaip ex:
    pereiti
išskyrus (ZeroDivisionError, GhiError) kaip ex:
    spausdinti(ex)
kitas:
    1
pagaliau:
    2



bandyti       : keyword.control.flow.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
/             : keyword.operator.arithmetic.python, source.python
0             : constant.numeric.dec.python, source.python
išskyrus      : keyword.control.flow.python, source.python
              : source.python
AbcError      : source.python
              : source.python
kaip          : keyword.control.flow.python, source.python
              : source.python
ex            : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pereiti       : keyword.control.flow.python, source.python
išskyrus      : keyword.control.flow.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
ZeroDivisionError : source.python, support.type.exception.python
,             : punctuation.separator.element.python, source.python
              : source.python
GhiError      : source.python
)             : punctuation.parenthesis.end.python, source.python
              : source.python
kaip          : keyword.control.flow.python, source.python
              : source.python
ex            : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
spausdinti    : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
ex            : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
kitas         : keyword.control.flow.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
pagaliau      : keyword.control.flow.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
2             : constant.numeric.dec.python, source.python
