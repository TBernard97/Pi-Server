import argparse
import pysftp
 
ap = argparse.ArgumentParser()

ap.add_argument("-d", "--download", required=False,
	help="Download File")

ap.add_argument("-u", "--upload", required=False,
    help="Upload File")

args = ap.parse_args()

with pysftp.Connection('S0m3_1P_0R_H0$T', username='S0m3_Dud3', password='d@Nk_Pa$$Wud') as sftp:
    if args.download is not None:
        sftp.get(args.download)

    if args.upload is not None:
        with sftp.cd("/home/pi/Public"):
            sftp.put(args.upload)