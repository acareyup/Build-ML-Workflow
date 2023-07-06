import json
import sagemaker
import base64
from sagemaker.predictor import Predictor
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-04-06-07-59-54-841"


def lambda_handler(event, context):

    ## TODO: fill in (Decoding the encoded 'Base64' image-data and class remains'bytes')
    image = base64.b64decode(event['body']['image_data']) 

     # Instantiate a Predictor
    predictor = Predictor(endpoint_name=ENDPOINT, sagemaker_session=sagemaker.Session())

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")

    # Make a prediction:
    inferences = predictor.predict(image)

    # We return the data back to the Step Function
    event["inferences"] = inferences.decode('utf-8')     
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)                       
    }
