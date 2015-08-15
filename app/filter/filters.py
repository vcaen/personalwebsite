from jinja2 import evalcontextfilter
import re
from markupsafe import Markup
from app.main import app


@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    _paragraph_re = re.compile(r'(?:\r\n|\r(?!\n)|\n){2,}')
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace(u'\n', Markup('<br>\n'))
                                         for p in _paragraph_re.split(value))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
