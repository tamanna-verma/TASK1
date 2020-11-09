import os,json
from requests import get


def Hadoop():
     print("Setting up Hadoop on your LinuxOS\n 1. Installing jdk")
     os.system('yum install jdk-8u171-linux-x64.rpm')
     print("2. Installing Hadoop version-1")
     os.system('yum install hadoop-1.2.1-1.x86_64.rpm  --force')
     print('Hadoop setup complete')

     print("""1. Configure Hadoop as a namenode
     2. Configure Hadoop as datanode
     3. Configure Hadoop as a client node""")

     i = int(input("enter your choice:"))

     if i == 1:
        print(" Configuring Hadoop as a namenode")
		# getting public through external api in json format
        ip=json.loads(get('https://api.ipify.org?format=json').text)
        ip=ip['ip']
        #ip = str(input(" Enter Master's IP:"))
        with open('/etc/hadoop/core-site.xml', 'w+') as file:
            str = "<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip+":9001</value>\n</property>\n"
            file.write(str)

        with open('/etc/hadoop/hdfs-site.xml', 'w+') as file:
            str = "<property>\n<name>dfs.name.dir</name>\n<value>/nn1</value>\n</property>\n"
            file.write(str)
			
		os.system("hadoop namenode -format")
        os.system('hadoop-daemon.sh  start namenode')
        

     if i == 2:
        print(" Configuring Hadoop as a datanode")
        ip = str(input(" Enter Master's IP:"))
        with open('/etc/hadoop/core-site.xml', 'w+') as file:
            str = "<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip+":9001</value>\n</property>\n"
            file.write(str)

        with open('/etc/hadoop/hdfs-site.xml', 'w+') as file:
            str = "<property>\n<name>dfs.data.dir</name>\n<value>/dn1</value>\n</property>\n"
            file.write(str)

        os.system('hadoop-daemon.sh  start datanode')

     if i == 3:
        print(" Configuring Hadoop as a client node")
        ip = str(input(" Enter Master's IP:"))
        with open('/etc/hadoop/core-site.xml', 'w+') as file:
            str = "<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip+":9001</value>\n</property>\n"
            file.write(str)



def Docker():
	print("""1.ConFigure Docker On  Your OS
	2.TO stop docker
	3.To start docker
	4.To launching Container
	5. To start and attach container (it is for already existed container)
	6. to stop container
	7. To check how many container is running
	8. To check how many container is present in your docker(either stopped or running)
	9. To Delete/ Remove the container 	
		""")
	os.system("tput setaf 7")
	i_n = int(input("enter your choice:"))

	#os.system("gedit")
	if i_n == 1:
		os.system("tput setaf 2")
		print("""1.For ConFiguring  Docker On  Your OS.
				there are some steps required to do
				Step 1.Check for Docker repo if not there then add
				step 2.Install docker 
				step 3.Start docker service
			  
			 """)
		os.system("tput setaf 7")
		print("now 1st step started....")
		print("checking for docker repo...")
		os.system("yum repolist")
		check = input("see there is any repo of docker if yes then type y or Y and if no then type n or N")
		if check == "N" or check == "n" :
			
			a = input("""copy this and paste it when editor will open .
	[docker123]
	baseurl=http://download.docker.com/linux/centos/7/x86_64/stable/
	gpgcheck=0

	if copied then press any key:""")
			os.system("cd //etc//yum.repos.d && gedit docker1.repo")
		print("step 1 completed!")
		print("moving to step 2nd ")
		print("step 2 started...")
		print("if there ask for y/n then press y")
		os.system("yum install docker-ce --nobest")
		print("2nd step completed")
		print("step 3 starting docker service")
		os.system("systemctl enable docker")
		print("step 3rd completed")
		print("your docker configured!")
	elif i_n == 2:
		os.system("systemctl stop docker")
	elif i_n == 3:
		os.system("systemctl start docker")
	elif i_n == 4:
		print("""for launching the container/Os:-
				there are some step to follow 
				1.download the container
				2.Install and Run the container 
				""")
		print("step1 begins....")
		os_name = input("which container/os do you want to download enter name:")
		p = "docker pull " +os_name
		os.system(p)
		print("step 1 completed")
		print("-----------------------------------------------------")
		print("step2 begins....")
		os_= input("which container/os do you want to launch enter name : version(e.g: centos:8,ubuntu 14.04):")
		os_name = input("Enter your Container name :")
		p = "docker run -it --name " +os_name+" "+os_
		os.system(p)
		print("step 2 completed")
		print("-----------------------------------------------------")
	elif i_n == 5:
		os_name = input("Enter your Container name :")
		p = "docker start " + os_name
		os.system(p)
		p = "docker attach " + os_name
		os.system(p)
	elif i_n == 6:
		os_name = input("Enter your Container name :")
		p = "docker stop " + os_name
		os.system(p)
	elif i_n == 7:
		os.system("docker ps")
	elif i_n == 8:
		os.system("docker ps -a")
	elif i_n == 9:
		ask = input("You have to know Container ID to remove It, Do you know Container ID(y/n): ")
		if ask == "y":
			os_name = input("Enter your Container ID:")
		else:
			os.system("docker ps -a")
			pr=input("Which container do you want to remove and Copy the Id of container,If copied then press any key:")
			os_name = input("Enter your Container ID:")
			
		p = "docker rm " + os_name
		os.system(p)
	else:
		print("Invalid choice!")



def Web_server():
	i = int(input("1.ConFigure webserver:"))
	if i == 1:
		print("There are some step to configuring webserver:") 
		print("step1. To Install httpd\nstep2.start httpd service. \nstep3.To changing directory (/var/www/html) and create a file.\nstep4. To Stop firewall")
		print("step1 begins....")
		print("---------------------------------------------------")
		os.system("yum install httpd")
		print("step1 completed!")
		print("---------------------------------------------------")
		print("step2 begins....")
		os.system("systemctl start httpd")
		print("step2 completed!")
		print("---------------------------------------------------")
		print("step3 begins....")
		pr=input("""if you don't know about html dont worry just copy it and paste in opening file and save it:
	<h1>Welcome to webserver</h1>
	<body bgcolor='aquablue' >
	<p>Your webserver is configured! </p>

	if you copied then press any key:""")
		os.system("cd //var//www//html && gedit r.html")
		print("step3 completed!")
		print("---------------------------------------------------")
		print("step4 begins....")
		os.system("systemctl stop firewalld")
		print("step4 completed!")
		print("---------------------------------------------------")
		ip = input("you you want to access this file then open your browser put : http://ip_of_youe_system/r.html in search box.if you do not know ip then press n:") 
		if ip == 'n':
			print("see your ip and access by http://ip_of_youe_system/r.html in search box in your browser")
			os.system("ifconfig enp0s3")



def Aws():
	print("""
1.ConFigure aws CLI On  Your OS
2.TO login to Aws by IAM user To do anything on AWS.
3.To create a key pair
4.To describe instances
5.To create Security Group 
6.To Create new Instance 
7.To Create EBS/hard disk volume 
8.To attach the EBS/HARD DISK to Instance
9. To Detach the EBS/HARD DISK to Instance	
10.To create a S3 bucket
11.To Create Cloudfront Distribution
12.To start the Instance
13.To stop the Instance
14.To Terminate the Instance
15.
16.
		""")
	i = int(input("Enter your choice"))
	if i == 1:
		print("configuring the AWS CLI.........")
		os.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" ')
		os.system('unzip awscliv2.zip')
		os.system('sudo ./aws/install')
		
		print("Completed!")
		print("your AWS CLI is configured!")
	
	elif i == 2:
		print("you need access ID and access key to login :")
		os.system("aws configure")
	
	elif i == 3:
		keyname = input("Enter the name of key pair")
		os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
		print("keypair created successfully!")
	
	elif i == 4:
		os.system("describe-instances")
	
	elif i == 5:
            groupname=input("Enter the name of security group:  ")
            groupdescription=input("Enter the description you want to give to your security group :  ")
            os.system("aws ec2 create-security-group --group-name {} --description {}".format(groupname,groupdescription))
	
	elif i == 6:
            imageid=input("Enter the image id: ")
            instance_type=input("Enter the instance type you want to have: ")
            instance_number=input("Enter the number of instances you want to create: ")
            subnet_id=input("Enter the subnet id: ")
            security_group=input("Enter the ids of security groups you want to provide: ")
            keyname=input("Enter the key pair you want to give: ")
            os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}".format(imageid,instance_type,instance_number,subnet_id,security_group,keyname))
	
	elif i ==7:
            avail_zone=input("Enter the availability zone you want to launch the ebs volume in")
            size=input("Enter the size of ebs volume")
            os.system("aws ec2 create-volume --availability-zone {} --size {} --volume-type gp2".format(avail_zone,size))
		

	elif i ==8:
            instance_id=input("Enter the id of instance to which you want to attach an ebs volume:  ")
            volume_id=input("Enter the id of the volume that you want to attach to the instance:  ")
            os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volume_id,instance_id))
	
	elif i == 9:
            volume_id=input("Enter the id of the volume that you want to detach:  ")
            os.system("aws ec2 detach-volume --volume-id {}".format(volume_id))

	elif i == 10:
	    name=input("Enter the name you want to give to the new s3 bucket(it should be unique):")
            os.system("aws s3 mb s3://{}".format(name))
	
	elif i == 11:
            bucketname=input("Enter the s3 bucket name")
            os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucketname))
	
	elif i == 12:
	    instance_id=input("Enter the id of instance which you want to start:  ")
            os.system("aws ec2 start-instances --instance-ids {}".format(instance_id))
	
	elif i == 13:
            instance_id=input("Enter the id of instance which you want to stop:  ")
            os.system("aws ec2 stop-instances --instance-ids {}".format(instance_id))
	
	elif i ==14:
	    instance_id=input("Enter the id of instance which you want to terminate:  ")
            os.system("aws ec2 terminate-instances --instance-ids {}".format(instance_id))
	
	else:
            print("you have selected",i,"this is not in option")
            print("invalid selection!")		
	
        
def Partitions():
    print("""
    \n
    Press 1 : To show all partitions
    Press 2 : To create a physical volume
    Press 3 : To display all the physical volume
    Press 4 : To create a volume group
    Press 5 : To display all the volume groups
    Press 6 : To create a lv partition
    Press 7 : To display all the lv partitions
    Press 8 : To format the partition
    Press 9 : To mount the partition
    Press 10 : To resize a lv partition
    Press 11 : To format only the resized partition
    """)
    ch = input("Enter your choice:")

    if int(ch)==1:
	os.system("fdisk -l")
    elif int(ch)==2:
	disk1= input("Enter disk name:")
	disk2= input("Enter disk name:")
	os.system("pvcreate {} {}".format(disk1,disk2))
    elif int(ch)==3:
	os.system("pvdisplay")
    elif int(ch)==4:
	vg= input("Enter volume group name:")
	diskvg1= input("Enter disk to create vg with:")
	diskvg2= input("Enter disk to create vg with:")
	os.system("vgcreate {} {} {}".format(vg,diskvg1,diskvg2))
    elif int(ch)==5:
	os.system("vgdisplay")
    elif int(ch)==6:
	lv= input("Enter vg name:")
	size= input("Enter size of the lv to create:")
	name= input("Enter name of the lv:")
	os.system("lvcreate --size {} --name {} {}".format(size,name,lv))
    elif int(ch)==7:
	os.system("lvdisplay")
    elif int(ch)==8:
	dir= input("Enter the location to be formatted:")
	os.system("mkfs.ext4 {}".format(dir))
    elif int(ch)==9:
	mount= input("Enter a partition to mount:")
	node= input("Enter a dir to mount:")
	os.system("mount {} {}".format(mount,node))
    elif int(ch)==10:
	um= input("Enter partition to unmount:")
	dis= input("Enter disk name to resize again:")
	os.system("umount {}".format(um))
	os.system("fdisk {}".format(dis))
    elif int(ch)==11:
	di= input("Enter partition to examine filesystems and format:")
	os.system("e2fsck -f {}".format(di))
	os.system("resize2fs {}".format(di))
    else:
	print("Enter valid number")














		
os.system("tput setaf 1")
print("			Welcome to my Menu !!")
os.system("tput setaf 2")
print("-----------------------------------------------------")
print("1.Docker\n2.Web server\n3.Hadoop\n4.Linux command\n5.Partitions")
i = int(input("Enter your choice where do you want to perform task:"))
if i == 1:
	Docker()
elif i ==2:
	Web_server()
elif i == 3:
	Aws()
elif i == 4:
	Hadoop()
elif i == 5:
        Partitions()
else:
	print("you have selected",i,"this is not in option")
	print("invalid selection!")		

	
