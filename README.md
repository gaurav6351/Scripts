# README 

ListAwsRunningInstances.py

    This script list all running Instance on AWS.
    
    Command : 
    
      python ListAwsRunningInstances.py <Access Key ID> <Secret Access Key>
    
ListActiveOssecAgent.py
    
    This script list all active OSSEC agent:
    
    Command:
    
      python ListActiveOssecAgent.py
      
OssecAgentAutoSetup.sh

    This script will Install Ossec Agent without any user intervention and add it to Ossec Server:
    
    Command:
    
      ./OssecAgentAutoSetup.sh
      
GetAwsLog.py
    
    This script will download cloudtrail log from s3 bucket on your local machine.Here we are using Boto module of Python. so give your
    AWS information in /etc/boto.cfg
    
    [Credentials]
    aws_access_key_id = ''	 
    aws_secret_access_key = ''

    Command:
    
      python /home/ubuntu/getawslog.py -b <bucketName> -d -j -D -l /mnt/amazon.log
      
RunningButNotConnectedInstanceAWS.py

    This script will give the list of running Instance of AWS which are not connected to Ossec .
   
    Command:
   
       python RunningButNotConnectedInstanceAWS.py <accessKey> <secretKey>
