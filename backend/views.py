from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from backend.inference.model import classifier
from backend.docs.schemas import comment_param, text_responses
from backend.validators import load_and_validate_text, EmptyText, TextTooShort, TextTooLong

LABELS = {
    "LABEL_0": "NO_RISK",
    "LABEL_1": "RISK"
}

def index(request):
    return JsonResponse({
        "message": "Welcome to the Suicide Risk Detection API",
        "endpoints": {
            "detect": "/api/detect"
        },
        "docs": "/docs"
    })

@swagger_auto_schema(
    method="post",
    operation_id="suicidalRiskDetection",
    operation_summary="Return whether a text comment shows risk indicators or not",
    request_body=comment_param,
    responses=text_responses,
    tags=["Classification"],
)
@api_view(["POST"])
def detection_view(request):
    try:
        comment = load_and_validate_text(request.data.get("comment"))
        result = classifier(comment)[0]
        return Response({
            "label": LABELS.get(result["label"], result["label"]),
            "score": round(result["score"], 4)
        })
    except (EmptyText, TextTooShort, TextTooLong) as e:
        return Response(e.detail, status=e.status_code)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
