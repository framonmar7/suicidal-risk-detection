from drf_yasg import openapi

text_output_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "label": openapi.Schema(
            type=openapi.TYPE_STRING,
            enum=["NO_RISK", "RISK"],
            example="RISK"
        ),
        "score": openapi.Schema(
            type=openapi.TYPE_NUMBER,
            format="float",
            example=0.9231
        ),
    },
    required=["label", "score"],
)

error_output_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "error": openapi.Schema(type=openapi.TYPE_STRING, example="Error message here"),
    },
    required=["error"],
)

empty_text_response = openapi.Response(
    description="Empty or invalid input text",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "error": openapi.Schema(
                type=openapi.TYPE_STRING,
                example="Empty comment."
            )
        },
        required=["error"],
    ),
)

internal_error_response = openapi.Response(
    description="Internal server error",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "error": openapi.Schema(
                type=openapi.TYPE_STRING,
                example="Unexpected error while processing the text"
            )
        },
        required=["error"],
    ),
)

text_responses = {
    200: text_output_schema,
    400: empty_text_response,
    500: internal_error_response,
}
