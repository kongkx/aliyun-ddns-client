## aliyun-ddns-client

- relative path to `ddns.conf`
- replace `requests` moudle, use `urllib2` + `json` to fetch data, so that this client can run on dd-wrt directly.

### INSTALLATION
1. copy all files to somewhere, e,g: `/opt/aliyun-ddns-client`
2. create `ddns.conf` file in the same folder
```bash
cp ddns.conf.example ddns.conf
```
3. run `ddns.py`
```bash
cd /path/to/aliyun-ddns-client/ && python ddns.py
```
4. create a cronjob which execute `python ddns.py` periodly

### CONFIGURATION
Required options need to be set in `ddns.conf`:
* access_id
* access_key
* domain
* sub_domain
* type

Optional options:
* id
* debug
* value

```
[DEFAULT]
# access id obtains from aliyun
access_id=
# access key obtains from aliyun
access_key=
# it is not used at this moment, you can just ignore it
interval=600
# turn on debug mode or not
debug=true

[1]
# domain name, like google.com
domain=
# subdomain name, like www, blog, bbs
sub_domain=
# record id which get from DNS service provider
id=
# it can be IP address, alias to another hostname...
value=
# resolve type, 'A', 'MX'...
type=
```

### GETTING STARTED
1. Create a subdomain on net.cn manually, e,g: blog
2. You can leave any IP address on net.cn for this subdomain, like 192.168.0.120
3. Make sure all mandantory options inputted correctly in `ddns.conf`
4. Make sure `ddns.conf` can be readable and writable for the user who setup cron job

### WORK FLOW
1. When Aliyun ddns client rums first time, it will fetch subdomain record's id and save to local `ddns.conf`
2. Then it will compare current public ip with local value in `ddns.conf`, if it doesn't match, it will sync the current public ip to net.cn server
3. If sync operation done successfully, the new updated value(IP) in server side will be saved in local `ddns.conf` too

### THANKS TO ORIGIN REPO
Python DDNS client for Aliyun(http://www.guanxigo.com/netcn-ddns-client/)
