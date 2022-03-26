import re

endereco = 'Rua teste, 999, jd. Teste 11200-909, Norteínea - BG'

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
#[0-9]{5}   -> define that the first 5 digitis ({5} are number (interval between 0 and 9 [0-9])
# [-]{0,1}  -> define that hifen will appear none or at least one time. It can be replace by [-]?
# [0-9]{3}  -> define that the first 5 digitis ({3} are number (interval between 0 and 9 [0-9])
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)

