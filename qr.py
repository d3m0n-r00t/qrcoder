from qrtools import QR
import sys
import os
from optparse import OptionParser 
import datetime

def qr_encode(option, opt_str, value, parser):
	text=sys.argv[2]
	img=QR(data=text,pixel_size=10)
	img.encode()
 	os.system("mv "+img.filename+" ~/Desktop/qr_"+datetime.datetime.now().strftime("%d%m%Y_%H%M%S")+".png")
 	print("File is saved in Desktop")


def qr_decode(option, opt_str, value, parser):
	file=sys.argv[2]
	img=QR(filename=file)
	img.decode()
	print("Decode Complete")
	print(img.data)	


def main():
	parser=OptionParser(usage="usage: qr.py [options] required text / filepath")
	parser.add_option("-e", "--encode",action="callback",callback=qr_encode,help="Encode the given text into QR code.",metavar="Text")
	parser.add_option("-d","--decode",action="callback",callback=qr_decode,help="Decode the given QR code.",metavar="FILE")
	(options, args)=parser.parse_args()


if __name__=="__main__":
	main()


