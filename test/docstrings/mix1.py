'''TEST'''

rūšis Foo:
    # comment
    R'''TEST'''

    apibrėžti foo(pats, a:'''TEST''') -> '''TEST''': #ok
        r'''TEST'''
        su bar:
            pereiti

    apibrėžti bar(pats, a:'''TEST''') -> '''TEST''': pereiti
        '''TEST''' # additional docstring
        su bar:
            pereiti




'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
TEST          : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
              : source.python
rūšis         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
Foo           : entity.name.type.class.python, meta.class.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 comment      : comment.line.number-sign.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.multi.python
TEST          : source.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.multi.python
              : source.python
              : meta.function.python, source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
pats          : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python, variable.parameter.function.language.special.pats.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
'''           : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
TEST          : meta.function.parameters.python, meta.function.python, source.python, string.quoted.multi.python
'''           : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.multi.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
              : meta.function.python, source.python
->            : meta.function.python, punctuation.separator.annotation.result.python, source.python
              : meta.function.python, source.python
'''           : meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
TEST          : meta.function.python, source.python, string.quoted.multi.python
'''           : meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.multi.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
ok            : comment.line.number-sign.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.multi.python
TEST          : source.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.multi.python
              : source.python
su            : keyword.control.flow.python, source.python
              : source.python
bar           : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pereiti       : keyword.control.flow.python, source.python
              : source.python
              : meta.function.python, source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
bar           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
pats          : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python, variable.parameter.function.language.special.pats.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
'''           : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
TEST          : meta.function.parameters.python, meta.function.python, source.python, string.quoted.multi.python
'''           : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.multi.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
              : meta.function.python, source.python
->            : meta.function.python, punctuation.separator.annotation.result.python, source.python
              : meta.function.python, source.python
'''           : meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
TEST          : meta.function.python, source.python, string.quoted.multi.python
'''           : meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.multi.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pereiti       : keyword.control.flow.python, source.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
TEST          : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 additional docstring : comment.line.number-sign.python, source.python
              : source.python
su            : keyword.control.flow.python, source.python
              : source.python
bar           : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pereiti       : keyword.control.flow.python, source.python
