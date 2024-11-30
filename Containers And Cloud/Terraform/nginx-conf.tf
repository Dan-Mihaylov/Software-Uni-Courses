terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

resource "docker_image" "nginxdemos" {
  name = "nginxdemos/hello"
}

resource "docker_container" "nginx_demo" {
  name = "nginx_demo"
  image = docker_image.nginxdemos.image_id
  ports {
    external = 8000
    internal = 80
  }
}
