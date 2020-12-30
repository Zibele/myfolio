const colors = require("tailwindcss/colors")

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    
    extend: {

      fontFamily:{
        'Poppins' : ['Poppins','sans-serif'],
      },

      colors: {
        dark: "#262E33",
        turq: "#21E6C1",
        darklight: "#303A52",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
