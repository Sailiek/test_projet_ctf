document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const user = document.getElementById('username').value;
    const pass = document.getElementById('password').value;
    const message = document.getElementById('message');

    // On envoie les données au serveur Flask
    const response = await fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: user, password: pass })
    });

    const result = await response.json();

    if (result.success) {
        message.style.color = "green";
        message.textContent = result.message;
    } else {
        message.style.color = "red";
        message.textContent = result.message;
    }
});