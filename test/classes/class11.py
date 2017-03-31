rūšis F:
    apibrėžti __init__(pats, a, b=1):
        pats.a = a
        pats.b = b
        spausdinti(pats)
        pats()
        a.pats = 1
        a.pats.bar = 2
        pats[123]



rūšis         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
F             : entity.name.type.class.python, meta.class.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : meta.function.python, source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
__init__      : meta.function.python, source.python, support.function.magic.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
pats          : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python, variable.parameter.function.language.special.pats.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
b             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
1             : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pats          : source.python, variable.language.special.pats.python
.             : source.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
a             : source.python
              : source.python
pats          : source.python, variable.language.special.pats.python
.             : source.python
b             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
b             : source.python
              : source.python
spausdinti    : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
pats          : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.language.special.pats.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
pats          : meta.function-call.python, source.python, variable.language.special.pats.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
a             : source.python
.             : source.python
pats          : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
              : source.python
a             : source.python
.             : source.python
pats          : source.python
.             : source.python
bar           : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
2             : constant.numeric.dec.python, source.python
              : source.python
pats          : meta.item-access.python, source.python, variable.language.special.pats.python
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
123           : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.python
