from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .inference.model import classifier

LABELS = {
    "LABEL_0": "NO_RISK",
    "LABEL_1": "RISK"
}

@api_view(["GET"])
def index(request):
    return Response({
        "message": "Welcome to the Suicide Risk Detection API",
        "endpoints": {
            "detect": "/api/detect"
        }
    })

@api_view(["POST"])
def detection_view(request):
    comment = request.data.get("comment", "").strip()

    if not comment:
        return Response({"error": "Empty comment."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        result = classifier(comment)[0]
        return Response({
            "label": LABELS.get(result["label"], result["label"]),
            "score": round(result["score"], 4)
        })
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
