#!/bin/bash

# lambda stuff
# zip function.zip main.py
# aws lambda create-function \
#   --function-name my-function \
#   --zip-file fileb://function.zip \
#   --handler main.handler \
#   --runtime python3.12 \
#   --role arn:aws:iam::123456789012:role/execution_role

#   aws lambda invoke --function-name my-function \                                                                ─╯
#     --payload file://test-files/test.json output.txt


# eventbridge
aws events put-rule \
    --name my-custom-rule \
    # --event-pattern "{\"source\":[\"test\"],\"detail-type\":[\"test-detail-type\"]}, \"detail\":{\"message\":[\"test-value\"]}" \

aws events put-targets \
    --rule my-custom-rule \
    --targets file://test-files/targets.json