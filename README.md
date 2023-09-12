
# installations

1. install requirements
```
pip install -r requirements.txt
```

2. init your `.env`
```bash
cp .env.example .env
```
then put your API key in the .env file

## issues 
- M1/M2 installations refer to reinstalling the grpcio [grpcio issue](https://github.com/Chainlit/chainlit/issues/56)

https://docs.trychroma.com/




# Run
## in docker
```
docker-compose up --build
```
## Local Environnment development mode

1. run chainlit interface
```bash
chainlit run main.py -w --port 8001

# or 

chainlit run main.py -w 

```


2. run langflow interface
```
langflow
```