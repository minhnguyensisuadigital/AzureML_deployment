# AzureML_deployment
Deploy pretrained model to Azure using Python SDK


Prerequisites:
- Jupyter Notebook
- Docker
- Python 

Deployment: using deploy.ipynb
- Provide Azure workspace credentials and model local path
- Fix ./source_dir/score.py if nescessary
- Run deploy.ipynb

Inference:
- URL: scoring_uri
- Access token: headers["Authorization"]
