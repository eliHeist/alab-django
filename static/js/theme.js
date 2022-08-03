// dark and light toggle tailwind
const themeBtn = document.querySelector('#themeToggle')
const themeSwitch = document.querySelector('span.switch')
let currentTheme

function getCurrentTheme() {
    let theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    localStorage.getItem('amartislab.theme') ? theme=localStorage.getItem('amartislab.theme') : null
    return theme
}

function loadTheme(theme) {
    console.log('load theme');
    const root = document.querySelector('html')
    if (theme == 'light') {
        themeBtn.checked = true
        root.classList.remove('dark')
    } else {
        themeBtn.checked = false
        root.classList.add('dark')
    }
    currentTheme = theme
}

let x = 0
themeSwitch.addEventListener('click', () => {
    let theme = getCurrentTheme()
    if (theme === 'dark') {
        theme = 'light'
    }else{
        theme = 'dark'
    }
    localStorage.setItem('amartislab.theme', `${theme}`)
    loadTheme(theme)
})

loadTheme(getCurrentTheme())