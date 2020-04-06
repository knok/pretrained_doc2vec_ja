#!/bin/sh

PYTHON_BASE=$(which python|sed -e 's!/bin/python!!')
PY4J_PATH=$PYTHON_BASE/share/py4j/py4j0.10.9.jar

javac -cp sudachi-0.3.2.jar:$PY4J_PATH:.  jsudachi.java
java -cp sudachi-0.3.2.jar:$PY4J_PATH:.  jsudachi
