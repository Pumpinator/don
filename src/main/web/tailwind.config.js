/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["../resources/templates/**/*.{html,js}"], // it will be explained later
    theme: {
        extend: {},
        colors: {
            transparent: 'transparent',
            current: 'currentColor',
            white: '#ffffff',
            terracotta: {
                light: '#E49A84',
                DEFAULT: '#CB765E',
                dark: '#9A4D3D',
            },
            wood: {
                light: '#B78C7A',
                DEFAULT: '#A07265',
                dark: '#7E5B4A',
            },
            red: {
                light: '#F88C6A',
                DEFAULT: '#F46F4A',
                dark: '#D14A31',
            },
            latte: {
                light: '#9E8A7C',
                DEFAULT: '#75635E',
                dark: '#4E4036',
            },
            dirt: {
                light: '#6D574F',
                DEFAULT: '#4B413E',
                dark: '#3A2D27',
            },
            chocolate: {
                light: '#5D463B',
                DEFAULT: '#332722',
                dark: '#2B1E17',
            }
        }
    },
    plugins: [],
}