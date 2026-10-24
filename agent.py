import ollama

video_idea = input("What video do you want to create? ")

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": f"""You are the director of my AI video generator.

Turn this video idea into a simple 5-shot plan for a 30-second video.

For each shot, give:
- Time
- Visual description
- What happens

Keep each shot around 6 seconds.

Video idea: {video_idea}"""
        }
    ]
)

print(response["message"]["content"])