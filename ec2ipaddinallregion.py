import boto3
import csv
from pprint import pprint

ec2_client=boto3.client('ec2')

# Get all regions
all_regions=[]
for each_region in ec2_client.describe_regions()['Regions']:
    all_regions.append(each_region['RegionName'])
print (all_regions)

print(f'instance_id,Region,PrivateIP,PublicIP')
count=1
for each_region in all_regions:
    ec2_resource=boto3.resource('ec2',region_name=each_region)
    for each_instance_in_region in ec2_resource.instances.all():
        print(count,each_instance_in_region.instance_id,each_instance_in_region.RegionName,each_instance_in_region.private_ip_address,each_instance_in_region.public_ip_address)
        count+=1


