import json

from config import client, MODEL, banner
from course_tool import read_course_fees


TOOL = {
    "type": "function",
    "function": {
        "name": "read_course_fees",
        "description": "Read the college course fee list from the external fee file.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}


question = "What is the fee for AI202 Machine Learning?"

banner("TOOL ENABLED RUN")

print("Q:", question)

messages = [
    {
        "role": "user",
        "content": question
    }
]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    tools=[TOOL],
    temperature=0
)

message = response.choices[0].message

if message.tool_calls:

    for call in message.tool_calls:

        print("\nTool call:")
        print("Name:", call.function.name)
        print("Arguments:", call.function.arguments)

        if call.function.name == "read_course_fees":

            result = read_course_fees()

            print("\nTool result:")
            print(result)

            messages.append({
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": [
                    {
                        "id": call.id,
                        "type": "function",
                        "function": {
                            "name": call.function.name,
                            "arguments": call.function.arguments
                        }
                    }
                ]
            })

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    final_response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    print("\nFinal answer:")
    print(final_response.choices[0].message.content)

else:

    print("\nNo tool was called.")

    print("Answer:")
    print(message.content)