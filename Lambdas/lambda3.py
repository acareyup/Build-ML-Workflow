import json

THRESHOLD = 0.7

def lambda_handler(event, context):
    
    data = json.loads(event['body'])
    inferences = json.loads(data['inferences'])
    
    meets_threshold = inferences[0] > THRESHOLD or inferences[1] > THRESHOLD   

    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': event["body"]   
    }