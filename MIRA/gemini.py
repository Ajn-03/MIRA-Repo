from google import genai
from django.conf import settings

#GenAI API 
def health_remarks(health_details):
    g = str(health_details.glucose)
    h = str(health_details.haemoglobin)
    c = str(health_details.cholesterol)
    client = genai.Client(api_key=settings.GEMINI_API_KEY)#accesses api key and returns remarks to helath view
    response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents="Offer general health remarks in just 2 lines when glucose = "+g+" haemoglobin HbA1c% = "+h+" cholesterol = "+c)
    return response.text
        
    
        