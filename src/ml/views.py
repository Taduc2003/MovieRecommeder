from django.shortcuts import render
from django.views.decorators.http import require_GET

# Create your views here.
from django.http import JsonResponse
from ml.tasks import batch_users_prediction_task


# API thực hiện cả retrain rồi mới gợi ý
@require_GET
def api_recommend_for_user(request):
    user_id = request.GET.get("user_id")
    if not user_id or not user_id.isdigit():
        return JsonResponse({"error": "Missing or invalid user_id"}, status=400)
    batch_users_prediction_task(users_ids=[int(user_id)], offset=50, max_pages=1)
    return JsonResponse({"status": "Recommendation started for user", "user_id": user_id})