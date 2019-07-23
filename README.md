# EqualStyleLogParser

Parser for "Equal style" log like:
```
May 31 15:54:33 10.10.10.1 time="May 29 1:52:07 2017"	timezone="GMT"	vendor="Zscaler"	product="Zscaler"	hostname="aaa.example.com"	clientip="192.168.1.1"	url="aaa.example.com/test"	actual_action="Allowed"	actual_status="200"	useragent="MICROSOFT_DEVICE_METADATA_RETRIEVAL_CLIENT"	requestmethod="POST"	urlcategory="Professional Services"	requestsize="222"	responsesize="1111"	user="test@example.local"	filetype="None"	refererurl="None"	reason="Allowed"	recordid="13111111111"	clienttranstime="52"	riskscore="0"	appname="generalbrowsing"	department="Default"	md5digest="None"	clientpublicip="x.x.x.x"	filename="None"	threatcategory="None"	module="General Browsing"	nsssvcip="10.10.10.100"	protocol="HTTP"	threatname="None"
May 31 15:54:39 10.10.10.1 time="May 29 1:52:08 2017"	timezone="GMT"	vendor="Zscaler"	product="Zscaler"	hostname="aaa.example.com"	clientip="192.168.1.1"	url="aaa.example.com/test333"	actual_action="Allowed"	actual_status="200"	useragent="MICROSOFT_DEVICE_METADATA_RETRIEVAL_CLIENT"	requestmethod="POST"	urlcategory="Professional Services"	requestsize="222"	responsesize="1111"	user="test@example.local"	filetype="None"	refererurl="None"	reason="Allowed"	recordid="13111111111"	clienttranstime="52"	riskscore="0"	appname="generalbrowsing"	department="Default"	md5digest="None"	clientpublicip="x.x.x.x"	filename="None"	threatcategory="None"	module="General Browsing"	nsssvcip="10.10.10.100"	protocol="HTTP"	threatname="None"
```

you can get columns sample with `-d` switch with position number

```
% python equalStyleLogParser.py test.log -d              
1 actual_action
2 actual_status
3 appname
4 clientip
5 clientpublicip
6 clienttranstime
7 department
8 filename
9 filetype
10 hostname
11 md5digest
12 module
13 nsssvcip
14 product
15 productversion
...
...
```

you can display columns you want with `-t` switch (commna separated)

```
% python convertEqualStyle2ColStyle.py TEMP/temp.log -t time,useragent
time	useragent
May 29 01:52:07 2017	Unknown
May 29 01:52:08 2017	MICROSOFT_DEVICE_METADATA_RETRIEVAL_CLIENT
```
