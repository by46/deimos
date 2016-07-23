#!/bin/sh

IMAGE=$(sirius docker_image_name | head -n 1)

docker tag -f ${IMAGE} docker.neg/${IMAGE}

docker push docker.neg/${IMAGE}

sirius docker_deploy:deimos,${IMAGE},server=scdfis01,ports="9200;8080"
