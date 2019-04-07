from django.http import JsonResponse


def error(msg, status=400):
  res = dict(error=msg)
  return JsonResponse(res, status=status)
