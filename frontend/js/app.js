const form = document.getElementById("email-form");
const status = document.getElementById("status");
const button = document.getElementById("submit-btn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const subject = document.getElementById("subject").value.trim();
  const message = document.getElementById("message").value.trim();

  // validação simples
  if (!email || !subject || !message) {
    setStatus("Preencha todos os campos.", "error");
    return;
  }

  try {
    button.disabled = true;
    button.textContent = "Enviando...";

    const response = await fetch("http://localhost:8000/send-email", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        email,
        subject,
        message
      })
    });

    if (!response.ok) {
      throw new Error("Erro ao enviar");
    }

    setStatus("E-mail enviado com sucesso!", "success");
    form.reset();

  } catch (error) {
    setStatus("Erro ao enviar e-mail.", "error");
  } finally {
    button.disabled = false;
    button.textContent = "Enviar";
  }
});

function setStatus(message, type) {
  status.textContent = message;
  status.className = `status ${type}`;
}