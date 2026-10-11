from google.adk.agents import LlmAgent

root_agent = LlmAgent(
 model='gemini-2.5-flash',
 name='weather_agent',
 description='Weather agent on Cloud Run',
 instruction='''
 Eres un asistente meteorológico útil.
 Proporciona información sobre el clima de ciudades de todo el mundo.
 '''
)