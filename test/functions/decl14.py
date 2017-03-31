# testing comments iš function definition
apibrėžti foo(    # before args
    a=42,   # between
            # args
    b=      # iš args
      24,
    d       # before '='
     =99,
    e
    )       # incomplete definition, missing COLON, you're probably typing it
    # pre docstring
    '''Docstring'''
    # post docstring

apibrėžti bar(): sugrįžti 1




#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 testing comments iš function definition : comment.line.number-sign.python, source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 before args  : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
42            : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 between      : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 args         : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
b             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 iš args      : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
24            : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
d             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 before '='   : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
99            : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
e             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
              : meta.function.parameters.python, meta.function.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
              : meta.function.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 incomplete definition, missing COLON, you're probably typing it : comment.line.number-sign.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 pre docstring : comment.line.number-sign.python, source.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
Docstring     : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 post docstring : comment.line.number-sign.python, source.python
              : source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
bar           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
sugrįžti      : keyword.control.flow.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
