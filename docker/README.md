# Pasos para inicializar el docker:

Para correr el docker de forma local importándolo desde docker hub, correr el siguiente comando:

`
docker run --rm -it \
-v $pwd:/home/jovyan/work  \
-p 8888:8888 \
--entrypoint "/bin/bash" \
rafaelortega123972/delitos_cdmx:v2
`



1. 
  docker build $(pwd) --force-rm -t rafaelortega123972/delitos_cdmx:v1

2. 
  docker run --rm -it \                                               
-v /home/rafaelortega/Documentos/nuevo_repo_proj_erick:/home/jovyan/work  \
-p 8887:8888 \
--entrypoint "/bin/bash" \
rafaelortega123972/delitos_cdmx:v1

docker run --rm -it \                                               
-v $pwd:/home/jovyan/work  \                                               
-p 8888:8888 \
--entrypoint "/bin/bash" \
rafaelortega123972/delitos_cdmx:v1
  
3. 
  docker login

4. push de la imagen
  docker image push rafaelortega123972/mno_final_proj:v2

