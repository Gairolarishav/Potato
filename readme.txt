docker Run command

1. docker run -t --rm -p 8501:8501 -v /home/rshavgairola/Documents/Projects/Potato:/Potato tensorflow/serving --rest_api_port=8501 --model_config_file=/Potato/models.config
2. change this (/home/rshavgairola/Documents/Projects/Potato) to the location where your models.config present.
3. after running docker also run fast api server
4. import tensorflow,pillow,fastapi,uvicorn,requests,numpy