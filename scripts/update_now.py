#!/usr/bin/env python3
from common.params import Params
import datetime
params = Params()
t = datetime.datetime.utcnow().isoformat()
params.put("LastUpdateTime", t.encode('utf8'))
