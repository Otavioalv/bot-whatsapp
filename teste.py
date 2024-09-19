import openai

# Coloque sua chave da API da OpenAI aqui
openai.api_key = "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"

def gerar_resposta(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Você pode usar o modelo GPT-4 se tiver acesso
        prompt=prompt,
        max_tokens=100,  # Limite de tokens na resposta
        n=1,  # Número de respostas que você quer gerar
        stop=None,  # Parada, quando você quer encerrar a geração
        temperature=0.7,  # Controle de criatividade (0.0 a 1.0)
    )
    return response.choices[0].text.strip()

# Exemplo de uso
prompt = "Explique o conceito de aprendizado supervisionado"
resposta = gerar_resposta(prompt)
print(resposta)
