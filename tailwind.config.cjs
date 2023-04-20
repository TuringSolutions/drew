/** @type {import('tailwindcss').Config} */

const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter var", ...defaultTheme.fontFamily.sans],
      },
      screens: {
        'cellphone': '640px',
        'tablet' : '768px',
        'laptop': '1280px',
        'desktop' : '1920px'
      }
    },
  },
  plugins: [],
};
