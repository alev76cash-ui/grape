// 🌙 УПРАВЛЕНИЕ ТЕМОЙ
export class ThemeManager {
    constructor() {
        this.themeToggle = document.getElementById('themeToggle');
        this.html = document.documentElement;
        this.init();
    }

    init() {
        // Восстанавливаем тему
        const savedTheme = localStorage.getItem('theme') || 'light';
        this.setTheme(savedTheme);

        // Назначаем обработчик
        if (this.themeToggle) {
            this.themeToggle.addEventListener('click', () => this.toggleTheme());
        }
    }

    setTheme(theme) {
        this.html.setAttribute('data-bs-theme', theme);

        const icon = this.themeToggle?.querySelector('i');
        if (icon) {
            icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
        }

        localStorage.setItem('theme', theme);
    }

    toggleTheme() {
        const currentTheme = this.html.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        this.setTheme(newTheme);

        // Анимация
        if (this.themeToggle) {
            this.themeToggle.style.transform = 'scale(1.2) rotate(180deg)';
            setTimeout(() => {
                this.themeToggle.style.transform = '';
            }, 300);
        }
    }
}
