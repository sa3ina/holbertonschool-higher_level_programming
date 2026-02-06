document.addEventListener('DOMContentLoaded', () => {
    const hello = document.getElementById('hello');

    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
        .then(response => response.json())
        .then(data => {
            hello.textContent = data.hello;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

