import argparse
import boto.ec2
from pprint import pprint
from boto import ec2
import json
import requests

access_key = ''
secret_key = ''
active = [];
listall = [];
import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/var/log/myapp.log')
formatter=logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#formatter = logging.Formatter('%(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)

def get_ec2_instances(region):
    ec2_conn = boto.ec2.connect_to_region(region,aws_access_key_id=access_key,aws_secret_access_key=secret_key)
    reservations = ec2_conn.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    for reservation in reservations:
         for instances in reservation.instances:
              if instances.state == "running":
                   x=str(instances.private_ip_address)
                   if x!="10.0.4.142":
                        listall.append(x)


def activeAgent():
    base_url = 'https://127.0.0.1:55000'
    auth = requests.auth.HTTPBasicAuth('foo', 'bar')
    verify = False

    url = '{0}{1}'.format(base_url, "/agents?status=Active")
    r = requests.get(url, auth=auth, params=None, verify=verify)
    x=json.dumps(r.json(), sort_keys=True)
    jsonResponse=json.loads(x)
    jsonData=jsonResponse["data"]
    for item in jsonData:
        name = item.get("name")
        result=str(name)
        if result !="ids-server":
            x=result.split('-')[1]
            active.append(x)

def diff():
    for elem in listall:
         if elem not in active:
              logger.error(elem)
              print elem

def main():
    regions = ['us-east-1','us-west-1','us-west-2','eu-west-1','sa-east-1',
                'ap-southeast-1','ap-southeast-2','ap-northeast-1']
    parser = argparse.ArgumentParser()
    parser.add_argument('access_key', help='Access Key');
    parser.add_argument('secret_key', help='Secret Key');
    args = parser.parse_args()
    global access_key
    global secret_key
    access_key = args.access_key
    secret_key = args.secret_key
    activeAgent()

    for region in regions: get_ec2_instances(region)
#    print active
 #   print listall
  #  print "Not Connected"
    diff()

if  __name__ =='__main__':main()
