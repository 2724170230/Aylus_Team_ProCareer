#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.cloud import automl
import pandas as pd

# TODO(developer): Uncomment and set the following variables
project_id = "balmy-tokenizer-328522"
model_id = "balmy-tokenizer-328522"
content = pd.read("job_information.csv")

prediction_client = automl.PredictionServiceClient()

# Get the full path of the model.
model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)

# Supported mime_types: 'text/plain', 'text/html'
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#textsnippet
text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
payload = automl.ExamplePayload(text_snippet=text_snippet)

response = prediction_client.predict(name=model_full_id, payload=payload)

for annotation_payload in response.payload:
    print(u"Predicted class name: {}".format(annotation_payload.display_name))
    print(
        u"Predicted class score: {}".format(annotation_payload.classification.score)
    )

