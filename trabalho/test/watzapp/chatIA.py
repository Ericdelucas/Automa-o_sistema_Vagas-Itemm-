import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Baixa recursos básicos do NLTK
nltk.download('punkt')

# Base de conhecimento simples (você pode expandir)
base_conhecimento = {
    "oi": ["Olá! Como posso te ajudar?", "Oi! Tudo bem?"],
    "tudo bem": ["Tudo ótimo! E com você?", "Estou bem, obrigado por perguntar!"],
    "qual seu nome": ["Sou um assistente virtual feito em Python com Scikit-learn."],
    "o que voce faz": ["Posso responder perguntas básicas e conversar com você!"],
    "adeus": ["Até logo!", "Tchau! Foi bom conversar com você!"],
    "quem te criou": ["Fui criado por um desenvolvedor que usa Scikit-Learn e Python!"],
    "default": ["Desculpe, não entendi. Pode reformular sua pergunta?"]
}

# Cria listas para treino
perguntas = list(base_conhecimento.keys())
respostas = list(base_conhecimento.values())

# Vetorizador
vectorizer = CountVectorizer().fit_transform(perguntas)
tfidf = TfidfTransformer().fit_transform(vectorizer)

def responder(texto_usuario):
    # Converte a entrada para minúsculas
    texto_usuario = texto_usuario.lower()

    # Adiciona o texto do usuário no vetor e calcula similaridade
    entrada_vec = CountVectorizer(vocabulary=vectorizer.vocabulary_).fit_transform([texto_usuario])
    entrada_tfidf = TfidfTransformer().fit_transform(entrada_vec)
    similaridades = cosine_similarity(entrada_tfidf, tfidf)

    # Pega o índice da melhor correspondência
    indice = similaridades.argmax()

    # Responde com a melhor opção
    if similaridades.max() < 0.3:
        return random.choice(base_conhecimento["default"])
    else:
        return random.choice(respostas[indice])

# Loop de conversa
print("🤖 Chat IA (Scikit-learn)\nDigite 'sair' para encerrar.\n")
while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Chat: Até mais! 👋")
        break
    resposta = responder(user_input)
    print("Chat:", resposta)
