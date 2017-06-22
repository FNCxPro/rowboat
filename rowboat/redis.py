from __future__ import absolute_import

import os
import redis

ENV = os.getenv('ENV', 'local')

rdb = redis.Redis(db=0, host='redis')
