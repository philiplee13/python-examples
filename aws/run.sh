#!/bin/bash

aws s3api create-bucket --bucket test-bucket
aws s3api create-bucket --bucket new-bucket
aws s3api put-object --bucket test-bucket --key 5gb-file --body test-files/random_5gb_file