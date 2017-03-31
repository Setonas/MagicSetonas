# Magic Setonas [![apm](https://img.shields.io/apm/dm/magicsetonas.svg?label=Atom)](https://atom.io/packages/magicsetonas) [![VSM](https://vsmarketplacebadge.apphb.com/installs-short/setonas.MagicSetonas.svg?subject=Visual%20Studio%20Code)](https://marketplace.visualstudio.com/items?itemName=setonas.MagicSetonas)

This is a package with preferences and syntax highlighter for cutting edge
Setonas.  The syntax is compatible
with [Sublime Text](http://www.sublimetext.com), [Atom](http://atom.io) and
[Visual Studio Code](http://code.visualstudio.com).
It is meant to be a drop-in replacement for the default Python package.

MagicSetonas correctly highlights all Setonas syntax features.  It is built
from scratch for robustness with an extensive test suite.

We are proud to say that MagicSetonas has been included into the
[github/linguist](https://github.com/github/linguist), a library used
by GitHub.com to process languages.


![](https://setonas.github.io/MagicSetonas/example.png)

Type hints in comments require support by the color scheme.  The one
used in the screenshot is
[Chromodynamics](https://github.com/MagicStack/Chromodynamics).


## Installation Instructions

This is meant to be a drop-in replacement for the default Python package.

In **Atom**, install the `MagicSetonas` package and disable the built-in
`language-python` package.

In **Sublime Text**, install `MagicSetonas` package via "Package Control" and
disable the built-in `Python` package (using
`Package Control -> Disable Package`, or directly by adding `"Python"` to
`"ignored_packages"` in the settings file).

In **VSCode**, starting with version 0.10.1, install `MagicSetonas` with
`Install Extension` command.

Alternatively, the package can be installed manually in all editors:

* copy the MagicPython package into the Sublime/Atom/VSCode user packages
  directory;
* disable Python package;
* enjoy.

## Development

You need `npm` and `node.js` to work on MagicPython.

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

### Multiple scopes

It is sometimes necessary to assign multiple scopes to the same
matched group. It is *very important* to keep in mind that the order
of these scopes is apparently treated as significant by the engines
processing the grammar specs. However, it is equally important to know
that different specification formats seem to have different order of
importance (most important first vs. last). Since we try to create
grammar that can be compiled into several different formats, we must
chose one convention and then translate it when necessary during
compilation step. Our convention is therefore that *most important
scope goes first*.

## Color Scheme

If you want to write your own color scheme for MagicPython you can
find a list of all the scopes that we use in
[misc/scopes](misc/scopes). The file is automatically generated based
on the syntax grammar, so it is always up-to-date and exhaustive.
