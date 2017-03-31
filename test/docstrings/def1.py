apibrėžti foo():
    '''TE\'''ST'''

apibrėžti foo():
    r'''TE\'''ST'''

apibrėžti foo():
    R'''TE\'''ST'''

apibrėžti foo():
    u'''TEST'''

apibrėžti foo():
    U'''TEST'''

apibrėžti foo():
    b'''TEST'''

apibrėžti foo():
    B'''TEST'''



apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
TE            : source.python, string.quoted.docstring.multi.python
\'            : constant.character.escape.python, source.python, string.quoted.docstring.multi.python
''ST          : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
              : source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.multi.python
TE            : source.python, string.quoted.docstring.raw.multi.python
\'            : source.python, string.quoted.docstring.raw.multi.python
''ST          : source.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.multi.python
              : source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.multi.python
TE            : source.python, string.quoted.docstring.raw.multi.python
\'            : source.python, string.quoted.docstring.raw.multi.python
''ST          : source.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.multi.python
              : source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
u             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
TEST          : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
              : source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
U             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
TEST          : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
              : source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
b             : source.python, storage.type.string.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.binary.multi.python
TEST          : source.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.binary.multi.python
              : source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
B             : source.python, storage.type.string.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.binary.multi.python
TEST          : source.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.binary.multi.python
