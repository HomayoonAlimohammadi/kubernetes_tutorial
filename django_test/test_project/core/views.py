from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


User = get_user_model()


@require_http_methods(["GET"])
def user_list(request):
    qs = User.objects.all()
    user_dict = {user.pk: model_to_dict(user) for user in qs}
    return JsonResponse(user_dict)


@require_http_methods(["GET"])
def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    return JsonResponse(model_to_dict(user))


@csrf_exempt
@require_http_methods(["POST"])
def user_create(request):
    user = User(
        username=request.POST.get("username"),
        email=request.POST.get("email"),
    )
    user.save()
    return JsonResponse(model_to_dict(user))
