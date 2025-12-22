    text={
    "format": {
      "type": "json_schema",
      "name": "person",
      "strict": True,
      "schema": {
        "type": "object",
        "properties": {
          "step": {
            "type": "string",
          },
          "content": {
            "type": "string",
          }
        },
        "required": [
          "step",
          "content"
        ],
        "additionalProperties": False
      }
    }
  }