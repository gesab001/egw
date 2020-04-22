#!/bin/bash
aws s3 sync . s3://egw.onecloudapps.net --exclude 'awss3sync.sh'
aws cloudfront create-invalidation --distribution-id E1U11FU0V8K37X --paths "/*"
