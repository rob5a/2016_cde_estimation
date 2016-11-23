# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:27:17 2016

@author: S. Bertrand
"""

import numpy as np
import donnees



# import des mesures réalisées avec le robot immobile
mesuresAuRepos = donnees.MesuresAuRepos()


# pour accéder aux données de temps, de mesures de position ou de vitesse : 
# mesuresAuRepos.temps
# mesuresAuRepos.position
# mesuresAuRepos.vitesse

# pour un affichage des mesures de position ou de vitesse :
# mesuresAuRepos.plotVitesse()
# mesuresAuRepos.plotPosition()



# calcul des moyennes et écarts type des bruits sur les mesures de vitesse et de position
# ********** 
#   A COMPLETER EN TD 
# **********