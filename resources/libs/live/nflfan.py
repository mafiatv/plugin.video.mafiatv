import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main
import re,sys

#MafiaTV

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.mafiaTV'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.mafiaTV', sys.argv)
art = main.art

def NFLMAIN():
    link=main.OPENURL('http://www.nfl.com/feeds-rs/videos/byChannel/nfl-videos.json')
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.findall('(?sim)"headline":"([^"]+)".+?"mediumImageUrl":"([^"]+)".+?"videoPath":"([^"]+)","bitrate":3000000',link)
    for name,thumb,url in match:
        main.addPlayc(name,url,183,thumb,'','','','','')
        
