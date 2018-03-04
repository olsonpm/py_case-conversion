import sys

PYTHON = sys.version_info[0]

if 3 == PYTHON:
    # Python 3 and ST3
    from . import case_parse
else:
    # Python 2 and ST2
    import case_parse


def camelcase(text, acronyms=None):
    """Return text in camelCase style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> camelcase("hello world")
    'helloWorld'
    >>> camelcase("HELLO_HTML_WORLD", True, ["HTML"])
    'helloHTMLWorld'
    """
    words, _, _ = case_parse.parse_case(text, acronyms)
    if words:
        words[0] = words[0].lower()
    return ''.join(words)


def pascalcase(text, acronyms=None):
    """Return text in PascalCase style (aka MixedCase).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> pascalcase("hello world")
    'HelloWorld'
    >>> pascalcase("HELLO_HTML_WORLD", True, ["HTML"])
    'HelloHTMLWorld'
    """
    words, _, _ = case_parse.parse_case(text, acronyms)
    return ''.join(words)


def snakecase(text, acronyms=None):
    """Return text in snake_case style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> snakecase("hello world")
    'hello_world'
    >>> snakecase("HelloHTMLWorld", True, ["HTML"])
    'hello_html_world'
    """
    words, _, _ = case_parse.parse_case(text, acronyms)
    return '_'.join([w.lower() for w in words])


def dashcase(text, acronyms=None):
    """Return text in dash-case style (aka kebab-case, spinal-case).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> dashcase("hello world")
    'hello-world'
    >>> dashcase("HelloHTMLWorld", True, ["HTML"])
    'hello-html-world'
    """
    words, _, _ = case_parse.parse_case(text, acronyms)
    return '-'.join([w.lower() for w in words])


def kebabcase(text, acronyms=None):
    """Return text in kebab-case style (aka snake-case, spinal-case).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> kebabcase("hello world")
    'hello-world'
    >>> kebabcase("HelloHTMLWorld", True, ["HTML"])
    'hello-html-world'
    """
    return dashcase(text, acronyms)


def spinalcase(text, acronyms=None):
    """Return text in spinal-case style (aka snake-case, kebab-case).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> spinalcase("hello world")
    'hello-world'
    >>> spinalcase("HELLO_HTML_WORLD", True, ["HTML"])
    'hello-html-world'
    """
    return dashcase(text, acronyms)


def constcase(text, acronyms=None):
    """Return text in CONST_CASE style (aka SCREAMING_SNAKE_CASE).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> constcase("hello world")
    'HELLO_WORLD'
    >>> constcase("helloHTMLWorld", True, ["HTML"])
    'HELLO_HTML_WORLD'
    """
    words, _, _ = case_parse.parse_case(text, acronyms)
    return '_'.join([w.upper() for w in words])


def screaming_snakecase(text, acronyms=None):
    """Return text in SCREAMING_SNAKE_CASE style (aka CONST_CASE).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> screaming_snakecase("hello world")
    'HELLO_WORLD'
    >>> screaming_snakecase("helloHTMLWorld", True, ["HTML"])
    'HELLO_HTML_WORLD'
    """
    return constcase(text, acronyms)


def dotcase(text, acronyms=None):
    """Return text in dot.case style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> dotcase("hello world")
    'hello.world'
    >>> dotcase("helloHTMLWorld", True, ["HTML"])
    'hello.html.world'
    """
    words, _, _ = case_parse.parse_case(text, acronyms)
    return '.'.join([w.lower() for w in words])


def separate_words(text, acronyms=None):
    """Return text in "seperate words" style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> separate_words("HELLO_WORLD")
    'HELLO WORLD'
    >>> separate_words("helloHTMLWorld", True, ["HTML"])
    'hello HTML World'
    """
    words, _, _ = case_parse.parse_case(text, acronyms, preserve_case=True)
    return ' '.join(words)


def slashcase(text, acronyms=None):
    """Return text in slash/case style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> slashcase("HELLO_WORLD")
    'HELLO/WORLD'
    >>> slashcase("helloHTMLWorld", True, ["HTML"])
    'hello/HTML/World'
    """
    words, _, _ = case_parse.parse_case(text, acronyms, preserve_case=True)
    return '/'.join(words)


def backslashcase(text, acronyms=None):
    """Return text in backslash\case style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> backslashcase("HELLO_WORLD") == r'HELLO\WORLD'
    True
    >>> backslashcase("helloHTMLWorld", True, ["HTML"]) == r'hello\HTML\World'
    True
    """
    words, _, _ = case_parse.parse_case(text, acronyms, preserve_case=True)
    return '\\'.join(words)
