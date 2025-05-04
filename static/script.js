const chatBox = document.getElementById("chat");
const messageInput = document.getElementById("mensagem");
const emptyState = document.getElementById("empty-state");
const typingIndicator = document.getElementById("typing-indicator");

// Função para adicionar uma mensagem ao chat
function addMessage(text, sender) {

    if (emptyState && chatBox.contains(emptyState)) {
        emptyState.style.display = 'none';
    }

    const messageElement = document.createElement("div");
    messageElement.classList.add("message", `message--${sender}`); // Adiciona classes para styling

    // Cria a bolha da mensagem
    const bubbleElement = document.createElement("div");
    bubbleElement.classList.add("message-bubble", `message-bubble--${sender}`);
    bubbleElement.innerHTML = text.replace(/\n/g, "<br>"); // Permite quebras de linha


    // Adiciona a bolha à mensagem. A ordem depende de quem manda a mensagem
    if (sender === 'sent') {
         messageElement.appendChild(bubbleElement);
    } else { // received (bot)
        messageElement.appendChild(bubbleElement);
    }


    chatBox.appendChild(messageElement);

    // Rola para a última mensagem com animação suave (se suportado)
    setTimeout(() => {
        messageElement.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }, 100); 
}

// Função para enviar mensagem
function enviar() {
    let mensagem = messageInput.value.trim();
    if (mensagem === "") return; // Evita enviar mensagem vazia

    addMessage(mensagem, "sent"); // Adiciona a mensagem do usuário COMO "sent"

    // Mostra indicador de digitação
    showTypingIndicator();

    // Limpa a caixa de mensagem ANTES de enviar a requisição
    messageInput.value = "";

    fetch("/perguntar", {
        method: "POST",
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: "mensagem=" + encodeURIComponent(mensagem)
    })
    .then(res => {
         if (!res.ok) {
            // Lidar com erros de resposta HTTP (ex: 404, 500)
            throw new Error(`Erro HTTP! Status: ${res.status}`);
         }
         return res.json();
    })
    .then(data => {
        hideTypingIndicator();

        // Adiciona a resposta do bot
        // Verifica se data.resposta existe e não é nula/vazia
        if (data && data.resposta) {
             addMessage(data.resposta, "received"); // CHAMA COMO "received"
        } else {
             // Caso a resposta do bot esteja vazia ou com formato inesperado
             console.warn("Resposta do bot vazia ou inesperada:", data);
             addMessage("Desculpe, não recebi uma resposta válida do bot.", "received"); // CHAMA COMO "received"
        }
    })
    .catch(error => {
        // Esconde indicador de digitação em caso de erro
        hideTypingIndicator();
        console.error("Erro ao comunicar com o backend:", error);
        // Opcional: adicionar uma mensagem de erro no chat
        addMessage("Desculpe, não consegui obter uma resposta no momento. Erro: " + error.message, "received"); // CHAMA COMO "received"
    });
}

// Função para verificar tecla Enter no input
function checkEnter(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Evita quebra de linha padrão no input
        enviar();
    }
}

// Função para mostrar o indicador de digitação
function showTypingIndicator() {
    // Remove o estado vazio se ele ainda estiver visível ao começar a digitar/enviar
    if (emptyState && chatBox.contains(emptyState)) {
        emptyState.style.display = 'none';
    }

    const chatBody = chatBox.parentElement; 
    const nextElement = chatBox.nextElementSibling; 

    if (typingIndicator && chatBody) {

        if (!nextElement || nextElement.id !== 'typing-indicator' || typingIndicator.parentElement !== chatBody) {
             chatBody.insertBefore(typingIndicator, chatBox.nextElementSibling);
        }
    }

    if (typingIndicator) {
       typingIndicator.style.display = 'flex'; // Use 'flex' para alinhar os pontos
    }
}

// Função para esconder o indicador de digitação
function hideTypingIndicator() {
     if (typingIndicator) {
        typingIndicator.style.display = 'none';
     }

     const children = chatBox.children;
     let onlyEmptyState = false;
     if (children.length === 1 && children[0].id === 'empty-state') {
         onlyEmptyState = true;
     } else if (children.length === 0) {
         // Se não tem filhos nenhum, também consideramos vazio
         onlyEmptyState = true;
     }


     if (onlyEmptyState && emptyState) {
         emptyState.style.display = 'flex'; // Mostra o estado vazio
         // Garante que o emptyState seja o único filho na prática, removendo outros se existirem por algum erro
          while (chatBox.children.length > 1) {
              if (chatBox.children[0].id !== 'empty-state') {
                  chatBox.removeChild(chatBox.children[0]);
              } else {
                  chatBox.removeChild(chatBox.children[1]);
              }
          }
     }
}

// Inicialização: verifica se o chat está vazio ao carregar a página
document.addEventListener('DOMContentLoaded', (event) => {
    // Verifica se o chatBox está vazio ou só contém o emptyState
     const children = chatBox.children;
     let hasNonEmptyStateChildren = false;
     for (let i = 0; i < children.length; i++) {
         if (children[i].id !== 'empty-state') {
             hasNonEmptyStateChildren = true;
             break;
         }
     }

    if (!hasNonEmptyStateChildren && emptyState) {
        emptyState.style.display = 'flex';
        // Garante que o emptyState seja o único filho visível no carregamento
         while (chatBox.children.length > 1) {
             if (chatBox.children[0].id !== 'empty-state') {
                  chatBox.removeChild(chatBox.children[0]);
             } else {
                 chatBox.removeChild(chatBox.children[1]);
             }
         }
    } else if (emptyState) {
        emptyState.style.display = 'none';
    }
});