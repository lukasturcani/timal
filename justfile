# list all recipes
default:
  @just --list

# install dependencies
setup:
  cd frontend && npm install
  ln -sf ../node_modules/flowbite/dist/flowbite.min.js frontend/assets/flowbite.min.js

# watch tailwind
watch-tailwind:
  cd frontend && npx tailwindcss -i ./input.css -o ./assets/tailwind.css --watch

# watch dioxus
watch-dioxus:
  cd frontend && dx serve
