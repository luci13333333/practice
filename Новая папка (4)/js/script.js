// Анимация появления элементов при прокрутке
window.addEventListener("scroll", reveal);

function reveal() {
    var reveals = document.querySelectorAll(".reveal");
    for (var i = 0; i < reveals.length; i++) {
        var windowheight = window.innerHeight;
        var revealtop = reveals[i].getBoundingClientRect().top;
        var revealpoint = 150;
        if (revealtop < windowheight - revealpoint) {
            reveals[i].classList.add("active");
        } else {
            reveals[i].classList.remove("active");
        }
    }
}

// Обработчики событий для ячеек
document.querySelectorAll('.profile-cell').forEach(cell => {
    cell.addEventListener('click', function() {
        this.style.transform = 'translateY(-5px)';
        setTimeout(() => {
            this.style.transform = 'translateY(0)';
        }, 200);
    });
});

// Обработчик кнопки редактирования профиля
document.querySelector('.edit-profile')?.addEventListener('click', function() {
    const phoneInput = document.querySelector('.profile-cell input[type="tel"]');
    if (phoneInput?.hasAttribute('disabled')) {
        phoneInput.removeAttribute('disabled');
        this.textContent = 'Сохранить';
    } else {
        phoneInput?.setAttribute('disabled', true);
        this.textContent = 'Редактировать профиль';
    }
});

// Обработчики навигации
document.querySelector('.nav-buttons .login')?.addEventListener('click', function(e) {
    e.preventDefault();
    window.location.href = 'login.html';
});

document.querySelector('.nav-buttons .create-account')?.addEventListener('click', function(e) {
    e.preventDefault();
    window.location.href = 'register.html';
});

// Обработка формы входа
document.getElementById('loginForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    // Здесь должна быть логика проверки учетных данных
    console.log('Вход:', { email, password });
    // После успешного входа перенаправьте на главную страницу
    window.location.href = 'index.html';
});

// Обработка формы регистрации
document.getElementById('registerForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    
    if (password !== confirmPassword) {
        alert('Пароли не совпадают');
        return;
    }
    
    // Здесь должна быть логика отправки данных на сервер
    console.log('Регистрация:', { email, password });
    window.location.href = 'login.html';
});