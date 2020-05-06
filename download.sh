wget http://revistas.inpi.gov.br/txt/$1$2.zip --directory-prefix=/home/ubuntu/inpi_extract/revistas/

unzip revistas/$1$2.zip -d /home/ubuntu/inpi_extract/revistas/

sleep 3