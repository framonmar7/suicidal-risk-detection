from drf_yasg import openapi

comment_param = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "comment": openapi.Schema(
            type=openapi.TYPE_STRING,
            example="I don't want to live anymore"
        ),
    },
    required=["comment"],
)

success_text_response = openapi.Response(
    description="Binary classification result",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "label": openapi.Schema(type=openapi.TYPE_STRING, enum=["NO_RISK", "RISK"], example="RISK"),
            "score": openapi.Schema(type=openapi.TYPE_NUMBER, format="float", example=0.9231),
        },
        required=["label", "score"],
    ),
)

bad_text_response = openapi.Response(
    description="Invalid input text (empty, too short, or too long)",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "error": openapi.Schema(type=openapi.TYPE_STRING, example="Empty comment"),
        },
        required=["error"],
    ),
)

internal_error_response = openapi.Response(
    description="Internal server error",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "error": openapi.Schema(type=openapi.TYPE_STRING, example="Unexpected error while processing the text"),
        },
        required=["error"],
    ),
)

text_responses = {
    200: success_text_response,
    400: bad_text_response,
    500: internal_error_response,
}
