pipeline {
    agent any
	 options {
	    disableConcurrentBuilds()
	  }
    stages {
        stage('Virtualenv configuration') {
         steps {
            sh '''#!/bin/bash
                git clean -d -x -f
                pwd
                mkdir tmp
                rm -rf venv
                virtualenv --python=/usr/bin/python3.5 venv
                source venv/bin/activate
                python --version
                #pip install -r ./requirements.txt
                pip install pytest
            '''
      }
        }
	stage('Running tests') {
		steps {
		  sh '''#!/bin/bash
			source venv/bin/activate
			python --version
			export PYTHONPATH=\$PYTHONPATH:\$PWD
			py.test test.py --junitxml tests.xml
		    '''
		}
	}
    }
  post {
    always {
        junit '**/tests.xml'
        cleanWs()
    }
  }
}
