import pathlib

def test_layout_css_variables():
    css = pathlib.Path('theme/layout.css').read_text()
    assert '--columns: 12;' in css
    assert '@media (max-width: 768px)' in css
