// tailwind.config.js
module.exports = {
	purge: ['./public/**/*.html', './src/**/*.vue'],
	darkMode: false, // or 'media' or 'class'
	theme: {
		colors: {
			themeyellow: '#FFE14E',
			themeBlue: '#38BDF8',
		},
		extend: {},
	},
	variants: {
		extend: {},
	},
	plugins: [],
};
