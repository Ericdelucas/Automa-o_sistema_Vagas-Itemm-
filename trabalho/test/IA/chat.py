import random
import nltk
import requests
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Baixa recursos do NLTK (só na 1ª execução)
nltk.download('punkt', quiet=True)

# 🧠 Base local simples (respostas diretas)
base_conhecimento = {
    "oi": ["Olá! Como posso te ajudar?", "Oi! Tudo bem?"],
    "ola": ["Olá! Tudo certo?", "Oi! Prazer em te ver por aqui!"],
    "bom dia": ["Bom dia ☀️ Espero que tenha um ótimo dia!", "Bom dia! Como posso ajudar?"],
    "boa tarde": ["Boa tarde 🌞 Tudo bem contigo?", "Boa tarde! O que deseja saber hoje?"],
    "boa noite": ["Boa noite 🌙 Como foi o seu dia?", "Boa noite! Está tudo bem por aí?"],
    "tudo bem": ["Tudo ótimo! E com você?", "Estou bem, obrigado por perguntar 😄"],
    "quem te criou": ["Fui criado por um desenvolvedor Eric De Lucas com Scikit-Learn e IA local com Ollama!"],
    "qual seu nome": ["Sou o PyBot 🤖, um assistente híbrido com inteligência artificial local!"],
    "o que voce faz": ["Posso responder perguntas simples e também gerar textos, resumos ou ideias com IA local."],
    "adeus": ["Até logo!", "Tchau! Foi bom conversar com você 👋"],
    "default": ["Desculpe, não entendi. Vou pensar melhor sobre isso 😅"]
}

# Vetorização para busca semântica local
perguntas = list(base_conhecimento.keys())
respostas = list(base_conhecimento.values())
vectorizer = CountVectorizer()
X_counts = vectorizer.fit_transform(perguntas)
tfidf = TfidfTransformer().fit_transform(X_counts)


def responder_local(texto_usuario):
    """Busca respostas rápidas na base local."""
    texto_usuario = texto_usuario.lower()
    entrada_counts = vectorizer.transform([texto_usuario])
    entrada_tfidf = TfidfTransformer().fit_transform(entrada_counts)
    similaridades = cosine_similarity(entrada_tfidf, tfidf)
    indice = similaridades.argmax()

    if similaridades.max() < 0.35:
        return None
    else:
        return random.choice(respostas[indice])


def responder_ia(texto_usuario):
    """Usa modelo local do Ollama (respostas longas e inteligentes)."""
    try:
        # Parâmetros otimizados para textos complexos e maiores
        payload = {
            "model": "llama3",              # ou "phi3" se quiser leve
            "prompt": texto_usuario,
            "stream": True,                 # Ativa modo streaming
            "options": {
                "temperature": 0.7,         # Criatividade moderada
                "num_predict": 1024,        # Permite respostas longas (~4k tokens)
                "top_p": 0.9                # Controle de diversidade
            }
        }

        resposta = ""
        with requests.post("http://localhost:11434/api/generate", json=payload, stream=True, timeout=300) as resp:
            for line in resp.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        if "response" in data:
                            print(data["response"], end="", flush=True)
                            resposta += data["response"]
                    except json.JSONDecodeError:
                        pass
        print()
        return resposta.strip() or "🤔 Não consegui formular uma resposta agora."

    except requests.exceptions.ConnectionError:
        return "⚠️ O Ollama não está rodando. Inicie com: ollama serve"
    except Exception as e:
        return f"⚠️ Erro ao gerar resposta: {e}"


# 💬 Loop principal
print("🤖 Chat Híbrido IA (Modo Local - Ollama)\nDigite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("PyBot: Até mais! 👋")
        break

    resposta_local = responder_local(user_input)

    if resposta_local:
        print("PyBot:", resposta_local)
    else:
        print("PyBot (IA pensando... 🤔)")
        resposta_gerada = responder_ia(user_input)
        print("\nPyBot:", resposta_gerada)
