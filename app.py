from fastapi import FastAPI , Query
from pydantic import BaseModel
import random   
from pydantic import EmailStr

app = FastAPI()
class College(BaseModel):
    Mean:float
    Median:float
    Mode:float
    Count:float
    Min:float
    Max:float
    secret_key:int
@app.get("/input")
def college_Data(email: EmailStr = Query(...)):
    secret_key =  random.randint(1000000000, 9999999999)
    Y = [1,70,80,20,90,30] 
    return {"Data" : Y , "Secret" : secret_key}

@app.post("/submit")
def submit_data(item:College , email: EmailStr = Query(...)):
    item = item.dict()
    statistics = {
        "Size": item["Count"],
        "Min": item["Min"],
        "Max": item["Max"],
        "Mean": item["Mean"],
        "Median": item["Median"],
        "Mode": item["Mode"],
    }
    
    return {"message": "Data submitted successfully", "data": statistics}
