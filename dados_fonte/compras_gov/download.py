import sys
# insert at 1, 0 is the script path (or '' in REPL)
from utils.compras_gov import download

import pandas as pd
import numpy as np
import itertools
import shutil
from google.colab import drive
from google.colab import files

print('--------------------- Orgãos do DF ---------------------')

dfOrgaos = pd.DataFrame(
    download.cria_dataframe(
        url='licitacoes/v1/orgaos.json?nome=Distrito+federal',
        nome='Orgaos'
    )
)

dfOrgaos.head()