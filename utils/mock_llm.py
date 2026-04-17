# -*- coding: utf-8 -*-
"""
OpenAI LLM — dùng API key thật để gọi OpenAI GPT-4.
"""
import os
from openai import OpenAI

# Khởi tạo OpenAI client với API key từ environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask(question: str) -> str:
    """
    Gọi OpenAI API thật để lấy câu trả lời từ GPT-4.
    """
    if not os.getenv("OPENAI_API_KEY"):
        return "Lỗi: Thiếu OPENAI_API_KEY. Vui lòng set environment variable."
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Bạn là một trợ lý AI thông minh và hữu ích. Hãy trả lời câu hỏi của người dùng một cách chi tiết và chính xác."},
                {"role": "user", "content": question}
            ],
            max_tokens=200,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Lỗi khi gọi OpenAI API: {str(e)}"