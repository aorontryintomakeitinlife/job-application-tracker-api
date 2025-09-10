from django.http import JsonResponse
from .models import JobApplication
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def job_list(request):
    if request.method == "GET":
        jobs = list(JobApplication.objects.values())
        return JsonResponse(jobs, safe=False)
    
    if request.method == "POST":
        data = json.loads(request.body)
        job = JobApplication.objects.create(
            company_name=data.get('company_name', ''),
            position=data.get('position', ''),
            status=data.get('status', 'APPLIED'),
            notes=data.get('notes', '')
        )
        return JsonResponse({"id": job.id, "message": "Job created"}, status=201)
