from mistralai import Mistral


# api_key = os.getenv("Z2512ZRS2O2mgHjJYCzlA98QjjmzlqfB")
client = Mistral(api_key="Z2512ZRS2O2mgHjJYCzlA98QjjmzlqfB")


document = {
    "type": "image_url",
    "image_url": "https://uniformsoftware.com/template/screenshots/wholesale-produce-distributor-invoice.webp"
}
# https://uniformsoftware.com/template/screenshots/wholesale-produce-distributor-invoice.webp
# https://images.template.net/wp-content/uploads/2015/10/30162134/Retail-Sales-Invoice-Template.jpg
# https://ordercircle.com/wp-content/uploads/invoice-1.png
ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document
)


print("Extracted Content:")
for i, page in enumerate(ocr_response.pages):
    print(f"--- Page {i + 1} ---")
    print(page.markdown)

ocr_text = "\n".join([page.markdown for page in ocr_response.pages])

