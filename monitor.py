#!/usr/bin/env python
import subprocess
import datetime
import argparse
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

def send_email(to, message):
    """ sendmail easily available on all linux machines and doesn't require additional SMTP configuration
    """
    msg = MIMEText(message)
    msg["From"] = 'monitor@server'
    msg["To"] = to
    msg["Subject"] = 'Monitoring alert from server'
    p = Popen(["/usr/sbin/sendmail", "-t", "--oi"], stdin=PIPE)
    p.communicate(msg.as_string())

def main(command, email):
  while True:
    try:
      subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
      message =  str(datetime.datetime.utcnow()) +  ' command ' + command + ' returned exit code ' + str(e.returncode) + '. Restarting'
      print message
      send_email(email, message)

parser = argparse.ArgumentParser()
parser.add_argument('command')
parser.add_argument('email')
args = parser.parse_args()
main(args.command, args.email)
