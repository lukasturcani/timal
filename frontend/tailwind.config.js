/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "media",
  mode: "all",
  content: [
    "./src/**/*.{rs,html,css}",
    "./dist/**/*.html",
    ".node_modules/flowbite/**/*.js",
    "./assets/**/*.{html,css}",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin"),
  ],
};
