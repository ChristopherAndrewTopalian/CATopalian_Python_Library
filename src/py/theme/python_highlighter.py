# python_highlighter.py

from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PySide6.QtCore import QRegularExpression

class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.highlighting_rules = []

        # Keywords (Vibrant Purple/Pink)
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#c586c0"))
        keyword_format.setFontWeight(QFont.Bold)
        keywords = [
            r"\bdef\b", r"\bimport\b", r"\bfrom\b", r"\bclass\b", 
            r"\breturn\b", r"\bif\b", r"\belse\b", r"\belif\b", 
            r"\bfor\b", r"\bwhile\b", r"\btry\b", r"\bexcept\b",
            r"\bwith\b", r"\bas\b", r"\bpass\b", r"\blambda\b",
            r"\bTrue\b", r"\bFalse\b", r"\bNone\b", r"\band\b", r"\bor\b", r"\bnot\b", r"\bin\b"
        ]
        for word in keywords:
            self.highlighting_rules.append((QRegularExpression(word), keyword_format))

        # Functions & Methods (Bright Yellow)
        # Matches any word immediately followed by an opening parenthesis
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#ffff00"))
        self.highlighting_rules.append((QRegularExpression(r"\b[A-Za-z0-9_]+(?=\()"), function_format))

        # Numbers (Light Green)
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#b5cea8"))
        self.highlighting_rules.append((QRegularExpression(r"\b[0-9]+\b"), number_format))

        # Strings (Warm Orange/Brown)
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#ce9178"))
        self.highlighting_rules.append((QRegularExpression(r'".*?"'), string_format))
        self.highlighting_rules.append((QRegularExpression(r"'.*?'"), string_format))

        # Comments (Forest Green)
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6a9955"))
        self.highlighting_rules.append((QRegularExpression(r"#[^\n]*"), comment_format))

    def highlightBlock(self, text):
        """This function is automatically called by C++ every time text is rendered."""
        for pattern, text_format in self.highlighting_rules:
            iterator = pattern.globalMatch(text)
            while iterator.hasNext():
                match = iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), text_format)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

