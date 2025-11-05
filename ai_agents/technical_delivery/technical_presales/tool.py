def answer_technical(topic: str) -> str:
    """Return a short technical explanation / recommended stack for a topic."""
    topic_lower = topic.lower()
    if "webrtc" in topic_lower or "video" in topic_lower:
        return "Recommended: WebRTC + SFU (e.g., mediasoup) for scaling real-time video. Use Node + STUN/TURN."
    if "ml" in topic_lower or "ai" in topic_lower:
        return "Recommended: Python backend with PyTorch/TensorFlow; deploy models on GPU or Vertex AI for production."
    return f"I can answer detailed technical questions about: {topic}"
