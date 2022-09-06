"""
This module contains what I consider best practices for 'for loops'. 

Influenced by :ref:`Raymond hettinger`
"""


def original_idea():
    """
    The description about original_idea
    """

    names = ["john", "jim", "mark"]

    for i in range(len(names)):
        print(names[i])

    for name in names:
        print(names)


def google_docstrings(num1, num2) -> int:
    """Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Args:
        num1 (int) : First number to add.
        num2 (int) : Second number to add.

    Returns:
        The sum of ``num1`` and ``num2``.

    Raises:
        AnyError: If anything bad happens.
    """
    return num1 + num2


def numpy_docstrings(num1, num2) -> int:
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    Raises
    ======
     MyException
        if anything bad happens

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2


def empty(shape, dtype=None, order="C"):
    """Return a new matrix of given shape and type, without initializing entries.

    Parameters
    ----------
    shape : int or tuple of int
        Shape of the empty matrix.
    dtype : data-type, optional
        Desired output data-type.
    order : {'C', 'F'}, optional
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.

    See Also
    --------
    empty_like, zeros

    .. snip

    """


def dummy_function_example(name, foo=None):
    """
    The docstring in the function should fully explain what the function is
    for and how to use it

    * this is a bullet list
    * with multiple entries and some text in *italic* and even **bold**.
      The bullet list items can span multiple lines which are indented

    .. warning:: bullet (as well as enumerated) lists have to start and end
       with an empty line

    1. Single backquotes are for **references** to other documented items.
       For example `basf2.Module` will link to the documentation of the class
       Module in the python module basf2. A different link name and link
       target can be specified with <>: `Module class <basf2.Module>` will
       link to basf2.Module but the link will read "Module class"
    2. Double backquotes are for ``literal text``.

    .. warning:: this is different to markdown where single backquotes are
       usually used for literal text

    3. Links to external websites are usually of the form `Link Text <http://example.com>`_.

    .. note:: there is an underscore at the end of links

    4. math is supported either inline :math:`f(x) = \sum_{x=i}^N x^i` or as
       display verssion:

       .. math::

          f(x) = \sum_{i=1}^N x^i

       .. seealso:: `Math support in Sphinx <http://www.sphinx-doc.org/en/stable/ext/math.html>`_
    5. The easiest way for code example is the "doctest" syntax: Start a new
       paragaph after an empty line with ``>>>`` followed by the python
       statements and (optionally) the expected output of these statements.

       >>> dummy_function_example("some name", foo="bar")
       "Hello some name, Lord of bar"

       .. seealso:: `Showing code examples <http://www.sphinx-doc.org/en/stable/markup/code.html>`_

    6. To document parameters and return types please use the :ref:`googlestyle` as shown below:

    Note:
      For class members please do not include the ``self`` parameter in this list

    Parameters:
      name (str): Description of the first parameter
       Can also span multiple lines if indented properly
      foo: Second parameter but no type given

    Returns:
      Description of the return value

    See Also:
      Some references to other functions
    """
