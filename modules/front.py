import string
import random

from flask import request, session

from modules.accounts import paste_csrf
from utils.db import db


def most_viewed():
    sql = "SELECT V.views, P.paste_id, P.title FROM pastes P LEFT JOIN paste_views V " \
          "ON P.paste_id = V.paste_id WHERE P.private=false ORDER BY V.views DESC LIMIT 100"
    result = db.session.execute(sql)
    return result.fetchall()


def create_paste():
    content = request.form["paste"]
    syntax = syntax_dict(request.form.get("syntax-choice", "Plain text"))
    if len(content) == 0:
        return "empty"
    private = True if request.form["visibility"] == "Private" else False
    burn = True if request.form.get("burn") == "on" else False
    paste_id = "".join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=80 if private else 8))
    title = content[:25]
    username = session.get("username", "Anonymous")
    if paste_csrf():
        username = "Anonymous"
    sql = "INSERT INTO pastes (paste_id, paste, username, title, private, burn, syntax, time) " \
          "VALUES (:paste_id, :paste, :username, :title, :private, :burn, :syntax, NOW())"
    db.session.execute(sql,
                       {"paste_id": paste_id, "paste": content, "username": username, "title": title,
                        "private": private, "burn": burn, "syntax": syntax})
    db.session.commit()
    return paste_id


def syntax_dict(syntax):
    values = {"Plain text": "none",
              "HTML": "html",
              "XML": "xml",
              "SVG": "svg",
              "MathML": "mathml",
              "SSML": "ssml",
              "RSS": "rss",
              "CSS": "css",
              "C-like": "clike",
              "JavaScript": "js",
              "ABAP": "abap",
              "ABNF": "abnf",
              "AL": "al",
              "ANTLR4": "antlr4",
              "Apache Configuration": "apacheconf",
              "APL": "apl",
              "AQL": "aql",
              "Arduino": "ino",
              "ARFF": "arff",
              "AsciiDoc": "asciidoc",
              "ASP.NET (C#)": "aspnet",
              "6502 Assembly": "asm6502",
              "Atmel AVR Assembly": "asmatmel",
              "AutoHotkey": "autohotkey",
              "AutoIt": "autoit",
              "AviSynth": "avisynth",
              "Avro IDL": "avro-idl",
              "BASIC": "basic",
              "BBcode": "bbcode",
              "BNF": "bnf",
              "RBNF": "rbnf",
              "BSL (1C": "bsl",
              "OneScript": "oscript",
              "C#": "csharp",
              "C++": "cpp",
              "CFScript": "cfscript",
              "CIL": "cil",
              "CMake": "cmake",
              "COBOL": "cobol",
              "CoffeeScript": "coffee",
              "Concurnas": "conc",
              "Content-Security-Policy": "csp",
              "CSS Extras": "css-extras",
              "CSV": "csv",
              "DataWeave": "dataweave",
              "DAX": "dax",
              "Django/Jinja2": "django",
              "DNS zone file": "dns-zone-file",
              "Docker": "dockerfile",
              "DOT (Graphviz)": "dot",
              "EBNF": "ebnf",
              "EditorConfig": "editorconfig",
              "EJS": "ejs",
              "Embedded Lua templating": "etlua",
              "ERB": "erb",
              "Excel Formula": "excel-formula",
              "F#": "fsharp",
              "Firestore security rules": "firestore-security-rules",
              "FreeMarker Template Language": "ftl",
              "GameMaker Language": "gml",
              "GAP (CAS)": "gap",
              "G-code": "gcode",
              "GDScript": "gdscript",
              "GEDCOM": "gedcom",
              "GLSL": "glsl",
              "GN": "gn",
              "Go module": "go-module",
              "GraphQL": "graphql",
              "Handlebars": "hbs",
              "Haskell": "hs",
              "HCL": "hcl",
              "HLSL": "hlsl",
              "HTTP": "http",
              "HTTP Public-Key-Pins": "hpkp",
              "HTTP Strict-Transport-Security": "hsts",
              "IchigoJam": "ichigojam",
              "ICU Message Format": "icu-message-format",
              "Idris": "idr",
              ".ignore": "ignore",
              ".gitignore": "gitignore",
              ".hgignore": "hgignore",
              ".npmignore": "npmignore",
              "Inform 7": "inform7",
              "Java": "java",
              "JavaDoc": "javadoc",
              "JavaDoc-like": "javadoclike",
              "Java stack trace": "javastacktrace",
              "JQ": "jq",
              "JSDoc": "jsdoc",
              "JS Extras": "js-extras",
              "JSON": "json",
              "Web App Manifest": "webmanifest",
              "JSON5": "json5",
              "JSONP": "jsonp",
              "JS stack trace": "jsstacktrace",
              "JS Templates": "js-templates",
              "Keepalived Configure": "keepalived",
              "Kotlin Script": "kts",
              "Kotlin": "kt",
              "KuMir (КуМир)": "kumir",
              "LaTeX": "latex",
              "TeX": "tex",
              "ConTeXt": "context",
              "LilyPond": "lilypond",
              "Lisp": "emacs",
              "LLVM IR": "llvm",
              "Log file": "log",
              "LOLCODE": "lolcode",
              "Magma (CAS)": "magma",
              "Markdown": "md",
              "Markup templating": "markup-templating",
              "MATLAB": "matlab",
              "MAXScript": "maxscript",
              "MEL": "mel",
              "MongoDB": "mongodb",
              "MoonScript": "moon",
              "N1QL": "n1ql",
              "N4JS": "n4js",
              "Nand To Tetris HDL": "nand2tetris-hdl",
              "Naninovel Script": "naniscript",
              "NASM": "nasm",
              "NEON": "neon",
              "nginx": "nginx",
              "NSIS": "nsis",
              "Objective-C": "objectivec",
              "OCaml": "ocaml",
              "OpenCL": "opencl",
              "OpenQasm": "openqasm",
              "PARI/GP": "parigp",
              "Object Pascal": "objectpascal",
              "PATROL Scripting Language": "psl",
              "PC-Axis": "pcaxis",
              "PeopleCode": "peoplecode",
              "PHP": "php",
              "PHPDoc": "phpdoc",
              "PHP Extras": "php-extras",
              "PL/SQL": "plsql",
              "PowerQuery": "powerquery",
              "PowerShell": "powershell",
              "PromQL": "promql",
              ".properties": "properties",
              "Protocol Buffers": "protobuf",
              "PureBasic": "purebasic",
              "PureScript": "purs",
              "Python": "py",
              "Q#": "qsharp",
              "Q (kdb+ database)": "q",
              "QML": "qml",
              "Racket": "rkt",
              "Razor C#": "cshtml",
              "React JSX": "jsx",
              "React TSX": "tsx",
              "Ren'py": "renpy",
              "reST (reStructuredText)": "rest",
              "Robot Framework": "robotframework",
              "Ruby": "rb",
              "SAS": "sas",
              "Sass (Sass)": "sass",
              "Sass (Scss)": "scss",
              "Shell session": "shell-session",
              "SML": "sml",
              "SML/NJ": "smlnj",
              "Solidity (Ethereum)": "solidity",
              "Solution file": "solution-file",
              "Soy (Closure Template)": "soy",
              "SPARQL": "sparql",
              "Splunk SPL": "splunk-spl",
              "SQF": "sqf",
              "SQL": "sql",
              "Structured Text (IEC 61131-3)": "iecst",
              "Systemd configuration file": "systemd",
              "T4 templating": "t4-templating",
              "T4 Text Templates (C#)": "t4-cs",
              "T4 Text Templates (VB)": "t4-vb",
              "TAP": "tap",
              "Template Toolkit 2": "tt2",
              "TOML": "toml",
              "trickle": "trickle",
              "troy": "troy",
              "TriG": "trig",
              "TypeScript": "ts",
              "TSConfig": "tsconfig",
              "UnrealScript": "uscript",
              "UO Razor Script": "uorazor",
              "URI": "uri",
              "URL": "url",
              "VB.Net": "vbnet",
              "VHDL": "vhdl",
              "vim": "vim",
              "Visual Basic": "visual-basic",
              "VBA": "vba",
              "WebAssembly": "wasm",
              "Web IDL": "web-idl",
              "Wiki markup": "wiki",
              "Wolfram language": "wolfram",
              "Mathematica Notebook": "nb",
              "XeoraCube": "xeoracube",
              "XML doc (.net)": "xml-doc",
              "Xojo (REALbasic)": "xojo",
              "XQuery": "xquery",
              "YAML": "yaml",
              "YANG": "yang"}
    if not syntax:
        syntax = "Plain text"
    return values.get(syntax, "Plain text")
