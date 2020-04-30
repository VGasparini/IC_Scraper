# Instalando virtualenv (encapsulador de ambiente)

`sudo pip3 install virtualenv`

# Configurando ambiente

`virtualenv env`

# Ativando env (necessário toda vez que for usar)

`source env/bin/activate`

# Instalando biblioteca (só no primeiro uso)

`pip3 install scrapy`

# Desativar env

`deactivate`

# Rodando

`scrapy runspider sbbd_15_years/sbbd_15_years/spiders/extract_count.py -o sbbd_15_years/sbbd_15_years/data/raw/count.json`
