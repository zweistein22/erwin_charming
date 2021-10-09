### Nicos configuration for interfacing with the [CHARMing software suite](https://github.com/zweistein-frm2/CHARMing) entangle devices

### Installation:  
- copy files into the directory <nicos_root>/nicos_mlz/erwin_charming
- you must set permissions for : chmod +x  /<nicos_root>  && chmod +x  /<nicos_root>/pid chmod +x  /<nicos_root>/bin/data 
- several pip packages have to be installed, please see [entangle-install-charming.cpp](https://github.com/zweistein-frm2/CHARMing/raw/master/entangle-install-charming/entangle-install-charming.cpp) 
### Run: 
- cd /<nicos_root>/nicos_mlz/erwin_charming 
- python3 erwin-loader.py
