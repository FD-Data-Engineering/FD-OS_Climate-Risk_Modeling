
# FD-OS_Climate-Risk_Modeling

Solution Demo with 2 steps

  - WebApp launch script 

  user@x:/.../FD-OS_Climate-Risk_Modeling/$ ./launch-webapp.sh 

 -  Open in browser http://localhost:5000/<model-template.html> 

Risk modeling tools including

  - Python Machine Learning OSF risk model 

  - Solidatus Taxonomy 
  
  - WebApp for model demonstrations


  - - Our WebApp allow analysis of risk scenarios in our datapoints

  WebApp  http://localhost:5000/
![Alt text](images/osf-data-maps-tool-entry-point-1.png?raw=true "WebApp home")
  
  Macro level
![Alt text](images/floodability-macro-level-2.png?raw=true "Floodability risk macro-level")


  Low level
![Alt text](images/floodability-low-level-3.png?raw=true "Property detail low-level")


  Floodability HeapMap
![Alt text](images/floodability-heatmap-2.png?raw=true "Floodability HeapMap")



  - - Python Machine Learning

  Model build via script using Pytorch machine learning NNs 


  user@x:/.../FD-OS_Climate-Risk_Modeling/$ ./build-model.sh   
  
![Alt text](images/neural-training-1.png?raw=true "Model Training 1")

![Alt text](images/neural-training-2.png?raw=true "Model Training 2")

![Alt text](images/neural-training-3.png?raw=true "Model Training 3")

# Solution - Github Actions

The First Derivatives Open Sustainable Finance OSF 
  
  We are open source our Open SF tools to the community

  - Python Flask Modeling interactive Tool


  - - Here we built a python flask interactive webapp and a osf_risk_model on pytorch.nn using github actions

  - - $ vi .github/python-app.yml


![Alt text](images/interactive-build-github-1.png?raw=true "Interactive build 1")

![Alt text](images/interactive-build-github-2.png?raw=true "Interactive build 2")

![Alt text](images/interactive-build-github-3.png?raw=true "Interactive build 3")

