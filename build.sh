#!/usr/bin/env bash

# We inline references because openapi-python-client does not support references within responses
echo "Inlining swagger references"
python -c "import json, jsonref; spec = jsonref.loads(open('swagger-clerk.json').read(), load_on_repr=True); open('swagger-clerk-inlined.json', 'w').write(json.dumps(spec, indent=2))"

openapi-python-client generate --path swagger-clerk-inlined.json --overwrite --output-path build/

rm -rf ./clerk_backend_api_client
mv ./build/* ./
