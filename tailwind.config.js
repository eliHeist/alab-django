/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/*.html', './**/templates/**/*.html', './templates/*.djhtml', './**/templates/**/*.djhtml'],
  theme: {
    extend: {
      colors: {
        primary: {
          100: '#dac8ba',
          500: '#FF7200',
          900: '#FF3D00',
        },
        secondary: {
          100: '#BDDADF',
          500: '#00e5ff',
          700: '#16bfd2',
          900: '#0d1515',
        },
        dark: {
          100: 'rgb(13, 13, 13)',
          200: 'rgb(23, 23, 23)',
          300: 'rgb(51, 51, 51)',
          400: 'rgb(110, 110, 110)',
        },
        light: {
          100: 'rgb(236, 236, 236)',
          200: 'rgb(226, 226, 226)',
          300: 'rgb(199, 199, 199)',
        },
      },
      fontFamily: {
        body: ['poppins']
      },
      strokeWidth: {
        '0': '0',
        '4': '4',
        '10': '10',
      }
    },
  },
  plugins: [],
  darkMode: 'class',
}
