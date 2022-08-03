
//#region dark and light toggle tailwind
const themeBtn = document.querySelector('#themeToggle')
const themeSwitch = document.querySelector('span.switch')
let currentTheme

function getCurrentTheme() {
    let theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    localStorage.getItem('amartislab.theme') ? theme=localStorage.getItem('amartislab.theme') : null
    return theme
}

function loadTheme(theme) {
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
//#endregion

//#region nav
let lastScroll = 0;
const nav = document.getElementById("navbar-sticky");
document.getElementById("hero").style.height = nav.offsetHeight + "px";

window.addEventListener("scroll", () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll <= 0) {
        nav.classList.remove("show");
    }
    if (currentScroll > lastScroll && !nav.classList.contains("hidden")) {
        nav.classList.remove("show");
        nav.classList.add("hidden");
    }
    if (currentScroll < lastScroll && nav.classList.contains("hidden")) {
        nav.classList.remove("hidden");
        nav.classList.add("show");
    }
    lastScroll = currentScroll;
});
//#endregion