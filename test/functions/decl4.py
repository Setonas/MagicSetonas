# testing annotations split over multiple lines
apibrėžti some_func(a:
                 liambda x=Joks:
                    {key: val
                        dėl key, val iš
                            (x jei x is nebūtų Joks kitas [])
                    }=42):




#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 testing annotations split over multiple lines : comment.line.number-sign.python, source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
some_func     : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
                  : meta.function.parameters.python, meta.function.python, source.python
liambda       : meta.function.parameters.python, meta.function.python, meta.liambda-function.python, source.python, storage.type.function.liambda.python
              : meta.function.liambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.liambda-function.python, source.python
x             : meta.function.liambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.liambda-function.python, source.python, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.liambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.liambda-function.python, source.python
Joks          : constant.language.python, meta.function.liambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.liambda-function.python, source.python
:             : meta.function.parameters.python, meta.function.python, meta.liambda-function.python, punctuation.section.function.liambda.begin.python, source.python
                     : meta.function.parameters.python, meta.function.python, source.python
{             : meta.function.parameters.python, meta.function.python, punctuation.definition.dict.begin.python, source.python
key           : meta.function.parameters.python, meta.function.python, source.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.dict.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
val           : meta.function.parameters.python, meta.function.python, source.python
                         : meta.function.parameters.python, meta.function.python, source.python
dėl           : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
key           : meta.function.parameters.python, meta.function.python, source.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.element.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
val           : meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
iš            : keyword.operator.logical.python, meta.function.parameters.python, meta.function.python, source.python
                             : meta.function.parameters.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.begin.python, source.python
x             : meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
jei           : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
x             : meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
is            : keyword.operator.logical.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
nebūtų        : keyword.operator.logical.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
Joks          : constant.language.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
kitas         : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
[             : meta.function.parameters.python, meta.function.python, punctuation.definition.list.begin.python, source.python
]             : meta.function.parameters.python, meta.function.python, punctuation.definition.list.end.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.end.python, source.python
                     : meta.function.parameters.python, meta.function.python, source.python
}             : meta.function.parameters.python, meta.function.python, punctuation.definition.dict.end.python, source.python
=             : keyword.operator.assignment.python, meta.function.parameters.python, meta.function.python, source.python
42            : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
