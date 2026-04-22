print("Multi-Agent system started...")

import ollama

# function to call AI
def ask_ai(prompt):
    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

# Planner Agent
def planner(task):
    return ask_ai("Break this task into simple steps:\n" + task)

# Writer Agent
def writer(plan):
    return ask_ai("Write a clear answer using this plan:\n" + plan)

# Critic Agent
def critic(answer):
    return ask_ai("Improve this answer:\n" + answer)

# MAIN LOOP
while True:
    user_input = input("\nEnter your task (type exit to stop): ")

    if user_input.lower() == "exit":
        break

    print("\n🧠 Planning...")
    plan = planner(user_input)
    print(plan)

    print("\n✍️ Writing...")
    draft = writer(plan)
    print(draft)

    print("\n🔍 Improving...")
    final = critic(draft)

    print("\n✅ FINAL ANSWER:\n", final)