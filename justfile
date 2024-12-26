# list all recipes
default:
  @just --list

# install dependencies
setup:
  npm install
  ln -sf ../node_modules/flowbite/dist/flowbite.min.js assets/flowbite.min.js
