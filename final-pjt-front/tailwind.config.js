// tailwind.config.js
const colors = require('tailwindcss/colors');
module.exports = {
	purge: ['./public/**/*.html', './src/**/*.vue'],
	darkMode: false, // or 'media' or 'class'
	theme: {
		colors,
		extend: {
			// colors,
			colors: {
				themeyellow: '#FFE14E',
				themeBlue: '#38BDF8',
			},
		},
	},
	variants: {
		extend: {},
	},
	plugins: [],
};
