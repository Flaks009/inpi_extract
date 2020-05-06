wget http://revistas.inpi.gov.br/txt/$1$2.zip --directory-prefix=revistas/

unzip revistas/$1$2.zip -d revistas/

sleep 3