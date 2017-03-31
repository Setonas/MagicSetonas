apibrėžti myfunc(pats,            # gotta have pats
           param1="value",  # values are cool
           param2=Tiesa,    # or Netikras, whatever
           **kwargs):       # you never know
    pereiti



apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
myfunc        : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
pats          : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python, variable.parameter.function.language.special.pats.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 gotta have pats : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
param1        : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
"             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
value         : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.python
"             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 values are cool : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
param2        : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
Tiesa         : constant.language.python, meta.function.parameters.python, meta.function.python, source.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 or Netikras, whatever : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
**            : keyword.operator.unpacking.parameter.python, meta.function.parameters.python, meta.function.python, source.python
kwargs        : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 you never know : comment.line.number-sign.python, source.python
              : source.python
pereiti       : keyword.control.flow.python, source.python
