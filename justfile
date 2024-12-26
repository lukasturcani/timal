# list all recipes
default:
  @just --list

# install dependencies
setup:
  npm install
  ln -sf ../node_modules/flowbite/dist/flowbite.min.js assets/flowbite.min.js

# watch tailwind
watch-tailwind:
  npx tailwindcss -i ./input.css -o ./assets/tailwind.css --watch

# watch dioxus
watch-dioxus:
  dx serve
