#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------#
#	delosemre.xyz	 	#
#delosemre.outlook.com	#
# twitter: @delosemre	#
# imstagram: @delosemree@
#-----------------------#

from urllib2 import *


menu = """

                                                
  (         (                                   
  )\ )   (  )\            (     )    (      (   
 (()/(  ))\((_) (   (    ))\   (     )(    ))\  
  ((_))/((_)_   )\  )\  /((_)  )\  '(()\  /((_) 
  _| |(_)) | | ((_)((_)(_))  _((_))  ((_)(_))   
/ _` |/ -_)| |/ _ \(_-</ -_)| '  \()| '_|/ -_)  
\__,_|\___||_|\___//__/\___||_|_|_| |_|  \___|.xyz v1.0
delosemre@delosemre.xyz | delosemre@outlook.com                                         
	
#############Bilgi Toplama Aracı#################.
|                                                .
|	1-) Whois                                .
|	2-) DNS Lookup                           .
|	3-) Ters DNS Arama                       .
|	4-) DNS Ana Bilgisayar Kayıtlarını Bulma .
|	5-) Paylaşılan DNS Sunucularını Bulma    .
|	6-) Zone Transfer                        .
|	7-) TCP Port Tarama                      .
|	8-) Çıkış                                .
|________________________________________________.
"""






print (menu)






print("")
secim = raw_input("    " + "delosemre" + "" "\033[1;91m@delosemre:~$\033[1;m ")
print("")



if secim == "1":
    url = raw_input("	Alan Adı Veya IP Adres: ")
    who = "http://api.hackertarget.com/whois/?q=" + url
    pwho = urlopen(who).read()
    print (pwho)
    print (menu)
    secim = raw_input("    " + "delosemre" + "" "\033[1;91m@delosemre:~$\033[1;m ")


if secim == "2":
	url = raw_input("	Alan Adı Veya IP Adres: ")
	dnsl = "http://api.hackertarget.com/dnslookup/?q=" + url
	pdnsl = urlopen(dnsl).read()
	print (pdnsl)
	if "cloudflare" in pdnsl:
				print ("cloudflare Tespit")
   	else:
   				print ("cloudflare Koruması Yok")
   	print (menu)
	secim = raw_input("    " + "delosemre" + "" "\033[1;91m@delosemre:~$\033[1;m ")
    


if secim == "3":
	url = raw_input("	DNS: ")
	dns = "https://api.hackertarget.com/reversedns/?q=" + url
	pdns = urlopen(dns).read()
	print (pdns)
	print (menu)
	secim = raw_input("    " + "delosemre" + "" "\033[1;91m@delosemre:~$\033[1;m ")
    

if secim == "4":
	url = raw_input("	Alan Adı: ")
	host = "https://api.hackertarget.com/hostsearch/?q=" + url
	phost = urlopen(host).read()
	print (phost)
	print (menu)
	secim = raw_input("    " + "delosemre" + "" "\033[1;91m@delosemre:~$\033[1;m ")
    

if secim == "5":
	url = raw_input("	DNS Adı: ")
	dnsa = "https://api.hackertarget.com/findshareddns/?q=" + url
	pdnsa = urlopen(dnsa).read()
	print (pdnsa)
	print (menu)
	secim = raw_input("    " + "delosemre" + "" "\033[1;91m@delosemre:~$\033[1;m ")
    

if secim == "6":
	url = raw_input("	Alan Adı: ")
	zone = "https://api.hackertarget.com/zonetransfer/?q=" + url
	pzone = urlopen(zone).read()
	print (pzone)
	print (menu)
	secim = raw_input("    " + "delosemre" + "" "\033[1;91m@delosemre:~$\033[1;m ")
    

if secim == "7":
	url = raw_input("	Ip Adresi Giriniz: ")
	tcp = "https://api.hackertarget.com/nmap/?q=" + url
	ptcp = urlopen(tcp).read()
	print (ptcp)
	print (menu)
	secim = raw_input("    " + "delosemre" + "" "\033[1;91m@delosemre:~$\033[1;m ")

if secim == "8":
	print ("Güle GÜle")
	quit()
	