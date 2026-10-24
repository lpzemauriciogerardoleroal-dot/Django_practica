import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from saludo.domain.persona import Persona
from saludo.application.services.saludar_service import SaludarService

@csrf_exempt
def saludar_view(request):
    nombre = "Brandon"

    # Si mandan datos por POST, los lee. Si es por GET, usa "Brandon" por defecto.
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre', 'Brandon')
        except:
            pass

    persona = Persona(nombre=nombre)
    service = SaludarService()
    mensaje = service.ejecutar(persona)

    return JsonResponse({"mensaje": mensaje})