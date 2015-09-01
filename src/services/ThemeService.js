import {THEMES} from '../utils/Constant.js';

export default {
    getThemes() {
        return THEMES;
    },

    getCurrentTheme() {
        let theme = localStorage.getItem('theme');
        return theme ? theme : THEMES[0];
    },

    setTheme(theme) {
        localStorage.setItem('theme', theme);
        return theme;
    }
}