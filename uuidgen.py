#!/usr/bin/env python
# http://serverfault.com/questions/103359/how-to-create-a-uuid-in-bash
# Changed to string type and upper() for similar output as /usr/bin/uuidgen on OSX
# UUID=$(cat /proc/sys/kernel/random/uuid) (poor man's choice on Linux)
import uuid
print str(uuid.uuid1()).upper()
