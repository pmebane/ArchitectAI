import boto3
import streamlit as st
import json
import uuid

def upload_to_s3(path, json_object):
 
    try:
        file_id = str(uuid.uuid4().hex)
        s3 = boto3.resource(
                's3',
                region_name='us-west-2',
                aws_access_key_id= st.secrets["aws_access_key"],
                aws_secret_access_key= st.secrets["aws_secret_access_key"]
            )
        s3.Object('archie-app', path+'/'+file_id+'.json').put(Body=json.dumps(json_object))
 
        return True
    except FileNotFoundError:
        #time.sleep(9)
        #st.error('File not found.')
        return False   
    