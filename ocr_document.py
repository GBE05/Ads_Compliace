import httpx
import os

def ocr_image_base64(image_base64: str) -> str:
    api_key = os.getenv("TYPHOON_OCR_API_KEY", "sk-LeVrQgRVU7ZlPcUMihmohXqum6pTfZWTP7qXJmirvWN19Bdf")
    api_url = os.getenv("TYPHOON_OCR_API_URL", "http://localhost:7500/ocr")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "image": image_base64,
        "options": {"language": "tha+eng"}
    }

    response = httpx.post(api_url, json=payload, headers=headers, timeout=100000000)
    response.raise_for_status()

    result = response.json()
    return result.get("text", "")
