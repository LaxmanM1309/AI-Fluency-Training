from config import client, MODEL, banner


question = "What is the fee for AI202 Machine Learning?"

banner("NO TOOL RUN")

print("Q:", question)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0
)

answer = response.choices[0].message.content

print("A:", answer)