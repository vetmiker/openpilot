#!/usr/bin/env python3.7
import cereal.messaging as messaging
import os
import time
import datetime
import signal
import threading

GPX_LOG_PATH = '/sdcard/gpx_logs/'

LOG_DELAY = 0.1 # secs, lower for higher accuracy, 0.1 seems fine
LOG_LENGTH = 30 # mins, higher means it keeps more data in the memory, will take more time to write into a file too.
LOST_SIGNAL_COUNT_LENGTH = 30 # secs, if we lost signal for this long, perform output to data
MIN_MOVE_SPEED_KMH = 5 # km/h, min speed to trigger logging

# do not change
LOST_SIGNAL_COUNT_MAX = LOST_SIGNAL_COUNT_LENGTH / LOG_DELAY # secs,
LOGS_PER_FILE = LOG_LENGTH * 60 / LOG_DELAY # e.g. 3 * 60 / 0.1 = 1800 points per file
MIN_MOVE_SPEED_MS = MIN_MOVE_SPEED_KMH / 3.6

class WaitTimeHelper:
  ready_event = threading.Event()
  shutdown = False

  def __init__(self):
    signal.signal(signal.SIGTERM, self.graceful_shutdown)
    signal.signal(signal.SIGINT, self.graceful_shutdown)
    signal.signal(signal.SIGHUP, self.graceful_shutdown)

  def graceful_shutdown(self, signum, frame):
    self.shutdown = True
    self.ready_event.set()

def main():
  # init
  sm = messaging.SubMaster(['gpsLocationExternal'])
  log_count = 0
  logs = list()
  lost_signal_count = 0
  wait_helper = WaitTimeHelper()
  started_time = datetime.datetime.utcnow().isoformat()
  while True:
    sm.update()
    if sm.updated['gpsLocationExternal']:
      gps = sm['gpsLocationExternal']

      # do not log when no fix, add lost_signal_count
      if gps.flags % 2 == 0:
        if log_count > 0:
          lost_signal_count += 1
      else:
        logs.append([datetime.datetime.utcnow().isoformat(), gps.latitude, gps.longitude, gps.altitude])
        log_count += 1
        lost_signal_count = 0
    '''
    write to log if
    1. reach per file limit
    2. lost signal for a certain time (e.g. under cover car park?)
    '''
    if log_count > 0 and (log_count >= LOGS_PER_FILE or lost_signal_count >= LOST_SIGNAL_COUNT_MAX):
      # output
      to_gpx(logs, started_time)
      lost_signal_count = 0
      log_count = 0
      logs.clear()
      started_time = datetime.datetime.utcnow().isoformat()

    time.sleep(LOG_DELAY)
    if wait_helper.shutdown:
      break
  # when process end, we store any logs.
  if log_count > 0:
    to_gpx(logs, started_time)

'''
write logs to a gpx file
'''
def to_gpx(logs, filename):
  if not os.path.exists(GPX_LOG_PATH):
    os.makedirs(GPX_LOG_PATH)
  with open('%s%sZ.gpx' % (GPX_LOG_PATH, filename.replace(':','-')), 'w') as f:
    f.write("%s\n" % '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>')
    f.write("%s\n" % '<gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" version="1.1">')
    f.write("\t<trk>\n")
    f.write("\t\t<trkseg>\n")
    for trkpt in logs:
      f.write("\t\t\t<trkpt time=\"%sZ\" lat=\"%s\" lon=\"%s\" ele=\"%s\" />\n" % (trkpt[0], trkpt[1], trkpt[2], trkpt[3]))
    f.write("\t\t</trkseg>\n")
    f.write("\t</trk>\n")
    f.write("%s\n" % '</gpx>')

if __name__ == "__main__":
  main()
