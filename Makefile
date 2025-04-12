all: run
.PHONY: all run

requirements:
	@echo
	@echo "******************** INSTALLING SOFTWARE REQUIREMENTS **********************************"
	if [ -x /usr/bin/apt-get ]; then  xargs -a requirements.txt sudo apt-get install -y; fi
	@echo
	@echo
	


run: 	 
	@echo
	@echo "******************** DOWNLOADING (IF NECESSARY) AND RUNNING MODEL **********************************"
	@echo
	python ./src/huggingface_tests/main.py
	@echo


	


