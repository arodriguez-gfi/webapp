// comment
pipeline {
 agent any
 stages {
        stage('Checkout-git'){
               steps{
		git poll: true, url: 'https://github.com/arodriguez-gfi/webapp.git'
               }
        }
        stage('TestApp') {
            steps {
            	sh '''
            		bash -c "cd webapp && pytest && cd .."
                '''
            }
        }  
        stage('RunApp') {
            steps {
            	sh '''
            		bash -c "python webapp/main.py &"
                '''
            }
        } 
        stage('BuildDocker') {
            steps {
            	sh '''
            		sudo docker build -t apptest:latest .
                '''
            }
        } 
    stage('PushDockerImage') {
            steps {
            	sh '''
            		sudo docker tag apptest:latest albertorodgz/apptest:latest
			sudo docker push albertorodgz/apptest:latest
			sudo docker rmi apptest:latest
                '''
            }
        } 
  }
}
