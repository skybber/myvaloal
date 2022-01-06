import os
from io import StringIO, BytesIO
import base64
import codecs
from lxml import etree

# TODO : parse arguments

buf = StringIO()
buf.write('<?xml version="1.0" encoding="utf-8"?>\n')
observing_sessions = ObservingSession.query.filter_by(user_id=current_user.id).all()
oal_observations = create_oal_observations(current_user, observing_sessions)
oal_observations.export(buf, 0)

# TODO : do not use ByteIO, but file

mem = BytesIO()
mem.write(codecs.BOM_UTF8)
mem.write(buf.getvalue().encode('utf-8'))
mem.seek(0)

