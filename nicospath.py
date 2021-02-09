import nicos
import os

class NicosPath:

 @staticmethod
 def root():

     nicos_root = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(nicos.__file__))))
     newPath = nicos_root.replace(os.sep, '/')
     print('nicos_root='+newPath)
     return newPath

 @staticmethod
 def live_png():
     lvg =  os.path.join(NicosPath.root(),'bin/data/live_lin.png')
     return lvg.replace(os.sep,'/')



