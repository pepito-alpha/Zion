#Delete todos los files *.so
rm *.so
echo "Hello Luiso"
echo "\n does it work?"
#Compilando el file searposi.f90 y creando el file play.so
f2py -c SearPosi.f90 -m play
#running el program main.py 
python main.py
echo "adios, a todos"