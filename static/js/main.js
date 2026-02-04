// 🚀 ГЛАВНЫЙ ФАЙЛ JS

import { ThemeManager } from './modules/theme.js';
import { SearchManager } from './modules/search.js';
import { CardAnimator } from './modules/cards.js';

document.addEventListener('DOMContentLoaded', function() {
    // Инициализация модулей
    new ThemeManager();
    new SearchManager();
    new CardAnimator();

    // Общие функции
    initTooltips();
    initAlerts();
    initSmoothScroll();
});

// Инициализация тултипов
function initTooltips() {
    const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltips.forEach(el => new bootstrap.Tooltip(el));
}

// Автоскрытие алертов
function initAlerts() {
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
}

// Плавный скролл
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });
}

// Глобальные функции
window.copyToClipboard = function(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Скопировано в буфер обмена!', 'success');
    }).catch(() => {
        // Fallback для старых браузеров
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        showNotification('Скопировано в буфер обмена!', 'success');
    });
};

window.showNotification = function(message, type = 'info') {
    // ... существующий код ...
};
