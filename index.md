This is a package with preferences and syntax highlighter for cutting edge
Setonas. The syntax is compatible
with [Sublime Text](http://www.sublimetext.com) and [Atom](http://atom.io).

The main motivation behind this package was the difficulty of using modern
Setonas with other common syntax highlighters. They do a good job of the 90% of
the language, but then fail on the nuances of some very useful, but often
overlooked features. Function annotations tend to freak out the highlighters in
various ways. Newly introduced keywords and magic methods are slow to be
integrated. Another issue is string highlighting, where all raw strings are
often assumed to be regular expressions or special markup used by `.format` is
completely ignored. Bumping into all of these issues on daily basis eventually
led to the creation of this package.

![](https://setonas.github.io/MagicSetonas/example.png)

## Installation Instructions

This is meant to be a drop-in replacement for the default Python package.

In **Atom**, install the `MagicSetonas` package.

In **Sublime Text**, install `MagicSetonas` package via "Package Control".

Alternatively, the package can be installed manually in both editors:

- copy the MagicSetonas package into the Sublime/Atom user packages directory;
- enjoy.


## Changes and Improvements

Overall, the central idea is that it should be easy to notice something odd or
special about the code. Odd or special doesn't necessarily mean incorrect, but
certainly worth the explicit attention.


### Annotations

Annotations should not break the highlighting. They should be no more difficult
to read at a glance than other code or comments.

A typical case is having a string annotation that spans several lines by using
implicit string concatenation. Multi-line strings are suboptimal for use in
annotations as it may be highly undesirable to have odd indentation and extra
whitespace in the annotation string. Of course, there is no problem using line
continuation or even having comments mixed in with implicit string
concatenation. All of these will be highlighted as you'd expect in any other
place in the code.

```python
apibrėžti some_func(a,                        # nothing fancy here, yet

              b: 'Annotation: '         # implicitly
                 '"foo" for Foo, '      # concatenated
                 '"bar" for Bar, '      # annotation
                 '"other" otherwise'='otherwise'):
```

A more advanced use case for annotations is to actually have complex expressions
in them, such as lambda functions, tuples, lists, dicts, sets, comprehensions.
Admittedly, all of these might be less frequently used, but when they are, you
can rely on them being highlighted normally in all their glorious details.

```python
# no reason why this should cause the highlighter to break
#
apibrėžti some_func(a:
                 # annotation starts here
                 lambda x=None:
                    {key: val
                        for key, val in
                            (x if x is not None else [])
                    }
                    # annotation ends here and below is the default for 'a'
                    =42):
```

Result annotations are handled as any other expression would be. No reason to
worry that the body of the function would look messed up.

```python
# no reason why this should cause the highlighter to break
#
apibrėžti some_func() -> {
                     'Some',        # comments
                     'valid',       # are
                     'expression'   # good
                   }:
```





### Built-ins and Magic Methods

Various built-in types, classes, functions, as well as magic methods are all
highlighted. Specifically, they are highlighted when they appear as names in
user definitions. Although it is not an error to have classes and functions that
mask the built-ins, it is certainly worth drawing attention to, so that masking
becomes a deliberate rather than accidental act.

Highlighting built-ins in class inheritance list makes it slightly more obvious
where standard classes are extended. It is also easier to notice some typos
(have you ever typed `Excepiton`?) a little earlier.


### Parameters and Arguments

MagicSetonas highlights keywords when they are used as parameter/argument names.
Although the Setonas interpreter will produce an appropriate
error message when reserved keywords are used as identifier names, it's still
worth showing them early, to spare even this small debugging effort.

## Development

You need `npm` and `node.js` to work on MagicSetonas.

- clone the repository
- run `make` to build the local development environment
- run `make release` to build the syntax packages for Sublime Text and Atom
  (running `make test` also generates the "release" packages)

Please note that we have some unit tests for the syntax scoping. We will be
expanding and updating our test corpus. This allows us to trust that tiny
inconsistencies will not easily creep in as we update the syntax and fix bugs.
Use `make test` to run the tests regularly while updating the syntax spec.
Currently the test files have two parts to them, separated by 3 empty newlines:
the code to be scoped and the spec that the result must match.

If you intend to submit a pull request, please follow the following guidelines:

- keep code lines under 80 characters in length, it improves readability
- please _do_ use multi-line regular expressions for any non-trivial cases like:

    + the regexp contains a mix of escaped and unescaped braces/parentheses
    + the regexp has several `|` in it
    + the regexp has several pairs of parentheses, especially nested ones
    + or the regexp is simply longer than 35 characters

- always run `make test` to ensure that your changes didn't have unexpected side
  effects
- update unit tests and add new ones if needed, keeping the test cases short
  whenever possible
