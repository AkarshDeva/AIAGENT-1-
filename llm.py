from dotenv import load_dotenv

load_dotenv()


def get_llm(provider="gemini"):
    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            temperature=0
        )

    raise ValueError("Unknown provider. Please choose a valid provider.")
